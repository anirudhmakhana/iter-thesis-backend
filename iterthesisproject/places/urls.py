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

# urlpatterns = [
#     path('', PlaceView.as_view(), name='place-list'),
#     path('<str:place_name>/', PlaceDetailView.as_view(), name='place-detail'),
#     path('accommodations/', AccommodationView.as_view(), name='accommodation-list'),
#     path('accommodations/<str:place_name>/', AccommodationDetailView.as_view(), name='accommodation-detail'),
#     path('restaurants/', RestaurantView.as_view(), name='restaurant-list'),
#     path('restaurants/<str:place_name>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
#     path('shops/', ShopView.as_view(), name='shop-list'),
#     path('shops/<str:place_name>/', ShopDetailView.as_view(), name='shop-detail'),
#     path('attractions/', AttractionView.as_view(), name='attraction-list'),
#     path('attractions/<str:place_name>/', AttractionDetailView.as_view(), name='attraction-detail'),
# ]
urlpatterns = [
    path('', PlaceView.as_view(), name='place-list'),
    path('<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),
    # path('<str:place_name>/', PlaceDetailView.as_view(), name='place-detail'),
    path('accommodations/', AccommodationView.as_view(), name='accommodation-list'),
    path('accommodations/<int:pk>/', AccommodationDetailView.as_view(), name='accommodation-detail'),
    path('restaurants/', RestaurantView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('shops/', ShopView.as_view(), name='shop-list'),
    path('shops/<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
    path('attractions/', AttractionView.as_view(), name='attraction-list'),
    path('attractions/<int:pk>/', AttractionDetailView.as_view(), name='attraction-detail'),
]