from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Instantiate browser of choice
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, value="//*[@id='articlecount']/ul/li[2]/a[1]")
print(article_count.text)

# article_count.click()

# Find by text between anchor tag
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the search input by name
search = driver.find_element(By.NAME, value="search")
# Send keyboard imput
# search.send_keys("Python")
# Keys class has a bunch of constants that are keys on the keyboard
# search.send_keys(Keys.ENTER)

# driver.quit()