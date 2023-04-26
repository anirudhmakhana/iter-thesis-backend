from django.db import models
from django.contrib.postgres.fields import ArrayField

#Classes used in Place
class Location(models.Model):
    address = models.CharField(max_length=255, blank=True)
    sub_district = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=255, blank=True)

class SHA(models.Model):
    sha_name = models.CharField(max_length=255, blank=True, null=True)
    sha_type_code = models.CharField(max_length=255, blank=True, null=True)
    sha_type_description = models.CharField(max_length=255, blank=True, null=True)
    sha_cate_id = models.CharField(max_length=255, blank=True, null=True)
    sha_cate_description = models.CharField(max_length=255, blank=True, null=True)

class Contact(models.Model):
    mobile_number = ArrayField(
        models.CharField(max_length=100, null=True, blank=True), blank=True, default=list
    )
    phone_number = ArrayField(
        models.CharField(max_length=100, null=True, blank=True), blank=True, default=list
    )
    fax_number = ArrayField(
        models.CharField(max_length=100, null=True, blank=True), blank=True, default=list
    )
    emails = ArrayField(
        models.EmailField(max_length=100, null=True, blank=True), blank=True, default=list
    )
    urls = ArrayField(
        models.URLField(max_length=200, null=True, blank=True), blank=True, default=list, null=True
    )

#Class used in Restaurant, Shop, Attraction
class OpeningHour(models.Model):
    day = models.CharField(max_length=255)
    opening_time = models.CharField(max_length=255, null=True, blank=True)
    closing_time = models.CharField(max_length=255, null=True, blank=True)
  
class Fee(models.Model):
    thai_child = models.FloatField(default=0)
    thai_adult = models.FloatField(default=0)
    foreigner_child = models.FloatField(default=0)
    foreigner_adult = models.FloatField(default=0) 

class Michelin(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(null=True, blank=True)

class Place(models.Model): 
    id = models.CharField(primary_key=True, max_length=100)
    place_name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    sha = models.ForeignKey(SHA, on_delete=models.CASCADE, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=True, null=True)
    introduction = models.CharField(max_length=2500, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    destination = models.CharField(max_length=255, blank=True, null=True)
    category_code = models.CharField(max_length=255, default='')
    category_description = models.CharField(max_length=255, default='')
    how_to_travels = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    mobile_picture_urls = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    web_picture_urls = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    payment_methods = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    facilities = ArrayField(models.CharField(max_length=100), blank=True, default=list, null=True)
    services = ArrayField(models.CharField(max_length=100), blank=True, default=list, null=True)

class Accommodation(Place):
    hotel_star = models.CharField(max_length=255, blank=True)
    register_license_id = models.CharField(max_length=255, blank=True, null=True)
    display_checkin_time = models.CharField(max_length=255, blank=True, null=True)
    number_of_rooms = models.IntegerField(blank=True)
    price_range = models.CharField(max_length=255)
    standard = models.CharField(max_length=255, blank=True, null=True)
    awards = ArrayField(models.CharField(max_length=100, blank=True), blank=True, null=True, default=list)
    hit_score = models.CharField(max_length=255, blank=True)
    accomodation_types = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    accomodation_rooms = ArrayField(models.CharField(max_length=100), blank=True, default=list)

class Room(models.Model):
    room_type = models.CharField(max_length=100)
    bd_type = models.CharField(max_length=100)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='rooms', null=True)

class Restaurant(Place):
    standard = models.CharField(max_length=255, blank=True)
    awards = ArrayField(models.CharField(max_length=100, blank=True, null=True), blank=True, null=True, default=list) 
    hit_score = models.CharField(max_length=255)
    restaurant_types = ArrayField(models.CharField(max_length=100, null=True, blank=True), blank=True, null=True)
    cuisine_types = ArrayField(models.CharField(max_length=100), blank=True)
    # michelines = models.CharField(max_length=255)
    tags = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    opening_hours = models.ManyToManyField(OpeningHour, related_name='restaurant_opening_hours', null=True, blank=True, default=list)
    michelins = models.ManyToManyField(Michelin, blank=True)

class Shop(Place): 
    standard = models.CharField(max_length=255, null=True, blank=True)
    shop_type = ArrayField(models.CharField(max_length=100, blank=True, null=True),  blank=True, null=True) 
    opening_hours = models.ManyToManyField(OpeningHour, related_name='shop_opening_hours', null=True, blank=True, default=list)

class Attraction(Place):
    hit_score = models.CharField(max_length=255)
    attraction_types = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    targets = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    activities = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    fee = models.OneToOneField(Fee, on_delete=models.CASCADE, related_name='attraction_fee')
    opening_hours = models.ManyToManyField(OpeningHour, related_name='attraction_opening_hours', null=True, blank=True, default=list)