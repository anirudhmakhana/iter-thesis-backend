from django.test import TestCase
from datetime import time
from .models import Location, SHA, Contact, OpeningHour, Fee, Place, Accommodation, Room, Restaurant, Shop, Attraction

class LocationModelTestCase(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            address='123 Main St',
            sub_district='Downtown',
            district='City Center',
            province='State',
            postcode='12345'
        )

    def test_location_fields(self):
        self.assertEqual(self.location.address, '123 Main St')
        self.assertEqual(self.location.sub_district, 'Downtown')
        self.assertEqual(self.location.district, 'City Center')
        self.assertEqual(self.location.province, 'State')
        self.assertEqual(self.location.postcode, '12345')

class SHAModelTestCase(TestCase):
    def setUp(self):
        self.sha = SHA.objects.create(
            sha_name='Test SHA',
            sha_type_code='A',
            sha_type_description='Type A',
            sha_cate_id='1',
            sha_cate_description='Category 1'
        )

    def test_sha_fields(self):
        self.assertEqual(self.sha.sha_name, 'Test SHA')
        self.assertEqual(self.sha.sha_type_code, 'A')
        self.assertEqual(self.sha.sha_type_description, 'Type A')
        self.assertEqual(self.sha.sha_cate_id, '1')
        self.assertEqual(self.sha.sha_cate_description, 'Category 1')

class ContactModelTestCase(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            mobile_number=['555-1234', '555-5678'],
            phone_number=['555-4321'],
            fax_number=['555-8765'],
            emails=['test@example.com', 'info@example.com'],
            urls=['http://www.example.com', 'http://www.test.com']
        )

    def test_contact_fields(self):
        self.assertEqual(self.contact.mobile_number, ['555-1234', '555-5678'])
        self.assertEqual(self.contact.phone_number, ['555-4321'])
        self.assertEqual(self.contact.fax_number, ['555-8765'])
        self.assertEqual(self.contact.emails, ['test@example.com', 'info@example.com'])
        self.assertEqual(self.contact.urls, ['http://www.example.com', 'http://www.test.com'])

# class OpeningHourTestCase(TestCase):
#     def setUp(self):
#         self.opening_hour = OpeningHour.objects.create(
#             day='Monday', 
#             opening_time=time(hour=9, minute=0), 
#             closing_time=time(hour=17, minute=0)
#         )

#     def test_opening_hour_str(self):
#         self.assertEqual(str(self.opening_hour), 'Monday: 09:00 - 17:00')

# class FeeTestCase(TestCase):
#     def setUp(self):
#         self.fee = Fee.objects.create(
#             thai_child=50.0, 
#             thai_adult=100.0, 
#             foreigner_child=500.0, 
#             foreigner_adult=1000.0
#         )

#     def test_fee_str(self):
#         self.assertEqual(str(self.fee), 'THB 50.0 - THB 100.0 / THB 500.0 - THB 1000.0')
class PlaceTestCase(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            address='123 Main St',
            sub_district='Subdistrict',
            district='District',
            province='Province',
            postcode='12345'
        )
        self.sha = SHA.objects.create(
            sha_name='Test SHA',
            sha_type_code='1',
            sha_type_description='Test SHA Type Description',
            sha_cate_id='1',
            sha_cate_description='Test SHA Category Description'
        )
        self.contact = Contact.objects.create(
            mobile_number=['123-456-7890'],
            phone_number=['123-456-7890'],
            fax_number=['123-456-7890'],
            emails=['test@example.com'],
            urls=['http://example.com']
        )
        self.place = Place.objects.create(
            id='1',
            place_name='Test Place',
            latitude=50.0,
            longitude=60.0,
            sha=self.sha,
            location=self.location,
            contact=self.contact,
            introduction='Test Introduction',
            detail='Test Detail',
            destination='Test Destination',
            category_code=['1', '2'],
            category_description='Test Category Description',
            how_to_travels=['Walk'],
            mobile_picture_urls=['http://example.com/mobile'],
            web_picture_urls=['http://example.com/web'],
            payment_methods=['Credit Card'],
            facilities=['WiFi'],
            services=['Room Service']
        )

    def test_place_creation(self):
        self.assertTrue(isinstance(self.place, Place))
        # self.assertEqual(self.place.__str__(), self.place.place_name)
        self.assertEqual(self.place.latitude, 50.0)
        self.assertEqual(self.place.longitude, 60.0)
        self.assertEqual(self.place.sha, self.sha)
        self.assertEqual(self.place.location, self.location)
        self.assertEqual(self.place.contact, self.contact)
        self.assertEqual(self.place.introduction, 'Test Introduction')
        self.assertEqual(self.place.detail, 'Test Detail')
        self.assertEqual(self.place.destination, 'Test Destination')
        self.assertEqual(self.place.category_code, ['1', '2'])
        self.assertEqual(self.place.category_description, 'Test Category Description')
        self.assertEqual(self.place.how_to_travels, ['Walk'])
        self.assertEqual(self.place.mobile_picture_urls, ['http://example.com/mobile'])
        self.assertEqual(self.place.web_picture_urls, ['http://example.com/web'])
        self.assertEqual(self.place.payment_methods, ['Credit Card'])
        self.assertEqual(self.place.facilities, ['WiFi'])
        self.assertEqual(self.place.services, ['Room Service'])