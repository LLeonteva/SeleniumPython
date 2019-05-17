from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

ALL_PRODUCTS = (By.CSS_SELECTOR, "div.a-text-center li.s-result-item")
PRODUCT_NAME = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name.a-text-bold')


@then("Verify every product on the page has 'Regular' text")
def verify_regular_text_presented(context):
    products = context.driver.find_elements(*ALL_PRODUCTS)
    print("\nProducts: ", products)

    for x in range(len(products)-1):
        actual_text = products[x].text
        print('\nChecking:', actual_text)
        assert 'Regular' in actual_text, "Expected 'Regular $' to be in product test, but got {}".format(actual_text)
"""
    for product in products:
        print('\nChecking:', product.text)
        assert 'Regular ' in product.text, "Expected 'Regular $' to be in product test, but got {}".format(product.text)

error: the last webelement id add and don't have $ and name
Step failed:  <then "Every product on the page has 'Regular' text">
Assertion Failed: Expected 'Regular $' to be in product test, but got Hundreds more in store. Look for the yellow signs.
Learn more

Prev. step failed. Rest part of scenario is skipped

"""


@then("Verify every product on the page has name")
def verify_product_name(context):
    """
    Finds ALL Product elements and searches for a name element inside each product element

    Example:
    # Get a product's element, it has html =>
    product1_element = context.driver.find_elements(*ALL_PRODUCTS)[1]
    print(product1_element)
    html = product1_element.get_attribute('innerHTML')
    print(html)
    # Search inside product1_element:
    name = product1_element.find_element(*PRODUCT_NAME)
    print('\n', name.text)

    """
    products = context.driver.find_elements(*ALL_PRODUCTS)
    for x in range(len(products)-1):
        print('\nProduct element: ', products[x])
        products[x].find_element(*PRODUCT_NAME)
