import requests
import json
from account.models import User
from places.models import Place

# def make_api_request(url, headers=None, params=None):
#     """
#     Makes a GET request to the specified API endpoint and returns the response.

#     Args:
#         url (str): The URL of the API endpoint to query.
#         headers (dict, optional): A dictionary of HTTP headers to include in the request.
#         params (dict, optional): A dictionary of query parameters to include in the request.

#     Returns:
#         dict: A dictionary containing the parsed JSON response from the API.

#     Raises:
#         requests.exceptions.RequestException: If an error occurs while making the API request.
#     """
#     try:
#         response = requests.get(url, headers=headers, params=params)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         raise e

import requests
from django.contrib.auth.models import User
from .models import Agenda, Itinerary

def create_itinerary_with_external_data(owner_username, co_traveler_usernames):
    # Make API request to external server to retrieve destination and plan data
    response = requests.get('https://external-api.com/itineraries/123')
    response_data = response.json()

    # Extract destination and plan data from response
    destination = response_data['destination']
    plan_data = response_data['plan']

    # Create new Itinerary object with destination and plan data
    itinerary = Itinerary.objects.create(
        destination=destination,
        owner=User.objects.get(username=owner_username)
    )

    # Create Agenda objects for each item in plan_data
    for agenda_data in plan_data:
        place_id = agenda_data['place_id']
        date = agenda_data['date']
        arrival_time = agenda_data['arrival_time']
        leave_time = agenda_data['leave_time']
        place = Place.objects.get(pk=place_id)
        agenda = Agenda.objects.create(
            place=place,
            date=date,
            arrival_time=arrival_time,
            leave_time=leave_time
        )
        itinerary.plan.add(agenda)

    # Add co_travelers to itinerary
    for username in co_traveler_usernames:
        user = User.objects.get(username=username)
        itinerary.co_travelers.add(user)

    # Save itinerary to database
    itinerary.save()