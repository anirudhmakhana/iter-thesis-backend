from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from itinerary.models import Itinerary, Agenda
from itinerary.serializers import ItinerarySerializer, AgendaSerializer

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
        try:
            itinerary = Itinerary.objects.get(pk=pk)
        except Itinerary.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.user == itinerary.owner or request.user in itinerary.co_travellers.all():
            serializer = ItinerarySerializer(itinerary)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

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

        if request.user != itinerary.owner and request.user not in itinerary.co_travellers.all():
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

        if request.user != itinerary.owner and request.user not in itinerary.co_travellers.all():
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