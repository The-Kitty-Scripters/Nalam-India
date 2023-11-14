import stripe
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from nalam.email_sendgrid.views import send_thank_you_email
from nalam.subscriptions.models import PaymentHistory
from nalam.users.admin import User

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(request):
    if request.method == "POST":
        try:
            site_base_url = "http://localhost:3000/"

            success_url = site_base_url + reverse_lazy("subscriptions:checkout-success")
            cancel_url = site_base_url + reverse_lazy("subscriptions:checkout-canceled")

            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price": "price_1OBij0L3io6xXWmkXVuFRxJ7",
                        "quantity": 1,
                    },
                ],
                mode="subscription",
                allow_promotion_codes=True,
                success_url=success_url,
                cancel_url=cancel_url,
            )
        except Exception as e:
            return JsonResponse({"error": f"Problems creating checkout session {e}"}, status=400)

        return redirect(checkout_session.url, code=303)


@csrf_exempt
def stripe_webhook(request):
    stripe_webhook_endpoint = settings.STRIPE_WEBHOOK_SECRET_ENDPOINT
    payload = request.body
    sig_header = request.headers["stripe-signature"]
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, stripe_webhook_endpoint)
    except ValueError as e:
        return HttpResponse(e, status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(e, status=400)

    # Passed signature verification

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        # ---------------- mikey --------------------- #
        # this is generally where you create the order and mark it as awaiting payment
        # Something.create_order(session["id"])
        session_id = session["id"]
        customer_email = session["customer_details"]["email"]

        user = User.objects.create(name=session["customer_details"]["name"], email=customer_email)

        # note: ignore this I just hard coded it b/c I didn't feel like converting it to decimals
        amount = session["amount_total"]

        payment_history = PaymentHistory.objects.create(
            subscription_id="",
            session_id=session_id,
            product_id="price_1OBij0L3io6xXWmkXVuFRxJ7",
            amount_total=399.99,
        )

        if session.payment_status == "paid":
            # this is where you fulfill the order
            # TODO: create and send email, see line 64
            send_thank_you_email(user, amount)
            payment_history.paid = True
            payment_history.save

    return HttpResponse(status=200)
