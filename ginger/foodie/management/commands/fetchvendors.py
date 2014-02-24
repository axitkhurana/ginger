from django.core.management.base import BaseCommand

import requests
from bs4 import BeautifulSoup

from ginger.foodie.models import Vendor


class Command(BaseCommand):
    help = "pulls new vendors from OffTheGrid site"

    def handle(self, *args, **kwargs):
        self.stdout.write('Sending request to OffTheGridSF..')
        r = requests.get('http://offthegridsf.com/vendors')

        self.stdout.write('Fetching vendors:')

        for vendor in self._vendors(r.text):
            obj, created = Vendor.objects.get_or_create(name=vendor['name'],
                                                        defaults=vendor)
            if created:
                self.stdout.write('New vendor added: %s' % obj.name)
            else:
                # TODO Update vendors here
                self.stdout.write('Vendor updated: %s' % obj.name)

    def _vendors(self, html):
        """Yields vendor information dict from HTML text"""
        html = BeautifulSoup(html).find_all(class_='otg-vendor-type')

        # vendors categorized by type
        for vendors_by_type in html:
            vendor_type = vendors_by_type.find('div',
                                               class_='otg-vendor-type-name'
                                               ).text
            self.stdout.write('Checking vendor type: %s' % vendor_type)

            # all vendors of one category
            vendors = vendors_by_type.find_all('tr',
                                               class_='otg-vendor')

            for vendor in vendors:
                name_node = vendor.find('a', class_='otg-vendor-name-link')
                vendor_details = {
                    'name': name_node.text,
                    'link': name_node.get('href', ''),
                    'description': vendor.find('div',
                                               class_='otg-vendor-cuisines'
                                               ).text.strip(),
                    'photo_url': vendor.find('img',
                                             class_='otg-vendor-logo'
                                             ).get('src', ''),
                    'type': vendor_type
                }
                yield vendor_details
