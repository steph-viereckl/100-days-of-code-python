# Terminal command
# python stock-news-extrahard-start/main.py
import requests
import os
import smtplib
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
FROM_EMAIL = "stepythonie@gmail.com"
PASSWORD = os.environ.get("PY_GMAIL_PW")

# Determine if there was a significant (i.e. 5%) stock price change. Return True if so.
def detect_stock_price_change():

    alpha_api_key = os.environ.get("ALPHA_API_KEY")

    alpha_parameters = {
        "function":"TIME_SERIES_DAILY",
        "symbol":STOCK,
        "apikey":alpha_api_key
    }

    stock_response = requests.get(url="https://www.alphavantage.co/query", params=alpha_parameters)
    stock_response.raise_for_status()
    stock_data = stock_response.json()

    # Get yesterday's date formatted in YYYY-MM-DD
    yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    # Get day before yesterday's date formatted in YYYY-MM-DD
    db_yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')

    try:
        yesterday_close = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
        db_yesterday_close = float(stock_data["Time Series (Daily)"][db_yesterday]["4. close"])
        db_yesterday_close = 300.00 # Value to test with

    # Daily API limit of 25 for free trial - catch exception and set hard coded values
    except KeyError as message:
        yesterday_close = 400
        db_yesterday_close = 300.00

    # Get the different between yesterdays' close and the day before in percent (i.e. 20)
    return ((yesterday_close - db_yesterday_close) / yesterday_close) * 100

# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():

    news_api_key = os.environ.get("NEWS_API_KEY")

    news_parameters = {
        "apikey":news_api_key,
        "pageSize":10,
        "language":"en",
        "q":"Tesla"
    }

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()

    news_articles = []

    # There are many news articles that are showing "removed" -
    # so loop through 10 and we will assume we can get 3 valid articles
    for article in news_data["articles"]:

        # Skip article if Author is blank (it was removed)
        if article["author"]:
            news_articles.append(article)

        # Break out of loop once we find 3 valid articles
        if len(news_articles) > 3:
            break

    return news_articles


# Send a separate message with the percentage change and each article's title and description to your phone number.
def send_email(percentage, news_article):

    # Object from smtp class to connect to specific provider
    with (smtplib.SMTP("smtp.gmail.com") as connection):

        if percentage > 0:
            ticker = "🔺"
        else:
            ticker = "🔻"

        subject_line = f"Subject:{STOCK}: {ticker}{abs(percentage)}% - {news_article["title"]}\n\n"
        message = f"{news_article["description"]}\n"
        combined_message = subject_line + message
        # Was running into issues with encoding so ignoring some chars
        updated_message = combined_message.encode('ascii', 'ignore').decode('ascii')
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL,
                            to_addrs="Stepythonie@yahoo.com",
                            msg=updated_message)

########## Program Start ############

# Get Stock Percentage increase or decrease
stock_delta_percentage = detect_stock_price_change()

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday, get email and send news
if 5 < stock_delta_percentage > -5:

    # For each news article, send email (since twilio texts aren't working in US)
    for article in get_news():
        send_email(stock_delta_percentage, article)

else:
    print("Nothing to see here")







#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

