from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/Magna-Tiles-100-Piece-Clear-Colors-Award-Winning/dp/B000CBSNRY?tag=googhydr-20&source=dsa&hvcampaign=toys&gclid=CjwKCAiAneK8BhAVEiwAoy2HYT-M1bWRyHTq2_XPg-U3TckLF_FtKoK6D69KSq_WfmiKSjQ6bAgJMxoCzT0QAvD_BwE"

# Full headers would look something like this
# https://myhttpheader.com/
header = {
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

# Minimal header
# header = {
#     "Accept-Language":"en-US",
#     "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
# }

response = requests.get(url=URL, headers=header)
website_html = response.text

soup = BeautifulSoup(markup=website_html, features="html.parser")
price = soup.find(name="span", class_="a-price-whole").getText()
decimal = soup.find(name="span", class_="a-price-fraction").getText()
whole_price = float(f"{price}{decimal}")
print(whole_price)

title = soup.find(name="span", id="productTitle")
formatted_title = title.getText().strip().replace("  ", "")
formatted_title.replace("\r", "")
print(formatted_title)

if whole_price < 100:

    # Object from smtp class to connect to specific provider
    with (smtplib.SMTP("smtp.gmail.com") as connection):

        load_dotenv()
        from_email = os.environ.get("FROM_EMAIL", "From Email cannot be found")
        email_password = os.environ.get("PASSWORD", "Email password cannot be found")

        subject_line = f"Subject:Amazon Price Alert!\n\n"
        message = f"{formatted_title} is now ${whole_price}! Buy now at {URL}\n"
        combined_message = subject_line + message
        # Was running into issues with encoding so ignoring some chars
        # updated_message = combined_message.encode('ascii', 'ignore').decode('ascii')
        connection.starttls()
        connection.login(user=from_email, password=email_password)
        connection.sendmail(from_addr=from_email,to_addrs=from_email,msg=combined_message.encode("utf-8"))