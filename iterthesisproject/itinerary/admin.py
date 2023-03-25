from django.contrib import admin

# Register your models here.
from .models import Agenda, Itinerary
class AgendaInline(admin.StackedInline):
    model = Agenda
    extra = 1

    
@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'place', 'date', 'arrival_time', 'leave_time')
    list_filter = ('place', 'date')

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'destination')
    list_filter = ('owner',)
    filter_horizontal = ('co_travelers',)
    readonly_fields = ('plan',)