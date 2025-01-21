from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CODE = "MSO"

# STEP 1: Get existing worksheet data using Sheety API
worksheet = DataManager()
# Connect to Amadeus Flight Api
flight_search = FlightSearch()

# Check to see if IATA city codes are blank in worksheet
for row in worksheet.price_data["prices"]:

    # If blank, use Flight Location API to get city IATA Code
    if row["iataCode"] == "":
        iata_code = flight_search.get_iata_code(row["city"])
        row["iataCode"] = iata_code
        # Update the Worksheet with the correct code
        worksheet.update_data(row)

    # Otherwise, if the IATA city code is populated, skip to next city (no updates needed)
    else:
        print(f"Skip getting IATA code for {row["city"]} since it is already populated")

list_of_hot_deals = []

# For the cities in the worksheet, get current flight offers
for row in worksheet.price_data["prices"]:

    non_stop_cheap_flight = flight_search.get_cheapest_flight_offer(
        city = row["city"],
        origin_code = ORIGIN_CODE,
        destination_code = row["iataCode"],
        from_time = "2025-02-01",
        to_time = "2025-02-15",
        lowest_price = float(row["lowestPrice"])
    )

    # If a cheap flight was found, add it to the list
    if non_stop_cheap_flight:
        list_of_hot_deals.append(non_stop_cheap_flight)

    # If a cheap flight was not found, try to find a non-direct flight
    else:

        non_direct_cheap_flight = flight_search.get_cheapest_flight_offer(
            city=row["city"],
            origin_code=ORIGIN_CODE,
            destination_code=row["iataCode"],
            from_time="2025-02-01",
            to_time="2025-02-15",
            lowest_price=float(row["lowestPrice"]),
            is_direct="false"
        )

        # If a cheap flight was found, add it to the list
        if non_direct_cheap_flight:
            list_of_hot_deals.append(non_direct_cheap_flight)

print(f"Here are the hot deals: {list_of_hot_deals}")

worksheet.get_customer_emails()

# If any deals are found that are better than the current prices, send an email
for hot_deal in list_of_hot_deals:
    emailer = NotificationManager()
    emailer.send_email(hot_deal, worksheet.user_data["users"])




