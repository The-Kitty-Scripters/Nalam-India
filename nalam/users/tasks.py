from django.contrib.auth import get_user_model

from config import celery_app
from nalam.email_sendgrid.views import send_thank_you_email

User = get_user_model()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()


@celery_app.task()
def send_email(d):
    send_thank_you_email(d)
