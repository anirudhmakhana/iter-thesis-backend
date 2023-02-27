from rest_framework import serializers
from .models import Place, Accommodation, Shop, Attraction, Restaurant, Contact, Location, SHA, OpeningHour, Fee

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class SHASerializer(serializers.ModelSerializer):
    class Meta:
        model = SHA
        fields = '__all__'

class OpeningHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = '__all__'

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'

class AccommodationSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    sha = SHASerializer()
    contact = ContactSerializer()

    class Meta:
        model = Accommodation
        fields = '__all__'

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        sha_data = validated_data.pop('sha')
        contact_data = validated_data.pop('contact')

        location_serializer = LocationSerializer(data=location_data)
        sha_serializer = SHASerializer(data=sha_data)
        contact_serializer = ContactSerializer(data=contact_data)

        if location_serializer.is_valid() and sha_serializer.is_valid() and contact_serializer.is_valid():
            location = location_serializer.save()
            sha = sha_serializer.save()
            contact = contact_serializer.save()
            accommodation = Accommodation.objects.create(location=location, sha=sha, contact=contact, **validated_data)
            return accommodation

        # Raise validation error if any serializer fails
        errors = {
            'location': location_serializer.errors,
            'sha': sha_serializer.errors,
            'contact': contact_serializer.errors
        }
        raise serializers.ValidationError(errors)
    
class ShopSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    sha = SHASerializer()
    contact = ContactSerializer()

    class Meta:
        model = Shop
        fields = '__all__'

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        sha_data = validated_data.pop('sha')
        contact_data = validated_data.pop('contact')

        location_serializer = LocationSerializer(data=location_data)
        sha_serializer = SHASerializer(data=sha_data)
        contact_serializer = ContactSerializer(data=contact_data)

        if location_serializer.is_valid() and sha_serializer.is_valid() and contact_serializer.is_valid():
            location = location_serializer.save()
            sha = sha_serializer.save()
            contact = contact_serializer.save()
            shop = Shop.objects.create(location=location, sha=sha, contact=contact, **validated_data)
            return shop

        # Raise validation error if any serializer fails
        errors = {
            'location': location_serializer.errors,
            'sha': sha_serializer.errors,
            'contact': contact_serializer.errors
        }
        raise serializers.ValidationError(errors)

class AttractionSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    sha = SHASerializer()
    contact = ContactSerializer()
    opening_hours = OpeningHourSerializer(many=True)
    fee = FeeSerializer()

    class Meta:
        model = Attraction
        fields = '__all__'

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        sha_data = validated_data.pop('sha')
        contact_data = validated_data.pop('contact')
        opening_hours_data = validated_data.pop('opening_hours')
        fee_data = validated_data.pop('fee')

        location_serializer = LocationSerializer(data=location_data)
        sha_serializer = SHASerializer(data=sha_data)
        contact_serializer = ContactSerializer(data=contact_data)
        opening_hours_serializer = OpeningHourSerializer(data=opening_hours_data, many=True)
        fee_serializer = FeeSerializer(data=fee_data)

        if location_serializer.is_valid() and sha_serializer.is_valid() and contact_serializer.is_valid() and opening_hours_serializer.is_valid() and fee_serializer.is_valid():
            location = location_serializer.save()
            sha = sha_serializer.save()
            contact = contact_serializer.save()
            opening_hours = opening_hours_serializer.save()
            fee = fee_serializer.save()

            attraction = Attraction.objects.create(location=location, sha=sha, contact=contact, fee=fee, **validated_data)
            attraction.opening_hours.set(opening_hours)
            return attraction

        # Raise validation error if any serializer fails
        errors = {
            'location': location_serializer.errors,
            'sha': sha_serializer.errors,
            'contact': contact_serializer.errors,
            'opening_hours': opening_hours_serializer.errors,
            'fee': fee_serializer.errors
        }
        raise serializers.ValidationError(errors)

class RestaurantSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    sha = SHASerializer()
    contact = ContactSerializer()
    opening_hours = OpeningHourSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = '__all__'

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        sha_data = validated_data.pop('sha')
        contact_data = validated_data.pop('contact')
        opening_hours_data = validated_data.pop('opening_hours')

        location_serializer = LocationSerializer(data=location_data)
        sha_serializer = SHASerializer(data=sha_data)
        contact_serializer = ContactSerializer(data=contact_data)
        opening_hours_serializer = OpeningHourSerializer(data=opening_hours_data, many=True)

        if location_serializer.is_valid() and sha_serializer.is_valid() and contact_serializer.is_valid() and opening_hours_serializer.is_valid():
            location = location_serializer.save()
            sha = sha_serializer.save()
            contact = contact_serializer.save()
            opening_hours = opening_hours_serializer.save()

            restaurant = Restaurant.objects.create(location=location, sha=sha, contact=contact, **validated_data)
            restaurant.opening_hours.set(opening_hours)
            return restaurant

        # Raise validation error if any serializer fails
        errors = {
            'location': location_serializer.errors,
            'sha': sha_serializer.errors,
            'contact': contact_serializer.errors,
            'opening_hours': opening_hours_serializer.errors
        }
        raise serializers.ValidationError(errors)

class PlaceSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    sha = SHASerializer()
    contact = ContactSerializer()

    class Meta:
        model = Place
        fields = '__all__'

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        sha_data = validated_data.pop('sha')
        contact_data = validated_data.pop('contact')

        location_serializer = LocationSerializer(data=location_data)
        sha_serializer = SHASerializer(data=sha_data)
        contact_serializer = ContactSerializer(data=contact_data)

        if location_serializer.is_valid() and sha_serializer.is_valid() and contact_serializer.is_valid():
            location = location_serializer.save()
            sha = sha_serializer.save()
            contact = contact_serializer.save()
            place = Place.objects.create(location=location, sha=sha, contact=contact, **validated_data)
            return place

        # Raise validation error if any serializer fails
        errors = {
            'location': location_serializer.errors,
            'sha': sha_serializer.errors,
            'contact': contact_serializer.errors
        }
        raise serializers.ValidationError(errors)