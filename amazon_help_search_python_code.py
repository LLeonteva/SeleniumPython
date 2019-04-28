# User can search for solutions of Cancelling an order on Amazon
from selenium import webdriver
from selenium.webdriver.common.by import By

HELP_SEARCH_LINK = (By.XPATH, "//a[contains(@href, 'ref_=nav_cs_help')]")
HELP_SEARCH_FIELD = (By.ID, "helpsearch")
HELP_SEARCH_GO = (By.ID, 'helpSearchSubmit')
SEARCH_RESULT_HEADER = (By.XPATH, "//div[@class='help-content']/h1")
SEARCH_TEXT = "Cancel order"
SEARCH_RESULT = "Cancel Items or Orders"

# init driver
driver = webdriver.Chrome('drivers/chromedriver')

# open the url
driver.get('https://www.amazon.com/')
driver.maximize_window()

# click Help link
driver.find_element(*HELP_SEARCH_LINK).click()

# search. input text
search = driver.find_element(*HELP_SEARCH_FIELD)
search.clear()
search.send_keys(SEARCH_TEXT)

# click Go
driver.find_element(*HELP_SEARCH_GO).click()

# verify search world in result
print(driver.find_element(*SEARCH_RESULT_HEADER).text)
assert SEARCH_RESULT in driver.find_element(*SEARCH_RESULT_HEADER).text

driver.quit()