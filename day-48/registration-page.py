from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Instantiate browser of choice
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
sign_up_button = driver.find_element(By.CSS_SELECTOR, value="form button")

first_name.send_keys("Bilbo")
last_name.send_keys("Baggins")
email.send_keys("bilbo@yahoo.com")
sign_up_button.send_keys(Keys.ENTER)

# driver.quit()