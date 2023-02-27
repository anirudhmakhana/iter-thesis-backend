from django.db import models
from account.models import User
from places.models import Place

# Create your models here.
class Agenda(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='agenda_place')
    date = models.DateField()
    arrival_time = models.TimeField()
    leave_time = models.TimeField()

class Itinerary(models.Model):
    destination = models.CharField(max_length=100, default='', null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='itineraries_owned')
    co_travelers = models.ManyToManyField(User, related_name='itineraries_joined',  blank=True)
    plan = models.ManyToManyField(Agenda)
