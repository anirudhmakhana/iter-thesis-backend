from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from itinerary.models import Itinerary, Agenda, UserPreference
from itinerary.serializers import ItinerarySerializer, AgendaSerializer, UserPreferenceSerializer
import requests
from django.db.models import Q

class AgendaListCreateView(APIView):
    """
    API View to list all agendas and create a new agenda
    """
    def get(self, request):
        agendas = Agenda.objects.all()
        serializer = AgendaSerializer(agendas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AgendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AgendaDetailView(APIView):
    """
    API View to retrieve, update and delete an agenda
    """
    def get_object(self, pk):
        try:
            return Agenda.objects.get(pk=pk)
        except Agenda.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        agenda = self.get_object(pk)
        serializer = AgendaSerializer(agenda)
        return Response(serializer.data)

    def put(self, request, pk):
        agenda = self.get_object(pk)
        serializer = AgendaSerializer(agenda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        agenda = self.get_object(pk)
        agenda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ##naya wala
# class ItineraryView(APIView):
#     def get(self, request):
#         itineraries = Itinerary.objects.all()
#         serializer = ItinerarySerializer(itineraries, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ItinerarySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ItineraryDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return Itinerary.objects.get(pk=pk)
#         except Itinerary.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         itinerary = self.get_object(pk)
#         serializer = ItinerarySerializer(itinerary)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         itinerary = self.get_object(pk)
#         serializer = ItinerarySerializer(itinerary, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         itinerary = self.get_object(pk)
#         itinerary.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



###############################
# class ItineraryView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request, pk=None):
#         if pk:
#             itinerary = Itinerary.objects.get(pk=pk, owner=request.user)
#             serializer = ItinerarySerializer(itinerary)
#             return Response(serializer.data)
#         else:
#             itineraries = Itinerary.objects.filter(owner=request.user)
#             serializer = ItinerarySerializer(itineraries, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = ItinerarySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         itinerary = Itinerary.objects.get(pk=pk, owner=request.user)
#         serializer = ItinerarySerializer(itinerary, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         itinerary = Itinerary.objects.get(pk=pk, owner=request.user)
#         itinerary.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ItineraryView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        if pk is None:
            itineraries = Itinerary.objects.filter(Q(owner=request.user) | Q(co_travelers=request.user))
            serializer = ItinerarySerializer(itineraries, many=True)
            return Response(serializer.data)
        else:
            try:
                itinerary = Itinerary.objects.get(pk=pk)
            except Itinerary.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if request.user == itinerary.owner or request.user in itinerary.co_travelers.all():
                serializer = ItinerarySerializer(itinerary)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
    
    # def get(self, request, pk=None):
    #     try:
    #         itinerary = Itinerary.objects.get(pk=pk)
    #     except Itinerary.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     if request.user == itinerary.owner or request.user in itinerary.co_travelers.all():
    #         serializer = ItinerarySerializer(itinerary)
    #         return Response(serializer.data)
    #     else:
    #         return Response(status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        print(request.data)
        serializer = ItinerarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     serializer = ItinerarySerializer(data=request.data)
    #     if serializer.is_valid():
    #         itinerary = serializer.save(owner=request.user)
    #         return Response(ItinerarySerializer(instance=itinerary).data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            itinerary = Itinerary.objects.get(pk=pk)
        except Itinerary.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.user != itinerary.owner and request.user not in itinerary.co_travelers.all():
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = ItinerarySerializer(itinerary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            itinerary = Itinerary.objects.get(pk=pk)
        except Itinerary.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.user != itinerary.owner and request.user not in itinerary.co_travelers.all():
            return Response(status=status.HTTP_403_FORBIDDEN)

        itinerary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItineraryDetailView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get_itinerary(self, pk):
        try:
            return Itinerary.objects.get(pk=pk, owner=self.request.user)
        except Itinerary.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        itinerary = self.get_itinerary(pk)
        serializer = ItinerarySerializer(itinerary)
        return Response(serializer.data)

    def put(self, request, pk):
        itinerary = self.get_itinerary(pk)
        serializer = ItinerarySerializer(itinerary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        itinerary = self.get_itinerary(pk)
        itinerary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# '''
# Caching data and shit like that
# ''' 
# class RequestItineraryView(APIView):
#     def post(self, request):
#         # //TODO: Return answer to the question.
        
#         # Retrieve data from the request, e.g. budget, travel dates, etc.
#         budget = request.data.get('budget')
#         start_date = request.data.get('start_date')
#         end_date = request.data.get('end_date')

#         # Generate a cache key based on the request data
#         cache_key = f'request_itinerary_{budget}_{start_date}_{end_date}'

#         # # Check if the response is already cached
#         # response = cache.get(cache_key)
#         # if response:
#         #     return Response(response)

#         # # If the response is not cached, generate the itinerary and cache the response
#         # itinerary = generate_itinerary(budget, start_date, end_date)  # some function to generate the itinerary
#         # response = {'itinerary': itinerary}  # create the response payload
#         # cache.set(cache_key, response, timeout=3600)  # cache the response for 1 hour

#         return Response(response)
    
class UserPreferenceView(APIView):
    """
    List all user preferences or create a new one
    """
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        user_preferences = UserPreference.objects.all()
        serializer = UserPreferenceSerializer(user_preferences, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = UserPreferenceSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = UserPreferenceSerializer(data=request.data)
        if serializer.is_valid():
            user_preference = serializer.save(user=request.user) # pass in the user object
            
            # Send a POST request to another server with the user's preferences
            url = "https://22cd-125-24-236-177.ngrok-free.app/api/recommenditinerary"
            data = serializer.data
            response = requests.post(url, json=data)
            if response.status_code == 200:
                user_preference.sent_to_server = True
                user_preference.save()
            
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(response.json, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserPreferenceDetail(APIView):
    """
    Retrieve, update or delete a user preference instance
    """
    def get_object(self, pk):
        try:
            return UserPreference.objects.get(pk=pk)
        except UserPreference.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_preference = self.get_object(pk)
        serializer = UserPreferenceSerializer(user_preference)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_preference = self.get_object(pk)
        serializer = UserPreferenceSerializer(user_preference, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_preference = self.get_object(pk)
        user_preference.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)