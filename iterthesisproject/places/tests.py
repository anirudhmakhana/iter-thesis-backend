from django.test import TestCase
from datetime import time
from django.db.utils import IntegrityError
from pytest_cases import parametrize_with_cases
import pytest
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

class RestaurantTestCase(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            id='P06001510',
            place_name='Ban Thanyaphuet',
            latitude=13.661932,
            longitude=100.470739,
            introduction='',
            detail='',
            destination='BANGKOK',
            category_code='REST',
            category_description='Restaurant',
            hit_score='High',
            cuisine_types=['Thai', 'Chinese'],
        )

        self.opening_hour1 = OpeningHour.objects.create(
            day='Monday',
            opening_time='09:00',
            closing_time='18:00'
        )

        self.opening_hour2 = OpeningHour.objects.create(
            day='Tuesday',
            opening_time='10:00',
            closing_time='19:00'
        )


    def test_restaurant_creation(self):
        self.assertEqual(self.restaurant.id, 'P06001510')
        self.assertEqual(self.restaurant.place_name, 'Ban Thanyaphuet')
        self.assertEqual(self.restaurant.latitude, 13.661932)
        self.assertEqual(self.restaurant.longitude, 100.470739)
        self.assertEqual(self.restaurant.introduction, '')
        self.assertEqual(self.restaurant.detail, '')
        self.assertEqual(self.restaurant.destination, 'BANGKOK')
        self.assertEqual(self.restaurant.category_code, 'REST')
        self.assertEqual(self.restaurant.category_description, 'Restaurant')
        self.assertEqual(self.restaurant.hit_score, 'High')
        self.assertListEqual(self.restaurant.cuisine_types, ['Thai', 'Chinese'])

class AccommodationTestCase(TestCase):
    def setUp(self):
        self.accommodation = Accommodation.objects.create(
            id='A123456',
            place_name='Hotel A',
            latitude=123.456,
            longitude=789.012,
            hit_score='100',
            hotel_star='5',
            number_of_rooms=100,
            price_range='$$$',
        )

    def test_accommodation_creation(self):
        self.assertEqual(self.accommodation.id, 'A123456')
        self.assertEqual(self.accommodation.place_name, 'Hotel A')
        self.assertEqual(self.accommodation.latitude, 123.456)
        self.assertEqual(self.accommodation.longitude, 789.012)
        self.assertEqual(self.accommodation.hit_score, '100')
        self.assertEqual(self.accommodation.hotel_star, '5')
        self.assertEqual(self.accommodation.number_of_rooms, 100)
        self.assertEqual(self.accommodation.price_range, '$$$')
        self.assertListEqual(self.accommodation.awards, [])
        self.assertListEqual(self.accommodation.accomodation_types, [])
        self.assertListEqual(self.accommodation.accomodation_rooms, [])

class ShopTestCase(TestCase):
    def setUp(self):
        self.shop = Shop.objects.create(
            id='S123456',
            place_name='Shop A',
            latitude=123.456,
            longitude=789.012,
            standard='Premium',
            shop_type=['Clothing', 'Accessories'],
        )

    def test_shop_creation(self):
        self.assertEqual(self.shop.id, 'S123456')
        self.assertEqual(self.shop.place_name, 'Shop A')
        self.assertEqual(self.shop.latitude, 123.456)
        self.assertEqual(self.shop.longitude, 789.012)
        self.assertEqual(self.shop.standard, 'Premium')
        self.assertListEqual(self.shop.shop_type, ['Clothing', 'Accessories'])
        self.assertQuerysetEqual(self.shop.opening_hours.all(), [])

class AttractionTestCase(TestCase):
    def setUp(self):
        self.fee = Fee.objects.create(
            thai_child=50.0,
            thai_adult=100.0,
            foreigner_child=200.0,
            foreigner_adult=400.0
        )
        self.attraction = Attraction.objects.create(
            id='A789012',
            place_name='Attraction A',
            latitude=345.678,
            longitude=901.234,
            hit_score='95',
            attraction_types=['Park', 'Museum'],
            tags=['Nature', 'History'],
            targets=['Families', 'Students'],
            activities=['Guided Tours', 'Interactive Exhibits'],
            fee=self.fee
        )

    def test_attraction_creation(self):
        self.assertEqual(self.attraction.id, 'A789012')
        self.assertEqual(self.attraction.place_name, 'Attraction A')
        self.assertEqual(self.attraction.latitude, 345.678)
        self.assertEqual(self.attraction.longitude, 901.234)
        self.assertEqual(self.attraction.hit_score, '95')
        self.assertListEqual(self.attraction.attraction_types, ['Park', 'Museum'])
        self.assertListEqual(self.attraction.tags, ['Nature', 'History'])
        self.assertListEqual(self.attraction.targets, ['Families', 'Students'])
        self.assertListEqual(self.attraction.activities, ['Guided Tours', 'Interactive Exhibits'])
        self.assertEqual(self.attraction.fee, self.fee)
        self.assertQuerysetEqual(self.attraction.opening_hours.all(), [])

    def test_attraction_creation_without_fee(self):
        with self.assertRaises(IntegrityError):
            Attraction.objects.create(
                id='A789012',
                place_name='Attraction A',
                latitude=345.678,
                longitude=901.234,
                hit_score='95',
                attraction_types=['Park', 'Museum'],
                tags=['Nature', 'History'],
                targets=['Families', 'Students'],
                activities=['Guided Tours', 'Interactive Exhibits'],
            )

# Test cases for different models
@pytest.fixture
def place_data():
    return {
        'id': 'P123',
        'place_name': 'Test Place',
        'latitude': 0.0,
        'longitude': 0.0,
    }

@pytest.fixture
def accommodation_data(place_data):
    data = place_data.copy()
    data.update({
        'hotel_star': '5',
        'number_of_rooms': 10,
    })
    return data

@pytest.fixture
def restaurant_data(place_data):
    data = place_data.copy()
    data.update({
        'standard': 'High',
        'cuisine_types': ['Italian', 'French'],
    })
    return data

@pytest.fixture
def shop_data(place_data):
    data = place_data.copy()
    data.update({
        'standard': 'Premium',
        'shop_type': ['Clothing', 'Accessories'],
    })
    return data

@pytest.fixture
def attraction_data(place_data):
    data = place_data.copy()
    data.update({
        'hit_score': 'Excellent',
        'attraction_types': ['Park', 'Museum'],
        'tags': ['Nature', 'History'],
    })
    return data

# Test cases
@pytest.mark.parametrize('place_data', [
    pytest.param(place_data, id='Place'),
    pytest.param(accommodation_data, id='Accommodation'),
    pytest.param(restaurant_data, id='Restaurant'),
    pytest.param(shop_data, id='Shop'),
    pytest.param(attraction_data, id='Attraction'),
])
def test_create_place(place_data):
    place = Place.objects.create(**place_data)
    assert place.id == place_data['id']
    assert place.place_name == place_data['place_name']

# Run the tests
@pytest.mark.parametrize('place_data', [
    pytest.param(place_data, id='Place'),
    pytest.param(accommodation_data, id='Accommodation'),
    pytest.param(restaurant_data, id='Restaurant'),
    pytest.param(shop_data, id='Shop'),
    pytest.param(attraction_data, id='Attraction'),
])
def test_places(place_data):
    test_create_place(place_data)