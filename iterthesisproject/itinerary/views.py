from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from itinerary.models import Itinerary
from itinerary.serializers import ItinerarySerializer

class ItineraryView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        if pk:
            itinerary = Itinerary.objects.get(pk=pk, owner=request.user)
            serializer = ItinerarySerializer(itinerary)
            return Response(serializer.data)
        else:
            itineraries = Itinerary.objects.filter(owner=request.user)
            serializer = ItinerarySerializer(itineraries, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ItinerarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        itinerary = Itinerary.objects.get(pk=pk, owner=request.user)
        serializer = ItinerarySerializer(itinerary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        itinerary = Itinerary.objects.get(pk=pk, owner=request.user)
        itinerary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItineraryDetailView(APIView):
    permission_classes = (IsAuthenticated,)

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