# Generated by Django 5.0.6 on 2024-05-27 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_category_colour_theme_category_icon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='digital_signage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
