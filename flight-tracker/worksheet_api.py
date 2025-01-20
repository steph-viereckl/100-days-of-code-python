import os
import requests

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN", "Sheety Bearer Token does not exist")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT", "Sheety Endpoint was not found")

class SheetyApi():

    def __init__(self):

        self.header = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
        print(self.header)
        self.city_list = []
        self.worksheet_data = {}

    def get_sheet_data(self, fake_data):

        # To conserve api calls, if fake data is false, then use hard coded data
        if fake_data is False:

            sheety_response = requests.get(url=SHEETY_ENDPOINT, headers=self.header)
            sheety_response.raise_for_status()
            self.worksheet_data = sheety_response.json()

        else:
            # {'prices': [{'city': 'Chicago', 'iataCode': '', 'lowestPrice': 42, 'id': 2}, {'city': 'Missoula', 'iataCode': '', 'lowestPrice': 95, 'id': 3}]}
            self.worksheet_data = {
                "prices": [
                    {"city": "Chicago",
                     "iataCode": "",
                     "lowestPrice": 49,
                     "id": 2
                     },
                    {"city": "Missoula",
                     "iataCode": "",
                     "lowestPrice": 40,
                     "id": 3
                     },
                ]
            }


    # Now that we have a list of IATA codes, update the Google Worksheet
    def update_iata_codes(self, flight_data):

        # For each city in the worksheet
        for row in self.worksheet_data["prices"]:

            # Get a list of IATA codes from the flight data object
            iata_list = flight_data.city_codes[row["city"]]
            # Convert list into comma separated string
            iata_string = ",".join(iata_list)
            row["iataCode"] = iata_string
            # Update the row in the sheet
            print(f"Row: {row}")
            print(f"Row: {row["id"]}")

            updated_data = {
                "price": row
            }

            print(f"updated_data: {updated_data}")

            update_iata_response = requests.put(url=f"{SHEETY_ENDPOINT}/{row["id"]}", json=updated_data, headers=self.header)
            update_iata_response.raise_for_status()
            print(update_iata_response.json())


    # print(self.city_list)
    # ['Paris', 'Frankfurt', 'Tokyo', 'Hong Kong', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Dublin']
    # {'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}
    # {'city': 'Frankfurt', 'iataCode': '', 'lowestPrice': 42, 'id': 3}
    # {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}
    # {'city': 'Hong Kong', 'iataCode': '', 'lowestPrice': 551, 'id': 5}
    # {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}
    # {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}
    # {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}
    # {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}
    # {'city': 'Dublin', 'iataCode': '', 'lowestPrice': 378, 'id': 10}
