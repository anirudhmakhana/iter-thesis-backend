from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Itinerary, Agenda, UserPreference
from places.serializers import Place, PlaceSerializer, Accommodation,AccommodationSerializer, Restaurant ,RestaurantSerializer,Shop ,ShopSerializer, AttractionSerializer, Attraction
from account.models import User
from collections import OrderedDict

from rest_framework import serializers
from .models import Itinerary, Agenda

import requests

'''
"Invalid pk \"Place object (P4358920)\" - object does not exist."
'''
class AgendaSerializer(serializers.ModelSerializer):
    place_id = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all())
    # place_id = serializers.StringRelatedField()
    # place_id = serializers.UUIDField()
    # place_id = serializers.CharField(source='place.place_id')
    place_id = serializers.CharField()

    class Meta:
        model = Agenda
        fields = ['id', 'place_id', 'date', 'arrival_time', 'leave_time', 'travel_time']
    
    def create(self, validated_data):
        print(validated_data.keys())
        place_id = validated_data.pop('place_id')
        place = Place.objects.get(id=place_id)
        print(place)
        place_id_value = place.id  # store the id in a new variable
        print(f"THE FUCKING PLACE ID VALUE IS {place_id_value}")
        agenda = Agenda.objects.create(place_id=place_id_value, **validated_data)
        print(agenda)
        return agenda
    
    # def create(self, validated_data):
    #     place_id = validated_data.pop('place_id')
    #     print(place_id)
    #     place_id_value = place_id.id  # store the id in a new variable
    #     agenda = Agenda.objects.create(place_id=place_id_value, **validated_data)
    #     return agenda


class ItinerarySerializer(serializers.ModelSerializer):
    plan = AgendaSerializer(many=True)

    class Meta:
        model = Itinerary
        fields = ['id', 'destination', 'owner', 'co_travelers', 'plan', 'start_date', 'end_date', 'start_time', 'end_time']

    def create(self, validated_data):
        print(validated_data.keys())
        agendas_data = validated_data.pop('plan')
        co_travelers_data = validated_data.pop('co_travelers')
        itinerary = Itinerary.objects.create(**validated_data)

        for agenda_data in agendas_data:
            agenda_serializer = AgendaSerializer(data=agenda_data)
            print(agenda_serializer)
            agenda_serializer.is_valid(raise_exception=True)
            agenda_serializer.save()

            itinerary.plan.add(agenda_serializer.instance)

        for traveler in co_travelers_data:
            itinerary.co_travelers.add(traveler)

        return itinerary
    
class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreference
        fields = ['destination', 'start_date', 'end_date', 'start_time', 'end_time', 'budget', 'tripType', 'targetTypes', 'preferredActivities', 'preferredCuisine', 'owner', 'co_travelers']