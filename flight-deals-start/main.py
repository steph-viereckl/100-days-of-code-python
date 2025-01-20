#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
# International Air Transport Association (IATA) codes for each city. Most of the cities in
# the sheet include multiple airports, you want the city code (not the airport code see here).

from flight_data import FlightData
from data_manager import DataManager

# STEP 1: Get existing worksheet data using Sheety API
worksheet = DataManager()
print(f"Worksheet.data: {worksheet.data}")

# STEP 2: Get Access Token from Amadeus API
flight_data = FlightData()
flight_data.get_access_token()

# STEP 3: If IATA Code is blank, update it
for row in worksheet.data["prices"]:

    if row["iataCode"] == "":
        iata_code = flight_data.get_iata_code(row["city"])
        row["iataCode"] = iata_code
        print(f"{iata_code}")
        worksheet.update_iata_code(row)
    else:
        print(f"Skip getting IATA code for {row["city"]} since it is already populated")


# flight_data.get_flight_offers(worksheet)

# TODO: Using Flight Search API, check for cheapest flights from tomorrow to 6 months from now

# TODO: If price is lower than current price in Worksheet, send email







