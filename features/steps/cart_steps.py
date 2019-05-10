from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


CARD_EMPTY_HEADER = (By.CSS_SELECTOR, "div.a-row.sc-cart-header")


@then("Verify '{expected_text}' is presented")
def verify_card_empty_header_presented(context, expected_text):
    context.driver.wait.until(EC.presence_of_element_located(CARD_EMPTY_HEADER))
    actual_text = context.driver.find_element(*CARD_EMPTY_HEADER).text
    assert expected_text == actual_text