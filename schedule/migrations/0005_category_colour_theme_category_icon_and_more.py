# Generated by Django 5.0.6 on 2024-05-24 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0004_rename_address_venue_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="colour_theme",
            field=models.CharField(
                choices=[("YELLOW", "Yellow"), ("ORANGE", "Orange"), ("PINK", "Pink"), ("PURPLE", "Purple")],
                default="PURPLE",
                max_length=32,
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="icon",
            field=models.CharField(
                choices=[
                    ("MASK", "Mask"),
                    ("TRUMPET", "Trumpet"),
                    ("BALLET_SHOES", "Ballet Shoes"),
                    ("MICROPHONE", "Microphone"),
                    ("PAINTBRUSH", "Paintbrush"),
                ],
                default="MASK",
                max_length=32,
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="advertisement_weight",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="event",
            name="primary_category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="primary_category",
                to="schedule.category",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="slug",
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="organisation",
            name="slug",
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
