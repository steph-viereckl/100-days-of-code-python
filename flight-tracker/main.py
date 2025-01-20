# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
# International Air Transport Association (IATA) codes for each city. Most of the cities in
# the sheet include multiple airports, you want the city code (not the airport code see here).

import requests
from datetime import datetime
import os
from airport_api import FlightApi
from worksheet_api import SheetyApi

# These are variables that can be toggled on/off
# Toggle off to conserve API usage
FAKE_WORKSHEET_DATA = True
SKIP_WORKSHEET_UPDATE = True

# STEP 1: Get existing worksheet data using Sheety API
sheety_api = SheetyApi()
sheety_api.get_sheet_data(fake_data=FAKE_WORKSHEET_DATA)

# STEP 2: Get Access Token from Amadeus API
flight_api = FlightApi()
flight_api.get_access_token()

# STEP 3: Update IATA Code in Worksheet (optional)
# 1. Find the IATA Code from the Amadeus API
# 2. Update the IATA Code in the Worksheet using Sheety API
if SKIP_WORKSHEET_UPDATE is False:

    # For each city listed in the Google Worksheet, use API to find IATA Code
    for city_data in sheety_api.worksheet_data["prices"]:
        flight_api.get_iata_codes(city_data["city"])

    # Update the Worksheet with the IATA Codes using Sheety APIU
    sheety_api.update_iata_codes(flight_api)

# TODO: Using Flight Search API, check for cheapest flights from tomorrow to 6 months from now

# TODO: If price is lower than current price in Worksheet, send email







