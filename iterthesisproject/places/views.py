from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Place, Accommodation, Restaurant, Shop, Attraction
from .serializers import PlaceSerializer, AccommodationSerializer, RestaurantSerializer, ShopSerializer, AttractionSerializer


class PlaceView(APIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post']
    """
    List all places or create a new place.
    """
    def get(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaceDetailView(APIView):
    """
    Retrieve, update or delete a place instance.
    """
    permission_classes = (IsAuthenticated,)
    
    def get_object(self, pk):
        try:
            return Place.objects.get(pk=pk)
        except Place.DoesNotExist:
            raise Response(Place.errors, status=status.HTTP_404_NOT_FOUND)


    def get(self, request, pk):
        place = self.get_object(pk)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)

    def put(self, request, pk):
        place = self.get_object(pk)
        serializer = PlaceSerializer(place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        place = self.get_object(pk)
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class PlaceDetailView(APIView):
#     """
#     Retrieve, update or delete a place instance.
#     """
#     permission_classes = (IsAuthenticated,)

#     def get_object(self, place_name):
#         try:
#             return Place.objects.get(place_name=place_name)
#         except Place.DoesNotExist:
#             raise Response(Place.errors, status=status.HTTP_404_NOT_FOUND)


#     def get(self, request, place_name):
#         place = self.get_object(place_name)
#         serializer = PlaceSerializer(place)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = PlaceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, place_name):
#         place = self.get_object(place_name)
#         serializer = PlaceSerializer(place, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, place_name):
#         place = self.get_object(place_name)
#         place.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class AccommodationView(APIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post']

    def get(self, request):
        accommodations = Accommodation.objects.all()
        serializer = AccommodationSerializer(accommodations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccommodationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccommodationDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Accommodation.objects.get(pk=pk)
        except Accommodation.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        accommodation = self.get_object(pk)
        serializer = AccommodationSerializer(accommodation)
        return Response(serializer.data)

    def put(self, request, pk):
        accommodation = self.get_object(pk)
        serializer = AccommodationSerializer(accommodation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        accommodation = self.get_object(pk)
        accommodation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# class AccommodationDetailView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get_object(self, place_name):
#         try:
#             return Accommodation.objects.get(place__name=place_name)
#         except Accommodation.DoesNotExist:
#             raise Http404

#     def get(self, request, place_name):
#         accommodation = self.get_object(place_name)
#         serializer = AccommodationSerializer(accommodation)
#         return Response(serializer.data)
    
#     def post(self, request, place_name):
#         serializer = AttractionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(place_name=place_name)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, place_name):
#         accommodation = self.get_object(place_name)
#         serializer = AccommodationSerializer(accommodation, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, place_name):
#         accommodation = self.get_object(place_name)
#         accommodation.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class RestaurantView(APIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post']

    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        restaurant = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def put(self, request, pk):
        restaurant = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        restaurant = self.get_object(pk)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# class RestaurantDetailView(APIView):
#     permission_classes = (IsAuthenticatedOrReadOnly,)

#     def get_object(self, place_name):
#         try:
#             return Restaurant.objects.get(place_name=place_name)
#         except Restaurant.DoesNotExist:
#             raise Http404

#     def get(self, request, place_name):
#         restaurant = self.get_object(place_name)
#         serializer = RestaurantSerializer(restaurant)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = RestaurantSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, place_name):
#         restaurant = self.get_object(place_name)
#         serializer = RestaurantSerializer(restaurant, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, place_name):
#         restaurant = self.get_object(place_name)
#         restaurant.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ShopView(APIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post']

    def get(self, request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShopDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Shop.objects.get(pk=pk)
        except Shop.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        shop = self.get_object(pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)

    def put(self, request, pk):
        shop = self.get_object(pk)
        serializer = ShopSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        shop = self.get_object(pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# class ShopDetailView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get_object(self, place_name):
#         try:
#             return Shop.objects.get(place_name=place_name)
#         except Shop.DoesNotExist:
#             raise Http404

#     def get(self, request, place_name):
#         shop = self.get_object(place_name)
#         serializer = ShopSerializer(shop)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ShopSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def put(self, request, place_name):
#         shop = self.get_object(place_name)
#         serializer = ShopSerializer(shop, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, place_name):
#         shop = self.get_object(place_name)
#         shop.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class AttractionView(APIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post']


    def get(self, request):
        attractions = Attraction.objects.all()
        serializer = AttractionSerializer(attractions, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.method)
        serializer = AttractionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttractionDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_attraction(self, pk):
        try:
            return Attraction.objects.get(pk=pk)
        except Attraction.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        attraction = self.get_attraction(pk)
        serializer = AttractionSerializer(attraction)
        return Response(serializer.data)

    def put(self, request, pk):
        attraction = self.get_attraction(pk)
        serializer = AttractionSerializer(attraction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        attraction = self.get_attraction(pk)
        attraction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class AttractionDetailView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get_attraction(self, place_name):
#         try:
#             return Attraction.objects.get(place__place_name=place_name)
#         except Attraction.DoesNotExist:
#             raise Http404

#     def get(self, request, place_name):
#         attraction = self.get_attraction(place_name)
#         serializer = AttractionSerializer(attraction)
#         return Response(serializer.data)
    
#     def post(self, request):
#         print(request.method)
#         serializer = AttractionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, place_name):
#         attraction = self.get_attraction(place_name)
#         serializer = AttractionSerializer(attraction, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, place_name):
#         attraction = self.get_attraction(place_name)
#         attraction.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
