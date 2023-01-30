from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
from django.db import models

#Classes used in Place
class Location():
    pass

class SHA():
    pass

class Contact():
    pass

#Class used in Restaurant, Shop, Attraction
#can we come up with a new name for this lol
class OpeningHour():
    pass

class Place(models.Model):
    place_name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    #sha = models.ForeignKey(Sha, on_delete=models.CASCADE)
    #location = models.ForeignKey(Location, on_delete=models.CASCADE)
    #contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    introduction = models.CharField(max_length=255)
    detail = models.TextField()
    destination = models.CharField(max_length=255)
    #category_code = ArrayField(models.CharField(max_length=10), blank=True)

    def __str__(self):
        return self.name

class Accommodation(Place):
    hotel_star = models.CharField(max_length=255)
    register_license_id = models.CharField(max_length=255)
    display_checkin_time = models.TimeField()
    display_checkin_time = models.TimeField()
    number_of_rooms = models.IntegerField()
    price_range = models.CharField()
    standard = models.CharField()
    awards = ArrayField(models.CharField(max_length=10), blank=True)
    hit_score = models.CharField(max_length=255)
    accomodation_types = ArrayField(models.CharField(max_length=10), blank=True)
    accomodation_rooms = ArrayField(models.CharField(max_length=10), blank=True)
    

class Restaurant(Place):
    place_name = models.CharField(max_length=255)

class Shop(Place):
    place_name = models.CharField(max_length=255)

class Attraction(Place):
    place_name = models.CharField(max_length=255)