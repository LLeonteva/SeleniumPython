from selenium.webdriver.common.by import By
from behave import given, when, then


TRY_PRIME_BTN = (By.XPATH, "//input[@class='prime-cta-signup-button-input']")
PRIME_LOGO = (By.ID, "prime-hero-header")
BENEFITS_CARD = (By.CSS_SELECTOR, "div.card-category")


@then("Amazon Prime page is opened")
def verify_on_page_prime(context):
    """
    Searches for unique elements of Prime page to verify it is opened
    """
    context.driver.find_element(*TRY_PRIME_BTN)
    context.driver.find_element(*PRIME_LOGO)


@then("Verify 4 benefits cards are displayed on Prime page")
def verify_benefits_card_presented(context):
    cards = context.driver.find_elements(*BENEFITS_CARD)
    print("Printing cards:", cards)
    actual_cards = len(cards)
    print("Actual amount of cards: ", actual_cards)
    expected_cards = 4
    assert actual_cards == expected_cards, \
        "Expected benefits cards '{}', but got '{}' ".format(expected_cards, actual_cards)