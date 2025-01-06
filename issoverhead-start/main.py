import requests
from datetime import datetime, timezone
import smtplib

MY_LAT = 46.872131
MY_LONG = -113.994019
FROM_EMAIL = "stepythonie@gmail.com"
PASSWORD = "ytrh zxsc afqe xlvp"

# Your position is within +5 or -5 degrees of the ISS position.
def iss_is_above():

    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_response_data = iss_response.json()

    iss_latitude = float(iss_response_data["iss_position"]["latitude"])
    iss_longitude = float(iss_response_data["iss_position"]["longitude"])

    # Fake the ISS in the correct position
    iss_latitude = 42
    iss_longitude = -100

    if abs(iss_latitude - MY_LAT) <= 5:
        return True
    elif abs(iss_longitude - MY_LONG) <= 5:
        return True
    else:
        print('ISS is not currently above you')
        return False

def is_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    sunrise_sunset_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sunrise_sunset_response.raise_for_status()
    sunrise_sunset_data = sunrise_sunset_response.json()
    sunrise_utc = sunrise_sunset_data["results"]["sunrise"]
    sunset_utc = sunrise_sunset_data["results"]["sunset"]

    sunrise_hour_utc = int(sunrise_utc.split("T")[1].split(":")[0])
    sunset_hour_utc = int(sunset_utc.split("T")[1].split(":")[0])
    current_hour_utc = datetime.now(timezone.utc).hour
    current_hour_utc = 12 # Testing

    print(f"current hour: {current_hour_utc}")
    print(f"sunrise: {sunrise_hour_utc}")
    print(f"sunset: {sunset_hour_utc}")

    if current_hour_utc > sunset_hour_utc and current_hour_utc < sunrise_hour_utc:
        return True
    else:
        print('It is not currently dark enough to see the ISS')
        return False

def send_email():

    print('Sending Email....')

    # Object from smtp class to connect to specific provider
    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs="stepythonie@yahoo.com",
            msg="Subject:ISS is above you!\n\nRun outside and go see it!")

################## Run Program ################

# If ISS is above you and it is currently dark
if iss_is_above() and is_dark():
    # Send email notifying you to look up
    send_email()



