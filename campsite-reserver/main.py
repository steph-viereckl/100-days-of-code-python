from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
# pip install python-dotenv
from dotenv import load_dotenv
from datetime import date
import calendar

# ============ Helper Methods ===============

def is_friday(date_to_check):
    """Checks if a given date is a Friday."""
    return date_to_check.weekday() == 4  # 4 represents Friday (Monday is 0)
    # return date_to_check.weekday() == 6  # Test with a Sunday reservation

def get_date(date_text):

        # Expected date looks like "May 14, 2025 - Site 027 is available"
        date_text = date_text.replace(",", "")
        date_list = date_text.split(" ")
        year = int(date_list[2])
        month = int(list(calendar.month_abbr).index(date_list[0]))
        day = int(date_list[1])

        return date(year, month, day)

# ============ Get Driver ===============

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Holland Lake Campground
URL = "https://www.recreation.gov/camping/campgrounds/234486"

# Instantiate browser of choice
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
print("Driver collected")

# ============ Find Reservations ===============

friday_reservation = None

while friday_reservation is None:

        print("Find available dates....")
        wait = WebDriverWait(driver, 10)
        availability_tags = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "rec-availability-date")))

        # Loop through available dates and determine if there is an available ("A") and it is a Friday
        for tag in availability_tags:

                reservation_date_string = tag.get_attribute('aria-label')
                reservation_date = get_date(reservation_date_string)

                # If the dates are earlier than July, skip to next 5 days
                if reservation_date < date(2025, 7, 1):
                        print("Skip to July")
                        break

                # If there is an available Friday reservation, click on it!
                if tag.text == "A" and is_friday(reservation_date):
                        print("There is an available friday reservation!")
                        friday_reservation = tag
                        break

                # If we are into the window of "Not Reservable" campsites, give up
                elif tag.text == "NR":
                        friday_reservation = "Not Reservable"
                        break

                # Use an arbitrary date for testing an available campsite
                # elif tag.text == "A" and reservation_date == date(2025, 5, 28):
                #         print("Testing with June 22nd 2025")
                #         friday_reservation = tag
                #         break

        # If we weren't able to find any Friday reservations, go to the next 5 days and try again
        if friday_reservation is None:
                print("Go to next 5 days...")
                next_5_days_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.forward")))
                next_5_days_button.click()

# If we ended the loop because there were no reservable spots, try again tomorrow
if friday_reservation == "Not Reservable":
        print("No reservations in this window found. Try again tomorrow.")

# Otherwise, if we found one, click on it to add to cart and sign in!
elif friday_reservation:
        # Click on reservation
        friday_reservation.click()
        # Click on add to cart button
        add_to_cart_button = driver.find_element(By.CSS_SELECTOR, value="button.availability-page-book-now-button-tracker")
        add_to_cart_button.click()
        print(f"Clicked button")

        # Enter in login credentials
        load_dotenv()
        username = os.environ.get("USERNAME", "Recreation.gov Username cannot be found")
        password = os.environ.get("PASSWORD", "Recreation.gov password cannot be found")
        username_input = driver.find_element(By.CSS_SELECTOR, value="input#email")
        username_input.send_keys(username)
        password_input = driver.find_element(By.CSS_SELECTOR, value="input#rec-acct-sign-in-password")
        password_input.send_keys(password)
        sign_in_button = driver.find_element(By.CSS_SELECTOR, value="button.rec-acct-sign-in-btn")
        sign_in_button.click()
        print(f"Signed in...")
        # Perform the remaining steps manually


