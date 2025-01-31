from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import os
from dotenv import load_dotenv

class InternetSpeedTwitterBot:

    def __init__(self):

        # ==================== Set up .env variables =====================

        load_dotenv()
        self.username = os.environ.get("USERNAME", "Twitter Username cannot be found")
        self.password = os.environ.get("PASSWORD", "Email password cannot be found")
        self.typical_up = os.environ.get("TYPICAL_UP", "Typical Up speed cannot be found")
        self.typical_down = os.environ.get("TYPICAL_DOWN", "Typical Down speed cannot be found")
        # ==================== Set up Driver =====================

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        URL = "https://www.speedtest.net/"

        # Instantiate browser of choice
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(URL)
        print("Driver collected")


    def get_internet_speed(self):
        print(f"Getting Internet Speeds...")
        go_button = self.driver.find_element(By.CLASS_NAME, value="js-start-test")
        print(f"Go Button: {go_button}")
        print(f"Go Button Text: {go_button.text}")
        go_button.click()
        print(f"Clicked Go button....")
        self.driver.implicitly_wait(20)
        print(f"After button click wait for element to be clickable")
        download_speed = self.driver.find_element(By.CLASS_NAME, "result-data-large").text
        # result = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(By.CLASS_NAME, "result-data-large"))
        print(f"This is your download speed: {download_speed}")



    def tweet_at_provider(self):
        pass


