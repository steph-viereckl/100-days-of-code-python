import os
from calendar import month
import requests
from dotenv import load_dotenv
from flight_data import FlightData

BASE_URL = "https://test.api.amadeus.com/v1"
AUTH_ENDPOINT = "/security/oauth2/token"
LOCATION_ENDPOINT = "/reference-data/locations"
FLIGHT_OFFERS_ENDPOINT = "/shopping/flight-offers"
ORIGIN_LOCATION = "ORD"
load_dotenv()

class FlightSearch:

    #This class is responsible for talking to the Flight Search API.
    def __init__(self):

        self.hot_deals = []

        api_key = os.environ.get("AMADEUS_API_KEY", "Amadeus Flight API KEY does not exist")
        api_secret = os.environ.get("AMADEUS_API_SECRET", "Amadeus Flight API SECRET does not exist")

        amadeus_access_response = requests.post(url=f"{BASE_URL}{AUTH_ENDPOINT}",
                                                data={"grant_type": "client_credentials"},
                                                auth=(api_key, api_secret))

        amadeus_access_response.raise_for_status()
        amadeus_access_token = amadeus_access_response.json()["access_token"]

        # Set header variable so it can be used later
        self.header = {"Authorization": f"Bearer {amadeus_access_token}"}

    def get_iata_code(self, city):

        location_api_params = {
            "subType": "CITY",
            "keyword": city
        }

        location_api_response = requests.get(
            url=f"{BASE_URL}{LOCATION_ENDPOINT}",
            headers=self.header,
            params=location_api_params
        )

        location_api_response.raise_for_status()
        return location_api_response.json()["data"][0]["iataCode"]

    def get_cheapest_flight_offer(self, city, origin_code, destination_code, from_time, to_time, lowest_price, is_direct="true"):

        print(f"Get Flight Offers for {city}...")

        params = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": from_time,
            "returnDate": to_time,
            "adults": 1,
            "max": 5,
            "currencyCode": "USD",
            "nonStop": is_direct
        }

        flight_offer_response = requests.get(
            url=f"https://test.api.amadeus.com/v2/shopping/flight-offers",
            headers=self.header,
            params=params)

        flight_offer_response.raise_for_status()
        flight_offer_response_json = flight_offer_response.json()
        print(f"Flight Offer Response: {flight_offer_response_json}")

        cheapest_flight = None

        for offer in flight_offer_response_json["data"]:

            current_price = float(offer["price"]["total"])

            if float(offer["price"]["total"]) < lowest_price:
                cheapest_flight = FlightData(
                    current_price,
                    origin_code,
                    destination_code,
                    from_time,
                    to_time,
                    len(offer["itineraries"])
                )

                lowest_price = current_price

        if cheapest_flight:
            print(f"Found new Cheap Flight for {city} for ${cheapest_flight.price}")
            return cheapest_flight
        else:
            print(f"Could not find Cheap Flight for {city}")
            return None


    # def get_flight_offers(self, worksheet):
    #
    #     list_of_hot_deals = []
    #
    #     for row in worksheet.data["prices"]:
    #
    #         print(f"Get Flight Offers for {row["city"]}...")
    #
    #         params = {
    #             "originLocationCode": "MSO",
    #             "destinationLocationCode": row["iataCode"],
    #             "departureDate": "2025-02-01",
    #             "returnDate": "2025-02-15",
    #             "adults": 1,
    #             "max": 5,
    #             "currencyCode": "USD"
    #         }
    #
    #         flight_offer_response = requests.get(
    #             url=f"https://test.api.amadeus.com/v2/shopping/flight-offers",
    #             headers=self.header,
    #             params=params)
    #
    #         flight_offer_response.raise_for_status()
    #         flight_offer_response_json = flight_offer_response.json()
    #         print(f"Flight Offer Response: {flight_offer_response_json}")
    #
    #         cheapest_price = float(row["lowestPrice"])
    #         print(f"Cheapest price for {row["city"]} is {cheapest_price}")
    #
    #         for offer in flight_offer_response_json["data"]:
    #
    #             current_price = float(offer["price"]["total"])
    #             print(f"Current Price is {current_price} and cheapest is {cheapest_price}")
    #
    #             if current_price < cheapest_price:
    #                 print("Found new cheap price!")
    #                 cheapest_flight = FlightData(current_price, "MSO", row["iataCode"], "N/A", "N/A")
    #                 cheapest_price = current_price
    #
    #
    #         if cheapest_flight:
    #             print(f"Found new Cheap Flight: {cheapest_flight.price}")
    #             list_of_hot_deals.append(cheapest_flight)
    #
    #     self.hot_deals = list_of_hot_deals