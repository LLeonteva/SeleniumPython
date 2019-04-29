from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

ADD_CART_BTN = (By.CSS_SELECTOR, "input#add-to-cart-button")
ADDED_TO_CARD_LABEL = (By.CSS_SELECTOR, "div#huc-v2-order-row-confirm-text")
CART_COUNT = (By.CSS_SELECTOR, "span#nav-cart-count")


@when("Click Add to cart button")
def add_to_cart(context):
    context.driver.find_element(*ADD_CART_BTN).click()


@then("Label 'Added to card' is present")
def verify_label_added_to_card(context):
    context.driver.find_element(*ADDED_TO_CARD_LABEL)


@then("Item has been added to the cart")
def verify_item_added(context):
    count = context.driver.find_element(*CART_COUNT).text
    assert int(count) == 1, "Expected item is 1, but actual items: '{}' ".format(count)