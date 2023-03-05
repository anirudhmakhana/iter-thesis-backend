from django.contrib import admin
from .models import *


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'destination', 'latitude', 'longitude')
    list_filter = ('destination',)
    search_fields = ('place_name', 'detail', 'category_description')
    ordering = ('destination', 'place_name',)
    fieldsets = (
        (None, {
            'fields': ('place_name', 'destination', 'category_code')
        }),
        ('Location', {
            'fields': ('latitude', 'longitude', 'sha', 'location')
        }),
        ('Contact', {
            'fields': ('contact',)
        }),
        ('Description', {
            'fields': ('introduction', 'detail', 'category_description')
        }),
        ('Facilities and Services', {
            'fields': ('facilities', 'services')
        }),
        ('Pictures', {
            'fields': ('mobile_picture_urls', 'web_picture_urls')
        }),
        ('Payment Methods', {
            'fields': ('payment_methods',)
        }),
        ('How to Travel', {
            'fields': ('how_to_travels',)
        }),
    )
    # filter_horizontal = ('category_code', 'facilities', 'services', 'how_to_travels',
    #                      'mobile_picture_urls', 'web_picture_urls', 'payment_methods')

@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'hotel_star', 'register_license_id', 'display_checkin_time', 'number_of_rooms', 'price_range', 'standard')
    list_filter = ('hotel_star', 'price_range', 'standard')
    search_fields = ('place_name', 'register_license_id', 'standard')
    ordering = ('place_name', )

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'latitude', 'longitude', 'standard')
    search_fields = ('place_name', 'standard', 'cuisine_types')
    list_filter = ('standard', 'restaurant_types', 'cuisine_types')

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'latitude', 'longitude', 'standard')
    list_filter = ('standard', 'shop_type')
    search_fields = ('place_name', 'standard', 'shop_type')

@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ['id', 'place_name', 'destination', 'hit_score']
    search_fields = ['place_name', 'destination', 'hit_score']
    list_filter = ['destination', 'attraction_types', 'targets', 'activities']
    # filter_horizontal = ['tags', 'targets', 'activities']
    readonly_fields = ['id']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['address', 'sub_district', 'district', 'province', 'postcode']


@admin.register(SHA)
class SHAAdmin(admin.ModelAdmin):
    list_display = ['sha_name', 'sha_type_code', 'sha_type_description', 'sha_cate_id', 'sha_cate_description']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['mobile_number', 'phone_number', 'fax_number', 'emails', 'urls']


@admin.register(OpeningHour)
class OpeningHourAdmin(admin.ModelAdmin):
    list_display = ['day', 'opening_time', 'closing_time']


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ['thai_child', 'thai_adult', 'foreigner_child', 'foreigner_adult']