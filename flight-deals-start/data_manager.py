import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:

    def __init__(self):

        self.token = os.environ.get("SHEETY_TOKEN", "Sheety Bearer Token does not exist")
        self.prices_endpoint = os.environ.get("PRICES_SHEET_ENDPOINT", "Sheety 'Prices' Endpoint was not found")
        self.users_endpoint = os.environ.get("USERS_SHEET_ENDPOINT", "Sheety 'Users' Endpoint was not found")
        self.header = {"Authorization": f"Bearer {self.token}"}

        # Comment out when conserving API Calls
        # sheety_response = requests.get(url=self.prices_endpoint, headers=self.header)
        # sheety_response.raise_for_status()
        # self.price_data = sheety_response.json()

        # Uncomment when faking data to conserve API Calls
        self.price_data = {
            "prices": [
                {"city": "Seattle",
                 "iataCode": "SEA",
                 "lowestPrice": 1000,
                 "id": 2
                 },
                # {"city": "Portland",
                #  "iataCode": "PDX",
                #  "lowestPrice": 1000,
                #  "id": 3
                #  },
                # {"city": "London",
                #  "iataCode": "LON",
                #  "lowestPrice": 1000,
                #  "id": 3
                #  },
            ]
        }

        print(f"Worksheet data: {self.price_data}")

    # Now that we have a list of IATA codes, update the Google Worksheet
    def update_data(self, row):

            updated_data = {
                "price": row
            }

            print(f"updated_data: {updated_data}")

            update_iata_response = requests.put(url=f"{self.prices_endpoint}/{row["id"]}", json=updated_data, headers=self.header)
            update_iata_response.raise_for_status()
            print(update_iata_response.json())

    # Now that we have a list of IATA codes, update the Google Worksheet
    def get_customer_emails(self):

        sheety_response = requests.get(url=self.users_endpoint, headers=self.header)
        sheety_response.raise_for_status()
        self.user_data = sheety_response.json()


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
