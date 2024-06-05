# Generated by Django 5.0.6 on 2024-05-27 22:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0007_venue_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="images/event-logos/"),
        ),
        migrations.AddField(
            model_name="organisation",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="images/organisation-logos/"),
        ),
    ]
