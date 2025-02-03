from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

class GoogleFormBot():

    def __init__(self):

        # ==================== Set up .env variables =====================

        load_dotenv()
        GOOGLE_FORM_URL = os.environ.get("FORM_URL", "Google Form cannot be found")
        # ==================== Set up Driver =====================

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        # Instantiate browser of choice
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(GOOGLE_FORM_URL)

    def populate_form(self, listings):

        print("Populating form...")

        self.wait = WebDriverWait(self.driver, 10)

        for num in range(0, len(listings)):

            address_tag = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")))
            address_tag.send_keys(listings[num]["address"])

            price_tag = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")))
            price_tag.send_keys(listings[num]["price"])

            link_tag = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")))
            link_tag.send_keys(listings[num]["link"])

            submit_button = self.driver.find_element(By.CSS_SELECTOR, value=f"[aria-label='Submit']")
            submit_button.click()

            # If there are more listings, click on "Submit another response" link
            if num < len(listings) - 1:
                submit_another_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Submit another response')]")))
                submit_another_link.click()
            # Otherwise, end program
            else:
                print("All listings submitted. Have a great day!")


