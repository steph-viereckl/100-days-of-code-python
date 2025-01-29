from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Instantiate browser of choice
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.python.org/")

events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li")
# events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

event_dict = {}

for num in range(0, len(events)):
    pprint(events[num].text)
    event_dict[num] = {
        "time": events[num].text[0:10],
        "name": events[num].text[11:]
    }

print(event_dict)