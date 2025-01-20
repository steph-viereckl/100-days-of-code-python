import os
import requests

AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY", "Amadeus Flight API KEY does not exist")
AMADEUS_SECRET = os.environ.get("AMADEUS_API_SECRET", "Amadeus Flight API SECRET does not exist")
AMADEUS_BASE_URL = "https://test.api.amadeus.com/v1"
AMADEUS_LOCATION_API = "/reference-data/locations"
AMADEUS_AUTH_ENDPOINT = "/security/oauth2/token"

class FlightApi():

    def __init__(self):
        self.location_data = []
        self.city_codes = {}

    def get_access_token(self):

        amadeus_access_response = requests.post(url=f"{AMADEUS_BASE_URL}{AMADEUS_AUTH_ENDPOINT}",
                                                data={"grant_type": "client_credentials"},
                                                auth=(AMADEUS_API_KEY, AMADEUS_SECRET))

        amadeus_access_response.raise_for_status()
        self.amadeus_access_token = amadeus_access_response.json()["access_token"]

    def get_iata_codes(self, city):

        location_api_header = {"Authorization": f"Bearer {self.amadeus_access_token}"}
        location_api_params = {
            "subType": "AIRPORT",
            "keyword": city
        }

        location_api_response = requests.get(
            url=f"{AMADEUS_BASE_URL}{AMADEUS_LOCATION_API}",
            headers=location_api_header,
            params=location_api_params)

        location_api_response.raise_for_status()
        # self.location_api_json = location_api_response.json()
        iata_list = []

        for result in location_api_response.json()["data"]:
            iata_list.append(result["iataCode"])

        # For example {'Chicago': ['ORD', 'MDW', 'RFD', 'DPA', 'GYY', 'PWK'], 'Missoula': ['MSO']}
        self.city_codes[city] = iata_list



        print(f"For {city} the codes are: {self.city_codes}")