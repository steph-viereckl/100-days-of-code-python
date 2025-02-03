from google_bot import GoogleFormBot
from zillow_bot import ZillowBot

# Use Beautiful Soup to scrape Zillow Listings and get a list of listings
zillow = ZillowBot()
zillow.get_listings()

# Use Selenium to submit a Google Form for each listing
form_bot = GoogleFormBot()
form_bot.populate_form(zillow.listing_results)


