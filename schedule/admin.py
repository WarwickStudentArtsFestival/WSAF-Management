from django.contrib import admin

# Register your models here.
from .models import Event, EventInstance, Venue, Organisation, Category

class EventInstanceInline(admin.TabularInline):
    model = EventInstance
    extra = 1


# in table of events, show str, prefered_occurrences, and a count of event instances

class EventAdmin(admin.ModelAdmin):
    inlines = [EventInstanceInline]

    list_display = ('__str__', 'preferred_occurrences')



admin.site.register(Organisation)
admin.site.register(Venue)
admin.site.register(Event, EventAdmin)
admin.site.register(EventInstance)
admin.site.register(Category)
