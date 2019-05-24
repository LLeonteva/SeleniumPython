from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


EMAIL_FIELD = (By.ID, "ap_email")
CONTINUE_BTN = (By.ID, "continue")
ERROR_MSG = (By.CSS_SELECTOR, "h4.a-alert-heading")


@when("Enter invalid email {invalid_email}")
def enter_invalid_pw(context, invalid_email):
    email = context.driver.find_element(*EMAIL_FIELD)
    email.clear()
    email.send_keys(invalid_email)


@when("Click on Continue button")
def click_continue_btn(context):
    context.driver.find_element(*CONTINUE_BTN).click()


@then("Verify error message {expected_text} is presented")
def verify_text_presented(context, expected_text):
    context.driver.wait.until(EC.presence_of_element_located(ERROR_MSG))
    actual_text = context.driver.find_element(*ERROR_MSG).text
    # print("actual_text is: " + actual_text)
    assert expected_text == actual_text, \
        "Expected_text is: {}, but the actual_text is: {}".format(expected_text, actual_text)