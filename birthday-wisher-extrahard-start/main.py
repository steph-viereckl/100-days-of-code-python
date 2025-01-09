##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import smtplib
import datetime as dt
import pandas

FROM_EMAIL = "stepythonie@gmail.com"
# PASSWORD = "ytrh zxsc afqe xlvp" # This is old - I created a new one


def get_letter(name):

    random_letter_num = random.randint(1,3)
    file_path = f"letter_templates/letter_{random_letter_num}.txt"

    with open(file_path, mode="r") as data:
        letter = data.read()
        updated_letter = letter.replace("[NAME]", name)
        print(f"Letter Updated: {updated_letter}")
        return updated_letter

def get_birthdays():

    current_month = dt.datetime.now().month
    current_day = dt.datetime.now().day

    birthdays_df = pandas.read_csv("birthdays.csv")
    current_birthdays = []

    for (index, row) in birthdays_df.iterrows():
        if row.month == current_month and row.day == current_day:
            current_birthdays.append(row)

    return current_birthdays

def send_email(birthday):

    # Object from smtp class to connect to specific provider
    with smtplib.SMTP("smtp.gmail.com") as connection:

        to_email = birthday["email"]
        message_body = get_letter(birthday["name"])
        email_message = f"Subject:Happy Birthday!\n\n{message_body}"
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL,
                            to_addrs=to_email,
                            msg=email_message)

        print()

########## Program Start #########

current_birthdays = get_birthdays()

for current_birthday in current_birthdays:
    send_email(current_birthday)

# Angela's solution includes using a tuple as they key with the month and day
today_tuple = (dt.datetime.now().month, dt.datetime.now().day,)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}