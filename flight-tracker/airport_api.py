import os
import requests

AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY", "Amadeus Flight API KEY does not exist")
AMADEUS_SECRET = os.environ.get("AMADEUS_API_SECRET", "Amadeus Flight API SECRET does not exist")
AMADEUS_BASE_URL = "https://test.api.amadeus.com/v1"
AUTH_ENDPOINT = "/security/oauth2/token"
LOCATION_ENDPOINT = "/reference-data/locations"
FLIGHT_OFFERS_ENDPOINT = "/shopping/flight-offers"

class FlightApi():

    def __init__(self):
        self.location_data = []
        self.city_codes = {}
        self.header = ""

    def get_access_token(self):

        amadeus_access_response = requests.post(url=f"{AMADEUS_BASE_URL}{AUTH_ENDPOINT}",
                                                data={"grant_type": "client_credentials"},
                                                auth=(AMADEUS_API_KEY, AMADEUS_SECRET))

        amadeus_access_response.raise_for_status()
        amadeus_access_token = amadeus_access_response.json()["access_token"]
        self.header = {"Authorization": f"Bearer {amadeus_access_token}"}

    def get_iata_codes(self, city):

        location_api_params = {
            "subType": "AIRPORT",
            "keyword": city
        }

        location_api_response = requests.get(
            url=f"{AMADEUS_BASE_URL}{LOCATION_ENDPOINT}",
            headers=self.header,
            params=location_api_params)

        location_api_response.raise_for_status()
        # self.location_api_json = location_api_response.json()
        iata_list = []

        for result in location_api_response.json()["data"]:
            iata_list.append(result["iataCode"])

        # For example {'Chicago': ['ORD', 'MDW', 'RFD', 'DPA', 'GYY', 'PWK'], 'Missoula': ['MSO']}
        self.city_codes[city] = iata_list

    def get_flight_offers(self):

        flight_offer_params = {
            "X-HTTP-Method-Override": "GET",
            "getFlightOffersBody": {
                "currencyCode": "USD",
                "originDestinations": [{
                    "id": "1",
                    "originLocationCode": "MSO",
                    "destinationLocationCode": "ORH",
                    "departureDateTimeRange": {
                        "date": "2025-01-31",
                        "time": "10:00:00"
                    }
                }],
                "travelers": [{
                    "id": "1",
                    "travelerType": "ADULT"
                }],
                "sources": [
                    "GDS"
                ],
                "searchCriteria": {
                    "maxFlightOffers": 2,
                    "flightFilters": {
                        "cabinRestrictions": [{
                            "cabin": "BUSINESS",
                            "coverage": "MOST_SEGMENTS",
                            "originDestinationIds": [
                                "1"
                            ]}
                        ]
                    }
                }
            }
        }

        flight_offer_response = requests.post(
            url=f"{AMADEUS_BASE_URL}{FLIGHT_OFFERS_ENDPOINT}",
            headers=self.header,
            params=flight_offer_params)

        flight_offer_response.raise_for_status()
        flight_offer_response_json = flight_offer_response.json()
        print(f"flight_offer_response_json: flight_offer_response_json")