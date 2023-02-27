from rest_framework import serializers
from .models import Itinerary, Agenda

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('id', 'place', 'date', 'arrival_time', 'leave_time')

class ItinerarySerializer(serializers.ModelSerializer):
    plan = AgendaSerializer(many=True)

    class Meta:
        model = Itinerary
        fields = ('id', 'owner', 'destination', 'plan')

    def create(self, validated_data):
        plan_data = validated_data.pop('plan')
        itinerary = Itinerary.objects.create(**validated_data)
        for plan in plan_data:
            Agenda.objects.create(itinerary=itinerary, **plan)
        return itinerary

    def update(self, instance, validated_data):
        plan_data = validated_data.pop('plan')
        itinerary = super().update(instance, validated_data)

        # retrieve and update existing plan items
        plan = (Agenda.objects.filter(itinerary=itinerary).all())
        plan_data_mapping = {plan_item['id']: plan_item for plan_item in plan_data}
        for item in plan:
            if item.id in plan_data_mapping:
                item.place = plan_data_mapping[item.id].get('place', item.place)
                item.date = plan_data_mapping[item.id].get('date', item.date)
                item.arrival_time = plan_data_mapping[item.id].get('arrival_time', item.arrival_time)
                item.leave_time = plan_data_mapping[item.id].get('leave_time', item.leave_time)
                item.save()
            else:
                item.delete()
        
        # create new plan items
        for plan_item in plan_data:
            if 'id' not in plan_item:
                Agenda.objects.create(itinerary=itinerary, **plan_item)
        
        return itinerary