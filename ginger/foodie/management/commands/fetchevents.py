from django.utils import timezone
from django.core.management.base import BaseCommand

from ginger.foodie.models import Event, Vendor
from ginger.settings import FB_APP_ID, FB_APP_SECRET

import fbconsole
from datetime import datetime
from dateutil.parser import parse


class Command(BaseCommand):
    help = "pulls new events from OffTheGrid's Facebook events page"

    def handle(self, *args, **kwargs):
        for fb_event in self._events():
            details = fbconsole.get('/{}'.format(fb_event['id']))
            event = Event(name=details['name'],
                          location=details['location'].strip(),
                          start_time=parse(details['start_time']),
                          end_time=parse(details['end_time']),
                          )
            event.save()

            event_description = details['description'].lower()
            vendors = [vendor for vendor in Vendor.objects.all()
                       if vendor.name.lower() in event_description]
            if vendors:
                event.vendors.add(*vendors)

            self.stdout.write('New event added! {} with vendors {}'.format(event.name, vendors))

    def _events(self):
        """Yields events after last saved event from OffTheGrid's FB page"""
        try:
            latest_event = Event.objects.latest('start_time')
            last_update = latest_event.start_time
        except Event.DoesNotExist:
            last_update = timezone.make_aware(datetime.min,
                                              timezone.get_default_timezone())

        self.stdout.write('Pulling events from OffTheGrid facebook page')
        fbconsole.ACCESS_TOKEN = '{}|{}'.format(FB_APP_ID, FB_APP_SECRET)
        events = fbconsole.get('/OffTheGridSF/events')['data']

        for event in events:
            if parse(event['start_time']) > last_update:
                yield event
