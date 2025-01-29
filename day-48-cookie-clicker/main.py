from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ========================= Helper Methods ===============================

def get_points(name):
    formatted_points = int(name.text.split()[-1].replace(",", ""))
    return formatted_points

def get_name(name):
    formatted_name = name.text.split(" - ")[0]
    return formatted_name

# ========================= Setup Selenium Driver ===============================

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Instantiate browser of choice
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# ========================= Program Start ===============================

# Set default times
timeout_start = time.time()
last_checked_time = timeout_start

# Get the cookie element
cookie = driver.find_element(By.ID, value="cookie")

# For 5 minutes (60 seconds x 5) loop through and click on cookie
while time.time() < timeout_start + 300:

    # Click cookie to get points
    cookie.click()

    # Every 5 seconds, buy the most expensive item from the store
    if time.time() > last_checked_time + 5:

        # Get updated money amount
        money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))
        print(f"Every 5 seconds buy something with {money} points")

        # Find all the items that are available in the store
        store_list = driver.find_elements(By.CSS_SELECTOR, value="#store b")

        # Set default values
        most_expensive_points = 0
        most_expensive_item = None

        # Loop through every item in the store
        for item in store_list:

            # If the item is not empty
            if item.text:
                # Get the item points and name from the element text
                item_points = get_points(item)
                item_name = get_name(item)
                print(f"Current store item {item_name} costs {item_points} points")

                # Find the store item in which you have enough money to buy, and is the most expensive
                if money >= item_points >= most_expensive_points:
                    most_expensive_points = item_points
                    most_expensive_item = item_name
                    print(f"Setting new expensive item: {most_expensive_item} that costs {most_expensive_points} points")

        # Using the most expensive item, find the store item element
        most_expensive_element = driver.find_element(By.CSS_SELECTOR, value=f"[id='buy{most_expensive_item}'] b")
        print(f"Store item to buy: {most_expensive_element.text}")
        # Click on element to purchase from store
        most_expensive_element.click()

        # Update the last checked time to current time so that we can reset the 5 second timer
        last_checked_time = time.time()

# Once while loop is exited (after 5 minutes) print out the number of cookies/second stored on the webpage
print(driver.find_element(By.ID, value="cps").text)
driver.quit()