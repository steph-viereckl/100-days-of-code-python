#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
# International Air Transport Association (IATA) codes for each city. Most of the cities in
# the sheet include multiple airports, you want the city code (not the airport code see here).

from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# STEP 1: Get existing worksheet data using Sheety API
worksheet = DataManager()

# Connect to Amadeus Flight Api
flight_search = FlightSearch()

# Check to see if IATA city codes are blank in worksheet
for row in worksheet.data["prices"]:

    # If blank, use Flight Location API to get city IATA Code
    if row["iataCode"] == "":

        iata_code = flight_search.get_iata_code(row["city"])
        row["iataCode"] = iata_code
        # Update the Worksheet with the correct code
        worksheet.update_iata_code(row)

    # Otherwise, if the IATA city code is populated, skip to next city (no updates needed)
    else:
        print(f"Skip getting IATA code for {row["city"]} since it is already populated")

# For the cities in the worksheet, get current flight offers
flight_search.get_flight_offers(worksheet)

# If any deals are found that are better than the current prices, send an email
for hot_deal in flight_search.hot_deals:
    emailer = NotificationManager()
    emailer.send_email(hot_deal)




