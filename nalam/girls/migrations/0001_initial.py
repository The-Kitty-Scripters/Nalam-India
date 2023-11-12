# Generated by Django 4.2.7 on 2023-11-12 03:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Girls",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("unique_id", models.CharField()),
                ("DOB", models.DateTimeField()),
                ("year_joined_orphanage", models.DateTimeField()),
            ],
        ),
    ]
