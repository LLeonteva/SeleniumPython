from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


AMAZON_LOGO = (By.CSS_SELECTOR, "a.a-link-nav-icon")
CREATE_ACCOUNT_LOGO = (By.CSS_SELECTOR, "h1.a-spacing-small")
YOUR_NAME_FIELD = (By.ID, "ap_customer_name")
E_MAIL_FIELD = (By.ID, "ap_email")
PASSWORD_FIELD = (By.ID, "ap_password")
RE_ENTER_PASSWORD_FIELD = (By.ID, "ap_password_check")
CREATE_ACCOUNT_BTN = (By.ID, "continue")
COU_LINK = (By.CSS_SELECTOR, "a[href*='ap_desktop_footer_cou']")
PRIVACY_LINK = (By.CSS_SELECTOR, "a[href*='privacy_notice']")
SIGN_IN_LINK = (By.CSS_SELECTOR, "a.a-link-emphasis")


@then("Sign up page is opened")
def verify_sign_up_opened(context):
    """
    Searches for unique elements of Sign Up page to verify it is opened
    """
    context.driver.find_element(*AMAZON_LOGO)
    context.driver.find_element(*CREATE_ACCOUNT_LOGO)
    context.driver.find_element(*YOUR_NAME_FIELD)
    context.driver.find_element(*E_MAIL_FIELD)
    context.driver.find_element(*PASSWORD_FIELD)
    context.driver.find_element(*RE_ENTER_PASSWORD_FIELD)
    context.driver.find_element(*CREATE_ACCOUNT_BTN)
    context.driver.find_element(*COU_LINK)
    context.driver.find_element(*PRIVACY_LINK)
    context.driver.find_element(*SIGN_IN_LINK)