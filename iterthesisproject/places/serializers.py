from rest_framework import serializers
from .models import Location, SHA, Contact, OpeningHour, Fee, Room, Place, Accommodation, Restaurant, Shop, Attraction

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['address', 'sub_district', 'district', 'province', 'postcode']

class SHASerializer(serializers.ModelSerializer):
    class Meta:
        model = SHA
        fields = ['sha_name', 'sha_type_code', 'sha_type_description', 'sha_cate_id', 'sha_cate_description']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['mobile_number', 'phone_number', 'fax_number', 'emails', 'urls']

class OpeningHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = ['day', 'opening_time', 'closing_time']

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = ['thai_child', 'thai_adult', 'foreigner_child', 'foreigner_adult']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_type', 'bd_type']

class PlaceSerializer(serializers.ModelSerializer):
    sha = SHASerializer()
    location = LocationSerializer()
    contact = ContactSerializer()
    class Meta:
        model = Place
        fields = ['place_name', 'latitude', 'longitude', 'sha', 'location', 'contact', 'introduction', 'detail', 'destination', 'category_code']

class AccommodationSerializer(PlaceSerializer):
    class Meta:
        model = Accommodation
        fields = PlaceSerializer.Meta.fields + ['hotel_star', 'register_license_id', 'display_checkin_time', 'display_checkout_time', 'number_of_rooms', 'price_range', 'standard', 'awards', 'hit_score', 'accomodation_types', 'accomodation_rooms']

class RestaurantSerializer(PlaceSerializer):
    opening_hours = OpeningHourSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = PlaceSerializer.Meta.fields + ['standard', 'awards', 'hit_score', 'restaurant_types', 'cuisine_types', 'michelines', 'tags', 'opening_hours']

class ShopSerializer(PlaceSerializer):
    opening_hours = OpeningHourSerializer(many=True)
    class Meta:
        model = Shop
        fields = PlaceSerializer.Meta.fields + ['standard', 'shop_type', 'opening_hours']