from django.core.validators import MinValueValidator
from django.db import models


class PaymentHistory(models.Model):
    subscription_id = models.CharField(max_length=255)
    session_id = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    amount_total = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    paid = models.BooleanField(default=False)
