# Generated by Django 5.0.6 on 2024-05-28 16:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0011_category_icon_alter_event_logo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="public_description",
            new_name="short_description",
        ),
    ]
