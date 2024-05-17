from django.db import models
from django.utils import timezone


class Organisation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """Return the name of the organisation."""
        return self.name


class Event(models.Model):
    organisation = models.ForeignKey("Organisation", on_delete=models.CASCADE, null=True, blank=True)
    submission_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    estimated_duration = models.DurationField(null=True, blank=True)
    preferred_occurrences = models.IntegerField(default=1)
    admins = models.ManyToManyField("accounts.User", related_name="events_admin", blank=True)
    participants = models.ManyToManyField("accounts.User", related_name="events_participating", blank=True)
    categories = models.ManyToManyField("Category", blank=True)

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
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    venue = models.ForeignKey("Venue", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Return the key info about the event occurance (event, venue, start, end)."""
        start_time = timezone.localtime(self.start).strftime("%A %H:%M")
        end_time = timezone.localtime(self.end).strftime("%H:%M")
        return f"{self.event} at {self.venue} from {start_time} to {end_time}"


class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        """Return the name of the venue."""
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    # define plural for django admin
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        """Return the name of the category."""
        return self.name
