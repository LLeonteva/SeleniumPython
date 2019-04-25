from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# =============================== LOCATORS ================================================
AMAZON_LOGO = (By.XPATH, "//i[@class='a-icon a-icon-logo']")
# AMAZON_LOGO = (By.XPATH, "//a[@href='/ref=ap_frn_logo']")
SIGN_IN_LOGO = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL_FIELD = (By.ID, 'ap_email')
# EMAIL_FIELD = (By.XPATH, "//input[@id='ap_email']")
PASSWORD_FIELD = (By.ID, 'ap_password')
# PASSWORD_FIELD = (By.XPATH, "//input[@id='ap_password']")
FORGOT_PASSWORD_LINK = (By.ID, 'auth-fpp-link-bottom')
SIGN_IN_BTN = (By.ID, 'signInSubmit')
KEEP_SIGNED_CHECKBOX = (By.NAME, 'rememberMe')
# KEEP_SIGNED_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
DETAILS_LINK = (By.ID, "remember_me_learn_more_link")
CREAT_ACCOUNT_LINK = (By.ID, "createAccountSubmit")
COU_LINK = (By.XPATH, "//a[contains(@href,'ap_desktop_footer_cou')]")
# COU_LINK = (By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')")
PRIVACY_NOTICE_LINK = (By.XPATH, "//a[contains(@href,'ap_desktop_footer_privacy_notice')]")
# =============================== LOCATORS ================================================

@then('Sign in page is opened')
def verify_on_sign_in(context):
    """
    Searches for unique elements of Sign In page to verify it is opened
    """
    context.driver.find_element(*EMAIL_FIELD)
    context.driver.find_element(*PASSWORD_FIELD)