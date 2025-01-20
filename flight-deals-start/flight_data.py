import os
from calendar import month

import requests

API_KEY = os.environ.get("AMADEUS_API_KEY", "Amadeus Flight API KEY does not exist")
API_SECRET = os.environ.get("AMADEUS_API_SECRET", "Amadeus Flight API SECRET does not exist")
BASE_URL = "https://test.api.amadeus.com/v1"
AUTH_ENDPOINT = "/security/oauth2/token"
LOCATION_ENDPOINT = "/reference-data/locations"
FLIGHT_OFFERS_ENDPOINT = "/shopping/flight-offers"

class FlightData:

    def __init__(self):
        self.location_data = []
        self.city_codes = {}
        self.header = ""

    def get_access_token(self):
        print("Get Access Token for Amadeus API")
        print(f"API KEY: {API_KEY}")
        print(f"API SECRET: {API_SECRET}")

        amadeus_access_response = requests.post(url=f"{BASE_URL}{AUTH_ENDPOINT}",
                                                data={"grant_type": "client_credentials"},
                                                auth=(API_KEY, API_SECRET))

        amadeus_access_response.raise_for_status()
        amadeus_access_token = amadeus_access_response.json()["access_token"]
        print(f"Access Token: {amadeus_access_token}")

        self.header = {"Authorization": f"Bearer {amadeus_access_token}"}

    def get_iata_code(self, city):

        print("Get IATA Codes")
        location_api_params = {
            "subType": "AIRPORT",
            "keyword": city
        }

        location_api_response = requests.get(
            url=f"{BASE_URL}{LOCATION_ENDPOINT}",
            headers=self.header,
            params=location_api_params)

        location_api_response.raise_for_status()
        # self.location_api_json = location_api_response.json()
        return location_api_response.json()["data"][0]["iataCode"]
        #
        # for result in :
        #     iata_list.append(result["iataCode"])
        #
        # # For example {'Chicago': ['ORD', 'MDW', 'RFD', 'DPA', 'GYY', 'PWK'], 'Missoula': ['MSO']}
        # self.city_codes[city] = iata_list




    def get_flight_offers(self, worksheet):

        for row in worksheet.data["prices"]:

            print(f"Get Flight Offers for {row["city"]}...")
            params = {
                "originLocationCode": "MSO",
                "destinationLocationCode": row["iataCode"],
                "departureDate": "2025-02-01",
                "returnDate": "2025-02-15",
                "adults": 1,
                "max": 5,
                "currencyCode": "USD"
            }
            print(f"Params for city: {params}")

            flight_offer_response = requests.get(
                url=f"https://test.api.amadeus.com/v2/shopping/flight-offers",
                headers=self.header,
                params=params)

            flight_offer_response.raise_for_status()
            flight_offer_response_json = flight_offer_response.json()
            print(f"{flight_offer_response_json}")

            for offer in flight_offer_response_json["data"]:
                print(f"{offer["price"]["total"]}")