from django.contrib import admin

from .models import Event, EventInstance, Venue, Organisation, Category

class EventInstanceInline(admin.TabularInline):
    model = EventInstance
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = [EventInstanceInline]

    list_display = ('__str__', 'preferred_occurrences', 'assigned_instances')

    def assigned_instances(self, obj):
        return obj.eventinstance_set.count()

class EventInstanceAdmin(admin.ModelAdmin):
    list_display = ('event', 'venue', 'start', 'end', 'venue', 'parent')

    ordering = ('start',)


admin.site.register(Organisation)
admin.site.register(Venue)
admin.site.register(Event, EventAdmin)
admin.site.register(EventInstance, EventInstanceAdmin)
admin.site.register(Category)
