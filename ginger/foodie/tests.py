from django.test import TestCase


class FoodieViewsTestCase(TestCase):
    fixtures = ['foodie_views_testdata.json']

    def test_vendors(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

        # Vendor with the highest frequency
        vendor_1, frequency_1 = resp.context['vendor_frequency'][0]
        self.assertEqual(vendor_1.name, 'Sanguchon')
        self.assertEqual(frequency_1, 9)
