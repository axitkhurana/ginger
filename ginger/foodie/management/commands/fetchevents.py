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
        try:
            latest_event = Event.objects.latest('start_time')
            last_update = latest_event.start_time
        except Event.DoesNotExist:
            last_update = timezone.make_aware(datetime.min,
                                              timezone.get_default_timezone())

        self.stdout.write('Pulling events from OffTheGrid facebook page')
        fbconsole.ACCESS_TOKEN = '{}|{}'.format(FB_APP_ID, FB_APP_SECRET)
        events = fbconsole.get('/OffTheGridSF/events')['data']

        latest_events = (e for e in events if
                         parse(e['start_time']) > last_update)

        for fb_event in latest_events:
            details = fbconsole.get('/{}'.format(fb_event['id']))
            event = Event(name=details['name'],
                          location=details['location'].strip(),
                          start_time=parse(details['start_time']),
                          end_time=parse(details['end_time']),
                          )
            event.save()

            vendors = self._get_vendors(details['description'])
            if vendors:
                event.vendors.add(*vendors)

            self.stdout.write('New event added! {}'.format(event.name))

    def _get_vendors(self, description):
        """Returns a generator of vendor objects from event description
        or None in case of failure"""

        # TODO Fix for other cases and consider using re.search
        start_string = 'Vendors:\r\n'

        start = description.find(start_string)
        end = description.find('\r\n\r\n', start)

        if start == -1 or end == -1:
            return None

        vendor_names_text = description[start:end].lstrip(start_string)
        vendors = [Vendor.objects.get_or_create(name=name)[0] for name in
                   vendor_names_text.split('\r\n') if name.strip()]
        return vendors
