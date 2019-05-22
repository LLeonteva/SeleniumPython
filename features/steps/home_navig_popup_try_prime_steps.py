from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


TRY_PRIME_BTN = (By.CSS_SELECTOR, "div.prime-button-try")


@when("Click on 'Try Prime' btn")
def click_try_prime_btn(context):
    context.driver.find_element(*TRY_PRIME_BTN).click()