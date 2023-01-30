from django.urls import path
from .views import ItineraryView

urlpatterns = [
    path('', ItineraryView.as_view()),
    path('<int:pk>/', ItineraryView.as_view()),
]