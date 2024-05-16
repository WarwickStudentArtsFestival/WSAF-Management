from django.db import models

class Organisation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    organisation = models.ForeignKey('Organisation', on_delete=models.CASCADE, null=True, blank=True)
    submission_id = models.IntegerField(null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    estimated_duration = models.DurationField(null=True, blank=True)
    preferred_occurrences = models.IntegerField(default=1)
    admins = models.ManyToManyField('accounts.User', related_name='events_admin', blank=True)
    participants = models.ManyToManyField('accounts.User', related_name='events_participating', blank=True)
    categories = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        if self.organisation is None:
            return f'{self.submission_id} - {self.title}'

        return f'{self.submission_id} - {self.title} ({self.organisation})'

class EventInstance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.event} at {self.venue} from {self.start} to {self.end}'

class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    # define plural for django admin
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name