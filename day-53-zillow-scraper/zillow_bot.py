from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

HEADER = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Dnt": "1",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}

def format_address(address):

    if " | " in address:
        return address.split(" | ")[1]
    elif ", " in address:
        return address.split(", ")[1]
    else:
        return address

def format_link(link):

    if "https://www.zillow.com/" in link:
        return link
    else:
        return f"https://www.zillow.com{link}"

def format_price(price):

    price = price.replace("+", "")
    price = price.replace("/mo", "")
    return price.split(" ")[0]

class ZillowBot:

    def __init__(self):

        load_dotenv()
        zillow_url = os.environ.get("ZILLOW_URL", "Zillow URL cannot be found")

        # Get HTML from Zillow webpage
        response = requests.get(url=zillow_url, headers=HEADER)
        self.website_html = response.text

        self.listing_results = []

    def get_listings(self):

        # Use Beautiful Soup
        soup = BeautifulSoup(markup=self.website_html, features="html.parser")

        # listings = soup.find_all(name="li", class_="ListItem-c11n-8-107-0__sc-13rwu5a-0")
        listings = soup.find_all(name="div", class_="property-card-data")

        for listing in listings:
            link = listing.find(name="a")["href"]
            formatted_link = format_link(link)

            price = listing.find(name="span", class_="PropertyCardWrapper__StyledPriceLine-srp-8-107-0__sc-16e8gqd-1").getText()
            formatted_price = format_price(price)

            address = listing.find(name="address").getText()
            formatted_address = format_address(address)

            listing_dict = {
                "price": formatted_price,
                "link": formatted_link,
                "address": formatted_address
            }

            self.listing_results.append(listing_dict)


