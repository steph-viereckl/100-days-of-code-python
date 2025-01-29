from selenium import webdriver
from selenium.webdriver.common.by import By
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Instantiate browser of choice
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Magna-Tiles-100-Piece-Clear-Colors-Award-Winning/dp/B000CBSNRY?tag=googhydr-20&source=dsa&hvcampaign=toys&gclid=CjwKCAiAneK8BhAVEiwAoy2HYT-M1bWRyHTq2_XPg-U3TckLF_FtKoK6D69KSq_WfmiKSjQ6bAgJMxoCzT0QAvD_BwE")

# Locator strategies
# https://www.selenium.dev/documentation/webdriver/elements/locators/
dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
print(f"dollar: {dollar}")
print(f"cents: {cents}")

# Additional ways to search
# dollar = driver.find_element(By.NAME, value="name-here").text
# dollar = driver.find_element(By.ID, value="submit").size

# Find the a tag where the parent class is the documentation widget
# This is useful if you don't have an easily identifiable element
driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# XPath - locate element by a path
# html/body/div/div/ul/li/a> Inspect > copy >  xpath
driver.find_element(By.XPATH, value="//*[@id='productTitle']")

# There is also a plural find element
driver.find_elements(By.CSS_SELECTOR, "123")

# close active tab
# driver.close()
# quit entire browser
driver.quit()