from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Itinerary, Agenda
from places.serializers import Place, PlaceSerializer, Accommodation,AccommodationSerializer, Restaurant ,RestaurantSerializer,Shop ,ShopSerializer, AttractionSerializer, Attraction
from account.models import User
from collections import OrderedDict

from rest_framework import serializers
from .models import Itinerary, Agenda

import requests

# class AgendaSerializer(serializers.ModelSerializer):
#     place = serializers.PrimaryKeyRelatedField(many=True, queryset=Place.objects.all())

#     class Meta:
#         model = Agenda
#         fields = '__all__'
    
#     def to_representation(self, instance):
#         ret = super().to_representation(instance)
#         place_data = ret.pop('place')
#         ret['place'] = PlaceSerializer(place_data).data
#         return ret
    
#     def create(self, validated_data):
#         place_data = validated_data.pop('place')
#         place = Place.objects.get(id=place_data)
#         agenda = Agenda.objects.create(place=place, **validated_data)
#         return agenda
    
# class ItinerarySerializer(serializers.ModelSerializer):
#     plan = AgendaSerializer(many=True)
#     co_travelers = serializers.ListField(child=serializers.IntegerField())

#     class Meta:
#         model = Itinerary
#         fields = '__all__'

#     # def create(self, validated_data):
#     #     plan_data = validated_data.pop('plan')
#     #     itinerary = Itinerary.objects.create(**validated_data)
#     #     for plan in plan_data:
#     #         Agenda.objects.create(itinerary=itinerary, **plan)
#     #     itinerary.plan.set(Agenda.objects.filter(itinerary=itinerary))
#     #     return itinerary
#     # def to_representation(self, instance):
#     #     ret = super().to_representation(instance)
#     #     plan_data = ret.pop('plan')
#     #     plan = []
#     #     for agenda_data in plan_data:
#     #         agenda = OrderedDict()
#     #         agenda['date'] = agenda_data['date']
#     #         agenda['arrival_time'] = agenda_data['arrival_time']
#     #         agenda['leave_time'] = agenda_data['leave_time']
#     #         agenda['place'] = agenda_data['place'].place_id  # Add place_id to the output
#     #         plan.append(agenda)
#     #     ret['plan'] = plan
#     #     return ret
    
#     def create(self, validated_data):
#         plan_data = validated_data.pop('plan')
#         co_travelers_data = validated_data.pop('co_travelers')
#         itinerary = Itinerary.objects.create(**validated_data)

#         for p_data in plan_data:
#             print(p_data)
#             place_id = p_data.pop('place')
#             place = Place.objects.get(id=place_id)
#             Agenda.objects.create(itinerary=itinerary, place=place, **p_data)

#         for traveler_id in co_travelers_data:
#             try:
#                 traveler = User.objects.get(id=traveler_id)
#                 itinerary.co_travelers.add(traveler)
#             except User.DoesNotExist:
#                 pass

#         return itinerary
    
#     # def create(self, validated_data):
#     #     print(validated_data)
#     #     plan_data = validated_data.pop('plan')
#     #     print(plan_data)
#     #     co_travelers_data = validated_data.pop('co_travelers')
#     #     itinerary = Itinerary.objects.create(**validated_data)
#     #     for p_data in plan_data:
#     #         plan_data = validated_data.pop('plan')  # Retrieve the nested plan data
#     #         itinerary = Itinerary.objects.create(**validated_data)
#     #         # place = Place.objects.get(id=place_id)
#     #         Agenda.objects.create(itinerary=itinerary, **p_data)  # Create each nested plan object and link it to the itinerary object
        
#     #     for traveler_id in co_travelers_data:
#     #         try:
#     #             traveler = User.objects.get(id=traveler_id)
#     #             itinerary.co_travelers.add(traveler)
#     #         except User.DoesNotExist:
#     #             pass

#     #     return itinerary
    
#     # def create(self, validated_data):
#     #     agendas_data = validated_data.pop('plan')
#     #     co_travelers_data = validated_data.pop('co_travelers')
#     #     itinerary = Itinerary.objects.create(**validated_data)

#     #     for agenda_data in agendas_data:
#     #         agenda_serializer = AgendaSerializer(data=agenda_data)
#     #         agenda_serializer.is_valid(raise_exception=True)
#     #         agenda_serializer.save()

#     #         itinerary.plan.add(agenda_serializer.instance)

#     #     for traveler_id in co_travelers_data:
#     #         try:
#     #             traveler = User.objects.get(id=traveler_id)
#     #             itinerary.co_travelers.add(traveler)
#     #         except User.DoesNotExist:
#     #             pass

#     #     return itinerary

#     def update(self, instance, validated_data):
#         plan_data = validated_data.pop('plan')
#         itinerary = super().update(instance, validated_data)

#         # retrieve and update existing plan items
#         plan = (Agenda.objects.filter(itinerary=itinerary).all())
#         plan_data_mapping = {plan_item['id']: plan_item for plan_item in plan_data}
#         for item in plan:
#             if item.id in plan_data_mapping:
#                 item.place = plan_data_mapping[item.id].get('place', item.place)
#                 item.date = plan_data_mapping[item.id].get('date', item.date)
#                 item.arrival_time = plan_data_mapping[item.id].get('arrival_time', item.arrival_time)
#                 item.leave_time = plan_data_mapping[item.id].get('leave_time', item.leave_time)
#                 item.save()
#             else:
#                 item.delete()
        
#         # create new plan items
#         for plan_item in plan_data:
#             if 'id' not in plan_item:
#                 Agenda.objects.create(itinerary=itinerary, **plan_item)

#         itinerary.plan.set(Agenda.objects.filter(itinerary=itinerary))
#         return itinerary


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
        fields = ['id', 'place_id', 'date', 'arrival_time', 'leave_time']
    
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
    
