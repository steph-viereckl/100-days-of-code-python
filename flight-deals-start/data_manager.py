import os
import requests

TOKEN = os.environ.get("SHEETY_TOKEN", "Sheety Bearer Token does not exist")
ENDPOINT = os.environ.get("SHEETY_ENDPOINT", "Sheety Endpoint was not found")

class DataManager:

    def __init__(self):

        self.header = {"Authorization": f"Bearer {TOKEN}"}

        # Comment out when conserving API Calls
        # sheety_response = requests.get(url=SHEETY_ENDPOINT, headers=self.header)
        # sheety_response.raise_for_status()
        # self.data = sheety_response.json()

        # {'prices': [{'city': 'Chicago', 'iataCode': '', 'lowestPrice': 42, 'id': 2}, {'city': 'Missoula', 'iataCode': '', 'lowestPrice': 95, 'id': 3}]}
        self.data = {
            "prices": [
                {"city": "Chicago",
                 "iataCode": "ORD",
                 "lowestPrice": 500,
                 "id": 2
                 },
                {"city": "Los Angeles",
                 "iataCode": "LAX",
                 "lowestPrice": 600,
                 "id": 3
                 },
            ]
        }

    # Now that we have a list of IATA codes, update the Google Worksheet
    def update_iata_code(self, row):

            # # Get a list of IATA codes from the flight data object
            # iata_list = flight_data.city_codes[row["city"]]
            # # Convert list into comma separated string
            # iata_string = ",".join(iata_list)
            # # Update data with IATA String
            # row["iataCode"] = iata_string
            # # Update the row in the sheet in a format Sheety will understand
            updated_data = {
                "price": row
            }

            print(f"updated_data: {updated_data}")

            update_iata_response = requests.put(url=f"{ENDPOINT}/{row["id"]}", json=updated_data, headers=self.header)
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
