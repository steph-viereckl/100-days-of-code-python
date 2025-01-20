# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
# International Air Transport Association (IATA) codes for each city. Most of the cities in
# the sheet include multiple airports, you want the city code (not the airport code see here).

from airport_api import FlightApi
from worksheet_api import SheetyApi

# STEP 1: Get existing worksheet data using Sheety API
worksheet = SheetyApi()

# STEP 2: Get Access Token from Amadeus API
flight_data = FlightApi()
flight_data.get_access_token()

# STEP 3: Update IATA Code in Worksheet (optional)
# 1. Find the IATA Code from the Amadeus API
# 2. Update the IATA Code in the Worksheet using Sheety API
# For each city listed in the Google Worksheet, use API to find IATA Code
# for city_data in worksheet.worksheet_data["prices"]:
#     flight_data.get_iata_codes(city_data["city"])
#
# # Update the Worksheet with the IATA Codes using Sheety APIU
# worksheet.update_iata_codes(flight_data)
flight_data.get_flight_offers()

# TODO: Using Flight Search API, check for cheapest flights from tomorrow to 6 months from now

# TODO: If price is lower than current price in Worksheet, send email







