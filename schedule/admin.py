from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .models import Category, Event, EventInstance, Organisation, Venue


class EventInstanceInline(admin.TabularInline):
    model = EventInstance
    extra = 1


class ChildEventInstanceInline(admin.TabularInline):
    model = EventInstance
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = [EventInstanceInline]

    list_display = ("__str__", "preferred_occurrences", "assigned_instances")

    def assigned_instances(self, obj):
        return obj.eventinstance_set.count()


class SatMonWeekDayListFilter(admin.SimpleListFilter):
    title = _("day")

    parameter_name = "weekday"

    days = [
        ("sat", _("Saturday")),
        ("sun", _("Sunday")),
        ("mon", _("Monday")),
    ]

    def lookups(self, request, model_admin):
        return self.days

    def queryset(self, request, queryset):
        if self.value() is None:
            return

        if self.value() == "sat":
            day_index = 7
        elif self.value() == "sun":
            day_index = 1
        elif self.value() == "mon":
            day_index = 2

        return queryset.filter(start__week_day=day_index)


class EventTypeListFilter(admin.SimpleListFilter):
    title = _("event type")

    parameter_name = "event_type"

    event_types = [
        ("sub", _("Child Event")),
        ("full", _("Full Event")),
    ]

    def lookups(self, request, model_admin):
        return self.event_types

    def queryset(self, request, queryset):
        if self.value() is None:
            return

        if self.value() == "sub":
            return queryset.filter(parent__isnull=False)
        elif self.value() == "full":
            return queryset.filter(parent__isnull=True)


class EventInstanceAdmin(admin.ModelAdmin):
    inlines = [ChildEventInstanceInline]

    list_filter = ["venue", "event__categories", SatMonWeekDayListFilter, EventTypeListFilter, "published"]

    list_display = ("event", "venue", "wsaf_time_start", "wsaf_time_end", "venue", "parent")

    ordering = ("start",)

    def truncated_event_name(self, obj):
        return str(obj)[:80]

    truncated_event_name.admin_order_field = "event"
    truncated_event_name.short_description = "Event"

    def wsaf_time_start(self, obj):
        return timezone.localtime(obj.start).strftime("%a %H:%M")

    wsaf_time_start.admin_order_field = "start"
    wsaf_time_start.short_description = "Event Start"

    def wsaf_time_end(self, obj):
        return timezone.localtime(obj.end).strftime("%a %H:%M")

    wsaf_time_end.admin_order_field = "end"
    wsaf_time_end.short_description = "Event End"


admin.site.register(Organisation)
admin.site.register(Venue)
admin.site.register(Event, EventAdmin)
admin.site.register(EventInstance, EventInstanceAdmin)
admin.site.register(Category)
