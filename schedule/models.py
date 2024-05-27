from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe

class Organisation(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50, unique=True, null=True)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """Return the name of the organisation."""
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=50, unique=True, null=True)
    submission_id = models.IntegerField(null=True, blank=True)

    organisation = models.ForeignKey("Organisation", on_delete=models.CASCADE, null=True, blank=True)

    primary_category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, related_name="primary_category")
    categories = models.ManyToManyField("Category", blank=True)
    public_description = models.TextField(null=True, blank=True)
    advertisement_weight = models.IntegerField(default=1)

    estimated_duration = models.DurationField(null=True, blank=True)
    preferred_occurrences = models.IntegerField(default=1)

    admins = models.ManyToManyField("accounts.User", related_name="events_admin", blank=True)
    participants = models.ManyToManyField("accounts.User", related_name="events_participating", blank=True)

    tech_notes = models.TextField(null=True, blank=True)
    org_notes = models.TextField(null=True, blank=True)

    published = models.BooleanField(default=False)
    digital_signage = models.BooleanField(default=False)

    data_collected = models.BooleanField(default=False)

    def __str__(self):
        """Return the key info about the event (name, title, organisation)."""
        name_string = ""
        if self.submission_id is not None:
            name_string += f"{self.submission_id} - "
        name_string += self.title
        if self.organisation is not None:
            name_string += f" ({self.organisation})"

        return name_string


class EventInstance(models.Model):
    class Meta:
        verbose_name = "Schedule Item"
        verbose_name_plural = "Schedule Items"

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    venue = models.ForeignKey("Venue", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        """Return the key info about the event occurance (event, venue, start, end)."""
        start_time = timezone.localtime(self.start).strftime("%A %H:%M")
        end_time = timezone.localtime(self.end).strftime("%H:%M")
        return f"{self.event} at {self.venue} from {start_time} to {end_time}"

    def get_json(self):
        """Return the event instance as a json object."""
        json_dict = {
            "organiser": self.event.organisation.name if self.event.organisation is not None else None,
            "title": self.event.title,
            "description": self.event.public_description,
            "categories": [category.name for category in self.event.additional_categories.all()],
            "start": self.start,
            "end": self.end,
            "venue": self.venue.name,
        }

        children = EventInstance.objects.filter(parent=self).all()
        children_json = [child.get_json() for child in children]
        if len(children_json) > 0:
            json_dict["sub-events"] = children_json

        return json_dict


class Venue(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50, unique=True, null=True)
    campus_map_url = models.CharField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/venues/', blank=True, null=True)

    def __str__(self):
        """Return the name of the venue."""
        return self.name

    def image_preview(self):
        return mark_safe('<img src="{}" style="max-width:50px; max-height:50px"/>'.format(self.image.url))


class Category(models.Model):
    class CategoryIcon(models.TextChoices):
        MASK = "MASK"
        TRUMPET = "TRUMPET"
        BALLET_SHOES = "BALLET_SHOES"
        MICROPHONE = "MICROPHONE"
        PAINTBRUSH = "PAINTBRUSH"

    class CategoryColourThemes(models.TextChoices):
        YELLOW = "YELLOW"
        ORANGE = "ORANGE"
        PINK = "PINK"
        PURPLE = "PURPLE"

    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=32, choices=CategoryIcon.choices, default=CategoryIcon.MASK)
    colour_theme = models.CharField(max_length=32, choices=CategoryColourThemes.choices, default=CategoryColourThemes.PURPLE)

    # define plural for django admin
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        """Return the name of the category."""
        return self.name
