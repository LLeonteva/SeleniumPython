from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# =============================== LOCATORS ================================================
# AMAZON_LOGO = (By.XPATH, "//i[@class='a-icon a-icon-logo']")
# AMAZON_LOGO = (By.XPATH, "//a[@href='/ref=ap_frn_logo']")
AMAZON_LOGO = (By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

# SIGN_IN_LOGO = (By.XPATH, "//h1[@class='a-spacing-small']")
SIGN_IN_LOGO = (By.CSS_SELECTOR, "h1.a-spacing-small")

EMAIL_FIELD = (By.ID, 'ap_email')
# EMAIL_FIELD = (By.CSS_SELECTOR, "input#ap_email")
# EMAIL_FIELD = (By.XPATH, "//input[@id='ap_email']")

PASSWORD_FIELD = (By.ID, 'ap_password')
# PASSWORD_FIELD = (By.CSS_SELECTOR, "input#ap_password")
# PASSWORD_FIELD = (By.XPATH, "//input[@id='ap_password']")

FORGOT_PASSWORD_LINK = (By.ID, 'auth-fpp-link-bottom')
# FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a#auth-fpp-link-bottom")

SIGN_IN_BTN = (By.ID, 'signInSubmit')
# SIGN_IN_BTN = (By.CSS_SELECTOR, "input#signInSubmit")

# KEEP_SIGNED_CHECKBOX = (By.NAME, 'rememberMe')
KEEP_SIGNED_CHECKBOX = (By.CSS_SELECTOR, "div.a-checkbox")
# KEEP_SIGNED_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")

DETAILS_LINK = (By.ID, "remember_me_learn_more_link")
# DETAILS_LINK = (By.CSS_SELECTOR, "a#remember_me_learn_more_link")

CREAT_ACCOUNT_LINK = (By.ID, "createAccountSubmit")
# CREAT_ACCOUNT_LINK = (By.CSS_SELECTOR, "a#createAccountSubmit")

# COU_LINK = (By.XPATH, "//a[contains(@href,'ap_desktop_footer_cou')]")
COU_LINK = (By.CSS_SELECTOR, "[href*='ap_desktop_footer_cou']")
# COU_LINK = (By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')")

# PRIVACY_NOTICE_LINK = (By.XPATH, "//a[contains(@href,'ap_desktop_footer_privacy_notice')]")
PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, "a[href*='ap_desktop_footer_privacy_notice']")

KEEP_SIGNED_CHECKBOX = (By.CSS_SELECTOR, "input[name='rememberMe']")
DETAILS_LINK = (By.ID, 'remember_me_learn_more_link')

# =============================== LOCATORS ================================================

@then('Sign in page is opened')
def verify_on_sign_in(context):
    """
    Searches for unique elements of Sign In page to verify it is opened
    """
    # mandatory
    context.driver.find_element(*EMAIL_FIELD)
    # context.driver.find_element(*EMAIL_FIELD).send_keys("checking this field")
    context.driver.find_element(*PASSWORD_FIELD)
    # context.driver.find_element(*PASSWORD_FIELD).send_keys("checking PW field")
    # in case
    context.driver.find_element(*AMAZON_LOGO)
    context.driver.find_element(*SIGN_IN_LOGO)
    context.driver.find_element(*FORGOT_PASSWORD_LINK)
    context.driver.find_element(*SIGN_IN_BTN)
    context.driver.find_element(*KEEP_SIGNED_CHECKBOX)
    context.driver.find_element(*DETAILS_LINK)
    context.driver.find_element(*CREAT_ACCOUNT_LINK)
    context.driver.find_element(*COU_LINK)
    context.driver.find_element(*PRIVACY_NOTICE_LINK)


@when("Click on 'Create your Amazon Account' button")
def click_create_acc_btn(context):
    context.driver.wait.until(EC.element_to_be_clickable(CREAT_ACCOUNT_LINK))
    context.driver.find_element(*CREAT_ACCOUNT_LINK).click()


@when("Click on Forgot Password link")
def click_forgot_pw_lnk(context):
    context.driver.find_element(*FORGOT_PASSWORD_LINK).click()