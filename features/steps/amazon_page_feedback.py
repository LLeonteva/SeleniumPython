from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

SHARE_FEEDBACK_FORM = (By.CSS_SELECTOR, "h4#a-popover-header-4")

SHARE_FEEDBACK_FORM_X = (By.CSS_SELECTOR, "button[data-action=a-popover-close]")
SHARE_FEEDBACK_FORM_CANCEL_BTN = (By.CSS_SELECTOR, "span#da-feedback-cancel-button")


@then("Ad feedback form is opened")
def verify_feedback_form_present(context):
    context.driver.wait.until(EC.element_to_be_clickable(SHARE_FEEDBACK_FORM_CANCEL_BTN))
    context.driver.find_element(*SHARE_FEEDBACK_FORM_CANCEL_BTN).click()
    # 2nd way:
    # context.driver.wait.until(EC.visibility_of_element_located(SHARE_FEEDBACK_FORM))

