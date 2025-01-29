import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import os
import dotenv
from dotenv import load_dotenv

# ==================== Set up .env variables =====================

load_dotenv()
EMAIL = os.environ.get("EMAIL", "From Email cannot be found")
PASSWORD = os.environ.get("PASSWORD", "Email password cannot be found")

# ==================== Set up Driver =====================

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://www.linkedin.com/jobs/search/?currentJobId=4136158094&geoId=103023809&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true"

# Instantiate browser of choice
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
# Need to make sure the "Sign In" Modal is loaded
print("Driver loaded, please wait....")
driver.implicitly_wait(20)
time.sleep(5)
# ==================== Click "Sign In" Button =====================

print("Clicking 'Sign In' button....")
# Having a lot of trouble with this button being available consistently
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='base-contextual-sign-in-modal']/div/section/div/div/div/div[2]/button"))).send_keys(Keys.ENTER)

# while button.is_displayed() is False:
#     time.sleep(10)
#     button = driver.find_element(By.CSS_SELECTOR, value=".sign-in-modal button")

# Adding another wait?
print("Sign In button clicked. Please wait while next page loads...")
driver.implicitly_wait(20)
time.sleep(5)

# ==================== Enter Credentials =====================
print("Entering in username and password....")

username = driver.find_element(By.XPATH, value="//*[@id='base-sign-in-modal_session_key']")
username.send_keys(EMAIL)

password = driver.find_element(By.XPATH, value="//*[@id='base-sign-in-modal_session_password']")
password.send_keys(PASSWORD)

sign_in_button = driver.find_element(By.XPATH, value="//*[@id='base-sign-in-modal']/div/section/div/div/form/div[2]/button")
sign_in_button.send_keys(Keys.ENTER)
print("Username and password entered. Loading next page...")

# ==================== Click "Save" on Job Postings =====================

time.sleep(5)
print(f"Finding jobs....")
job_list = driver.find_elements(By.CLASS_NAME, value="job-card-container--clickable")
# job_list = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "job-card-container--clickable")))
print(f"Found list of jobs.... count of {len(job_list)}")

for num in range(0,5):
    print(f"Clicking on current job posting: {job_list[num].text}")
    job_list[num].click()
    time.sleep(5)
    print(f"Finding Save button to click....")
    job_save_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-save-button")
    print(f"Found Save button. Clicking now...")
    job_save_button.click()
    print(f"Saved Job. Go to Next Job...")
#

print("All jobs saved! Closing program.")
driver.quit()


