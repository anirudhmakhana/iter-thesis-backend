from django.urls import path
from .views import ItineraryView, AgendaListCreateView, AgendaDetailView, RequestItineraryView

urlpatterns = [
    path('', ItineraryView.as_view()),
    path('<int:pk>/', ItineraryView.as_view()),
    path('agendas/', AgendaListCreateView.as_view(), name='agenda-list-create'),
    path('agendas/<int:pk>/', AgendaDetailView.as_view(), name='agenda-detail'),
    path('request-itinerary/', RequestItineraryView.as_view(), name='request_itinerary'),
]