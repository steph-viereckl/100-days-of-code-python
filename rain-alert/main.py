import requests

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
api_key = os.environ.get('OWM_API_KEY')
print(f"os environ: {os.environ}")

print(f"auth token: {auth_token}")
print(f"api key: {api_key}")
# Missoula
# LAT = 46.872131
# LONG = -113.994019

# Paris
LAT = 48.856613
LONG = 2.352222

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid" : api_key,
    "cnt": 4,
    "units": "imperial"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

print(f"Forecast for {response.json()["city"]["name"]}")

hourly_forecasts = response.json()["list"]

will_rain_today = False

for forecast in hourly_forecasts:

    # print(forecast["weather"])
    # print(forecast["weather"][0]["id"])
    # Only bring umbrella if weather code < 500 (raining, not snowing)
    if forecast["weather"][0]["id"] < 600:
        print(f"Bring umbrella because the forecast is {forecast["weather"][0]["main"]}")
        will_rain_today = True
    else:
        print("No rain yay!")

if will_rain_today:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It is going to rain. Bring an umbrella!",
        from_="+18447878112",
        to="+155555555",
    )

    print(message.status)


# Terminal > ENV + Enter
# Environment variables are convenient and more secure because you can modify them without having to touch the code
# Separate where we store where we store our keys away from the code base
# Create by saying export NAME_OF_VARIABLE=1234
# export OWM_API_KEY=1234567