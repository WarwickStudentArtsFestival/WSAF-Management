import json

from django.contrib.syndication.views import Feed
from django.core.serializers.json import DjangoJSONEncoder

from .models import EventInstance


class AllScheduleDSFeed(Feed):
    title = "WSAF Schedule for Digital Signage"
    description = "All published Warwick Student Arts Festival events in a RSS/JSON feed."
    link = "https://wsaf.org.uk"

    def items(self):
        return EventInstance.objects.filter(parent=None, event__digital_signage=True).order_by("start").all()

    def item_title(self, item: EventInstance):
        return str(item.event.title)

    def item_description(self, item):
        json_str = json.dumps(item.get_json(), cls=DjangoJSONEncoder)
        json_str = json_str.replace(" ", "%20")
        return json_str

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return "https://wsaf.org.uk"
