from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SIGN_IN_BTN = (By.ID, "nav-al-signin")


@when("Click on Account&Lists SignIn btn")
def click_sign_in_btn(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN))
    context.driver.find_element(*SIGN_IN_BTN).click()
