import smtplib
import random

my_email = "stepythonie@gmail.com"
my_password = "ytrh zxsc afqe xlvp"
#
# # Object from smtp class to connect to specific provider
# with smtplib.SMTP("smtp.gmail.com") as connection:
#
#     # TLS = Transport Layer Security (secures our connection)
#     # Allows email to be encrypted so no one can read it if they intercept
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="stepythonie@yahoo.com",
#                         msg="Subject:Hello World\n\n"
#                             "This is the body of the email")
#
#     # Don't need this if we with the with keyword
#     # connection.close()

# Rename so it is easier to understand
import datetime as dt
#
# # current date at time
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
#
# print(now)
#
# # Create datetime Required to do year, month, day
# day_of_birth = dt.datetime(year=1999, month=12, day=31, hour=1)
# print(day_of_birth)


def get_quote():
    with open("quotes.txt", mode="r") as quote_file:
        quote = random.choice(quote_file.readlines())
        return quote

def send_email(quote_for_email):
    # Object from smtp class to connect to specific provider
    with smtplib.SMTP("smtp.gmail.com") as connection:

        print('Send Email')
        email_message = f"Subject:Happy Monday!\n\n{quote_for_email}"
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="stepythonie@yahoo.com",
                            msg=email_message)

#--------- Program Start ------------#

# If the current day of the week is Monday, send a motivational quote
# Monday is 0, Friday is 4
if dt.datetime.now().weekday() == 4:
    quote = get_quote()
    send_email(quote)







