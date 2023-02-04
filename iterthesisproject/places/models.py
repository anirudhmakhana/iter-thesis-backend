from django.db import models
from django.contrib.postgres.fields import ArrayField

#Classes used in Place
class Location(models.Model):
    address = models.CharField(max_length=255)
    sub_district = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)

class SHA(models.Model):
    sha_name = models.CharField(max_length=255)
    sha_type_code = models.CharField(max_length=255)
    sha_type_description = models.CharField(max_length=255)
    sha_cate_id = models.CharField(max_length=255)
    sha_cate_description = models.CharField(max_length=255)

class Contact(models.Model):
    mobile_number = ArrayField(
        models.CharField(max_length=100), blank=True
    )
    phone_number = ArrayField(
        models.CharField(max_length=100), blank=True
    )
    fax_number = ArrayField(
        models.CharField(max_length=100), blank=True
    )
    emails = ArrayField(
        models.EmailField(max_length=100), blank=True
    )
    urls = ArrayField(
        models.URLField(max_length=200), blank=True
    )

#Class used in Restaurant, Shop, Attraction
class OpeningHour(models.Model):
    day = models.CharField(max_length=255)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
  
class Fee(models.Model):
    thai_child = models.FloatField()
    thai_adult = models.FloatField()
    foreigner_child = models.FloatField()
    foreigner_adult = models.FloatField() 

class Room(models.Model):
    room_type = models.CharField(max_length=100)
    bd_type = models.CharField(max_length=100)

class Place(models.Model): 
    place_name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    sha = models.ForeignKey(SHA, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    introduction = models.CharField(max_length=255)
    detail = models.TextField()
    destination = models.CharField(max_length=255)
    category_code = ArrayField(models.CharField(max_length=100), blank=True)

    def __str__(self):
        return self.name

class Accommodation(Place):
    hotel_star = models.CharField(max_length=255)
    register_license_id = models.CharField(max_length=255)
    display_checkin_time = models.TimeField()
    display_checkin_time = models.TimeField()
    number_of_rooms = models.IntegerField()
    price_range = models.CharField(max_length=255)
    standard = models.CharField(max_length=255)
    awards = ArrayField(models.CharField(max_length=100), blank=True)
    hit_score = models.CharField(max_length=255)
    accomodation_types = ArrayField(models.CharField(max_length=100), blank=True)
    accomodation_rooms = ArrayField(models.CharField(max_length=100), blank=True)
    

class Restaurant(Place):
    standard = models.CharField(max_length=255)
    awards = ArrayField(models.CharField(max_length=100), blank=True) 
    hit_score = models.CharField(max_length=255)
    restaurant_types = ArrayField(models.CharField(max_length=100), blank=True)
    cuisine_types = ArrayField(models.CharField(max_length=100), blank=True)
    michelines = models.CharField(max_length=255)
    tags = ArrayField(models.CharField(max_length=100), blank=True)
    opening_hours = models.ManyToManyField(OpeningHour, related_name='restaurant_opening_hours')

class Shop(Place): 
    standard = models.CharField(max_length=255)
    shop_type = ArrayField(models.CharField(max_length=100),  blank=True) 
    opening_hours = models.ManyToManyField(OpeningHour, related_name='shop_opening_hours')

class Attraction(Place):
    hit_score = models.CharField(max_length=255)
    attraction_types = ArrayField(models.CharField(max_length=100), blank=True)
    tags = ArrayField(models.CharField(max_length=100), blank=True)
    targets = ArrayField(models.CharField(max_length=100), blank=True)
    activities = ArrayField(models.CharField(max_length=100), blank=True)
    fee = models.OneToOneField(Fee, on_delete=models.CASCADE)
    opening_hours = models.ManyToManyField(OpeningHour, related_name='attraction_opening_hours')  