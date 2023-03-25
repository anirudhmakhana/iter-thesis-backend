from django.urls import path
from places.views import (
    PlaceView,
    PlaceDetailView,
    AccommodationView,
    AccommodationDetailView,
    RestaurantView,
    RestaurantDetailView,
    ShopView,
    ShopDetailView,
    AttractionView,
    AttractionDetailView,
)

urlpatterns = [
    path('accommodations/', AccommodationView.as_view(), name='accommodation-list'),
    path('accommodations/<str:pk>/', AccommodationDetailView.as_view(), name='accommodation-detail'),
    path('restaurants/', RestaurantView.as_view(), name='restaurant-list'),
    path('restaurants/<str:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('shops/', ShopView.as_view(), name='shop-list'),
    path('shops/<str:pk>/', ShopDetailView.as_view(), name='shop-detail'),
    path('attractions/', AttractionView.as_view(), name='attraction-list'),
    path('attractions/<str:pk>/', AttractionDetailView.as_view(), name='attraction-detail'),
    path('', PlaceView.as_view(), name='place-list'),
    path('<str:pk>/', PlaceDetailView.as_view(), name='place-detail'),
]
# urlpatterns = [
#     path('', PlaceView.as_view(), name='place-list'),
#     path('<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),
#     # path('<str:place_name>/', PlaceDetailView.as_view(), name='place-detail'),
#     path('accommodations/', AccommodationView.as_view(), name='accommodation-list'),
#     path('accommodations/<int:pk>/', AccommodationDetailView.as_view(), name='accommodation-detail'),
#     path('restaurants/', RestaurantView.as_view(), name='restaurant-list'),
#     path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
#     path('shops/', ShopView.as_view(), name='shop-list'),
#     path('shops/<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
#     path('attractions/', AttractionView.as_view(), name='attraction-list'),
#     path('attractions/<int:pk>/', AttractionDetailView.as_view(), name='attraction-detail'),
# ]