from django.db import models
from account.models import User
from places.models import Place
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.
class Agenda(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='agenda_place')
    date = models.DateField()
    '''
    {other_place: 10, other_placeA: 25, ...}
    '''
    travel_time = JSONField(default=dict)
    arrival_time = models.TimeField()
    leave_time = models.TimeField()

class Itinerary(models.Model):
    destination = models.CharField(max_length=100, default='', null=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='itineraries_owned')
    co_travelers = models.ManyToManyField(User, related_name='itineraries_joined',  blank=True)
    plan = models.ManyToManyField(Agenda)

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="preference_user")
    destination = models.CharField(max_length=100, default='', null=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    budget = ArrayField(models.IntegerField())
    tripType = models.CharField(max_length=100)
    targetTypes = ArrayField(models.CharField(max_length=100))
    preferredActivities = ArrayField(models.CharField(max_length=100))
    preferredCuisine = ArrayField(models.CharField(max_length=100))