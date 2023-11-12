# Create your models here.
from django.db import models

LOCATION_CHOICES = [
    ("In-School", "In-school at orphanage"),
    ("LOC2", "1-year vocational training"),
    ("LOC3", "2-year vocational training"),
    ("LOC3", "2-year junior college"),
    ("LOC3", "3-year college"),
    ("LOC3", "4-year college"),
    ("LOC3", "3-year university"),
    ("LOC3", "4-year university"),
]

BACKGROUND_CHOICES = [
    ("OR", "Orphan"),
    ("HALF", "Half-Orphan"),
    ("DEST", "Destitute"),
    ("OTHER", "Other: Not in the orphanage"),
]


class Girls(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    unique_id = models.CharField()
    background = models.CharField(max_length=50, choices=BACKGROUND_CHOICES, default="OR")
    DOB = models.DateTimeField()
    year_joined_orphanage = models.CharField()
    current_location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default="In-School")
    year_of_graduation = models.CharField(max_length=4, default="2000")
    dream_job = models.CharField(default="N/A")
    year_self_sufficiency = models.CharField(max_length=4, default="2000")
    time_to_self_sufficency = models.CharField(max_length=4, default="2000")
    estimate_funding = models.DecimalField(max_digits=10, decimal_places=2, default="0")
    picture_url = models.URLField(default="")
    explicit_permission = models.BooleanField(default=False)
    personal_story = models.CharField(default="")
