from django.template import RequestContext
from django.shortcuts import render_to_response

from collections import defaultdict
from datetime import datetime, timedelta

from ginger.foodie.models import Event


def vendors(request):
    last_month = datetime.today() - timedelta(days=30)

    events = Event.objects.filter(start_time__gt=last_month)
    events = events.prefetch_related('vendors')

    vendors = defaultdict(int)
    for event in events:
        for vendor in event.vendors.all():
            vendors[vendor] += 1

    # XXX Consider uglier faster alternative:
    # Vendor.objects.extra(
    #         select = {"event_count": "SELECT COUNT(*) FROM event WHERE
    #                    foodie_vendor.id=foodie_event.vendor AND
    #                    food_event.start_time > ?"},
    #         select_params = [last_month.strftime('%Y-%m-%d %H:%M:%S')]
    #                 ).order_by('-event_count')

    vendor_frequency = [(vendor, vendors[vendor]) for vendor in
                        sorted(vendors, key=vendors.get, reverse=True)]

    return render_to_response('vendors.html', {'vendor_frequency':
                              vendor_frequency},
                              context_instance=RequestContext(request))
