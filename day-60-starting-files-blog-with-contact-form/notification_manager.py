import smtplib
import os
from dotenv import load_dotenv

class NotificationManager:

    def __init__(self):

        load_dotenv()
        self.email = os.environ.get("EMAIL", "ENV Email Variable cannot be found")
        self.password = os.environ.get("EMAIL_PASSWORD", "ENV Email Password cannot be found")

    def send_email(self, name, email, phone, message):
        print("Sending email...")

        to_addresses = []

        # Object from smtp class to connect to specific provider
        with smtplib.SMTP("smtp.gmail.com") as connection:

            subject = f"New Contact Request Submitted"
            body = (f"Name: {name} \n"
                    f"Email: {email} \n"
                    f"Phone: {phone} \n"
                    f"Message: {message}"
            )
            message = f"Subject:{subject}\n\n{body}"

            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email,
                                to_addrs=self.email,
                                msg=message)
        print("Email Sent")
