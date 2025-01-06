import requests
from datetime import datetime
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# print(response.status_code)

# Response codes tell us if our request succeeded or failed
# 1XX: Hold on something is happening it's not final
# 2XX: Here you go
# 3##: You don't have permission
# 4XX: You did something wrong, it may not exist
# 5XX: We did something wrong (server is down)
# https://www.webfx.com/web-development/glossary/http-status-codes/

# Requests has a method that will raise exceptions for you
# response.raise_for_status()
#
# data = response.json()
# print(data)



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(f"Data: {data}")
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(f"sunrise: {sunrise} and sunset: {sunset}")

sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(f"sunrise_hour: {sunrise_hour} and sunset_hour: {sunset_hour}")


time_now = datetime.now()
print(time_now.now())