from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
# pip install python-dotenv
from dotenv import load_dotenv
from datetime import date
import calendar

# ============ Helper Methods ===============

def get_day_number(day_string=str):
    return getattr(calendar, day_string.upper())

def get_date(date_text=str):

        # Expected date looks like "May 14, 2025 - Site 027 is available"
        date_text = date_text.replace(",", "")
        date_list = date_text.split(" ")
        year = int(date_list[2])
        month = int(list(calendar.month_abbr).index(date_list[0]))
        day = int(date_list[1])

        return date(year, month, day)

class CampgroundReserver:

    def __init__(self, campground_url):

        # ============ Get Driver ===============

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        # Instantiate browser of choice
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(campground_url)

        # Default empty reservation
        self.reservation = None
        self.not_reservable = False

        # Enter in login credentials
        load_dotenv()
        self.username = os.environ.get("USERNAME", "Recreation.gov Username cannot be found")
        self.password = os.environ.get("PASSWORD", "Recreation.gov password cannot be found")

    def find_reservation(self, day_name=str, specific_date=date, skip_to_date=date):

        # If user inputted specific day, get the day number
        if day_name is not None:
            day_number = get_day_number(day_name)
        # Otherwise set the day number to None so it doesn't enter the condition below
        else:
            day_number = None

        # While we haven't found a reservation, and we still think that are reservable spots, loop through and find reservations
        while self.reservation is None and self.not_reservable is False:

            print("Find available dates....")
            self.wait = WebDriverWait(self.driver, 10)
            availability_tags = self.driver.find_elements(By.CLASS_NAME, "rec-availability-date")
            # availability_tags = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "rec-availability-date")))
            # Tried only searching for "A" tags and it sped things up at first but slowed it down later
            # availability_tags = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//button[contains(text(), 'A')]")))

            # What happens if there are no "A" or "NR" tags..
            try:

                # Loop through available dates and determine if there is an available ("A") and it is a Friday
                for tag in availability_tags:

                    reservation_date_string = tag.get_attribute('aria-label')
                    reservation_date = get_date(reservation_date_string)

                    # Skip to the date passed into the method (i.e. don't camp in cold weather)
                    if reservation_date < skip_to_date:
                        print(f"Skip to {skip_to_date} for maximum fun")
                        break

                    # If a specific date is requested and is available, reserve it
                    elif tag.text == "A" and reservation_date == specific_date:
                        print(f"There is an available reservation for {specific_date}!!!")
                        self.reservation = tag
                        break

                    # Otherwise, check to see if a specific weekday is available (i.e. Monday = 0, Friday = 4)
                    elif tag.text == "A" and reservation_date.weekday() == day_number:
                        print(f"There is an available reservation for the {day_number}!!!")
                        self.reservation = tag
                        break

            # If there are no "A" tags, check to see if there are any "NR" tags (Not Reservable)
            except TimeoutException:
                print("TimeoutException while trying to find 'A' tags.")
                try:
                    print("Try to find 'NR' tags...")
                    # Find "NR" tags
                    self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//button[contains(text(), 'NR')]")))

                except TimeoutException:
                    print("TimeoutException while trying to find 'NR' tags. Try searching for next week.")

                else:
                    print("There are no A tags and we have hit the 'Not Reservable' days. Better luck next time.")
                    self.not_reservable = True
                    break

            next_5_days_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.forward")))
            next_5_days_button.click()

    def reserve_campsite(self):

        print("Adding campsite to cart...")
        # Click on reservation
        self.reservation.click()
        # Click on add to cart button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.availability-page-book-now-button-tracker")))
        # add_to_cart_button = self.driver.find_element(By.CSS_SELECTOR, value="button.availability-page-book-now-button-tracker")
        add_to_cart_button.click()

        print("Signing in...")
        # Enter in username
        username_input = self.driver.find_element(By.CSS_SELECTOR, value="input#email")
        username_input.send_keys(self.username)
        # Enter in password
        password_input = self.driver.find_element(By.CSS_SELECTOR, value="input#rec-acct-sign-in-password")
        password_input.send_keys(self.password)
        # Click Sign In
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR, value="button.rec-acct-sign-in-btn")
        sign_in_button.click()

        print(f"Signed in...")
        # Perform the remaining steps manually

