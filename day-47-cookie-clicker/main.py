from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def format_points(points):
    formatted_points = int(points.text.split()[-1].replace(",", ""))
    return formatted_points

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Instantiate browser of choice
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

timeout_start = time.time()
last_checked_time = timeout_start

# For 5 minutes do this
while time.time() < timeout_start + 30:

    # Click cookie to get points
    cookie.click()

    # Every 5 seconds, reset the last checked time
    if time.time() > last_checked_time + 5:

        money = int(driver.find_element(By.ID, value="money").text)

        print(f"Every 5 seconds buy something with {money} points")
        last_checked_time = time.time()

        cursor_price = format_points(driver.find_element(By.CSS_SELECTOR, value="#buyCursor b"))
        grandma_price = format_points(driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b"))
        factory_price = format_points(driver.find_element(By.CSS_SELECTOR, value="#buyFactory b"))
        mine_price = format_points(driver.find_element(By.CSS_SELECTOR, value="#buyMine b"))
        shipment_price = format_points(driver.find_element(By.CSS_SELECTOR, value="#buyShipment b"))
        # If you have a space in your id, you can format it like this
        alchemy_lab_price = format_points(driver.find_element(By.CSS_SELECTOR, value="[id='buyAlchemy lab'] b"))
        portal_price = format_points(driver.find_element(By.CSS_SELECTOR, value="#buyPortal b"))
        time_machine_price = format_points(driver.find_element(By.CSS_SELECTOR, value="[id='buyTime machine'] b"))

        if money >= time_machine_price:
            time_machine = driver.find_element(By.ID, value="buyTime machine")
            time_machine.click()
        if money >= portal_price:
            portal = driver.find_element(By.ID, value="buyPortal")
            portal.click()
        elif money >= alchemy_lab_price:
            alchemy_lab = driver.find_element(By.ID, value="buyAlchemy Lab")
            alchemy_lab.click()
        elif money >= shipment_price:
            shipment = driver.find_element(By.ID, value="buyShipment")
            shipment.click()
        elif money >= mine_price:
            mine = driver.find_element(By.ID, value="buyMine")
            mine.click()
        elif money >= factory_price:
            factory = driver.find_element(By.ID, value="buyFactory")
            factory.click()
        elif money >= grandma_price:
            grandma = driver.find_element(By.ID, value="buyGrandma")
            grandma.click()
        elif money >= cursor_price:
            cursor = driver.find_element(By.ID, value="buyCursor")
            cursor.click()

print(driver.find_element(By.ID, value="cps").text)
driver.quit()