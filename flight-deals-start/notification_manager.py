import smtplib
import os
from dotenv import load_dotenv

class NotificationManager:

    def __init__(self):

        load_dotenv()
        self.email = os.environ.get("EMAIL", "ENV Email Variable cannot be found")
        self.password = os.environ.get("EMAIL_PASSWORD", "ENV Email Password cannot be found")

    def send_email(self, hot_deal):

        # Object from smtp class to connect to specific provider
        with smtplib.SMTP("smtp.gmail.com") as connection:

            subject = f"Subject:Hot Flight Alert for {hot_deal.arrival_iata_code}"
            body = (f"Hurry! There is a new deal for a flight from {hot_deal.departure_iata_code} to "
                    f"{hot_deal.arrival_iata_code} for only ${hot_deal.price}")
            message = f"{subject}\n\n{body}"

            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email,
                                to_addrs=self.email,
                                msg=message)

        print(f"Send email about hot deal price {hot_deal.price}")
