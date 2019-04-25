from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

SEARCH_WORLD = "dress"

# init driver
driver = webdriver.Chrome('drivers/chromedriver')

# open the url
driver.get('https://www.google.com/')
driver.maximize_window()

# search = driver.find_element(By.NAME, 'q')
# search = driver.find_element_by_xpath("//input[@name='q']") - not stable code, xpath can changes
search = driver.find_element(By.XPATH, "//input[@name='q']") # recommend to use
search.clear()
search.send_keys(SEARCH_WORLD)

# wait for 4 sec from time library from Python, better to use wait from Selenium later
sleep(4)

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
# collect all text from block
assert SEARCH_WORLD in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
# print(driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text)
assert SEARCH_WORLD in driver.find_element(By.XPATH, "//div[@class='g']").text
print(driver.find_element(By.XPATH, "//div[@class='g']").text)

driver.quit()
