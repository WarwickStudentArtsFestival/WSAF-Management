# Generated by Django 5.0.6 on 2024-05-16 23:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Venue",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("address", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Organisation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("admins", models.ManyToManyField(related_name="events_admin", to=settings.AUTH_USER_MODEL)),
                (
                    "participants",
                    models.ManyToManyField(related_name="events_participating", to=settings.AUTH_USER_MODEL),
                ),
                (
                    "organisation",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="schedule.organisation"
                    ),
                ),
                ("submission_id", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="EventInstance",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("start", models.DateTimeField()),
                ("end", models.DateTimeField()),
                ("event", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="schedule.event")),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="schedule.eventinstance"
                    ),
                ),
                ("venue", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="schedule.venue")),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name_plural": "categories",
            },
        ),
        migrations.AddField(
            model_name="event",
            name="categories",
            field=models.ManyToManyField(blank=True, to="schedule.category"),
        ),
        migrations.AlterField(
            model_name="event",
            name="participants",
            field=models.ManyToManyField(blank=True, related_name="events_participating", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name="event",
            name="admins",
            field=models.ManyToManyField(blank=True, related_name="events_admin", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="event",
            name="estimated_duration",
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="submission_id",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="preferred_occurrences",
            field=models.IntegerField(default=1),
        ),
    ]
