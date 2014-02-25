from django.core.management.base import BaseCommand

import hipchat
from datetime import date

from ginger.settings import HIPCHAT_API_TOKEN, HIPCHAT_ROOM_ID
from ginger.foodie.models import Event


class Command(BaseCommand):
    help = "posts today's vendors at 5th and Minnia on HipChat"

    def handle(self, *args, **kwargs):
        today = date.today()
        events = Event.objects.filter(start_time__year=today.year,
                                      start_time__month=today.month,
                                      start_time__day=today.day,
                                      location__icontains='minna')
        # TODO Ask if precise location can be used: 410 Minna St, San Francisco

        hipster = hipchat.HipChat(token=HIPCHAT_API_TOKEN)
        for event in events:
            vendors = [vendor.name for vendor in event.vendors.all()]

            if not vendors:
                vendors = [('Checkout https://facebook.com/events/{}'
                            ' for more information.'.format(event.fb_id))]

            message = '\n'.join([event.name] + vendors)
            hipster.message_room(HIPCHAT_ROOM_ID, 'foodiebot', message)
