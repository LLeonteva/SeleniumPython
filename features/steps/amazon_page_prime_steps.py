from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


TRY_PRIME_BTN = (By.XPATH, "//input[@class='prime-cta-signup-button-input']")
PRIME_LOGO = (By.XPATH, "//div[@class='prime-header-logo']")


@then("Amazon Prime page is opened")
def verify_on_page_prime(context):
    """
    Searches for unique elements of Prime page to verify it is opened
    """
    context.driver.find_element(*TRY_PRIME_BTN)
    context.driver.find_element(*PRIME_LOGO)