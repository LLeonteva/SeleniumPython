from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

LEARN_MORE_LNK = (By.CSS_SELECTOR, "div.icp-helplink")


@when("Click on 'Learn more' link")
def click_learn_more_lnk(context):
    context.driver.find_element(*LEARN_MORE_LNK).click()