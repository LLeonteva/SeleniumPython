from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


NAVIG_LINK_HELP = (By.XPATH, "//a[contains(@href, 'ref_=nav_cs_help')]")
NAVIG_LINK_ORDERS = (By.ID, "nav-orders")

HAMBURGER_MENU = (By.XPATH, "//i[@class='hm-icon nav-sprite']")
SHOP_BY_CATEGORY_HEADER = (By.XPATH, "//ul[@class='hmenu  hmenu-visible']/li[1]/div[@class='hmenu-item hmenu-title']")
HAMBURGER_MENU_X = (By.XPATH, "//div[@class='nav-sprite hmenu-close-icon']")
# LOGO_TRY_PRIME_LINK = (By.XPATH, "//a[@class='nav-sprite nav-logo-tagline nav-prime-try']")
LOGO_TRY_PRIME_LINK = (By.XPATH, "//div[@id='nav-logo']/a[contains(@href, 'prime')]")
AD_FEEDBACK_LINK = (By.CSS_SELECTOR, "span#ad-feedback-text-right-7")


@when("Click on Help navigation link")
def click_help_link(context):
    context.driver.find_element(*NAVIG_LINK_HELP).click()


@when("Click on Orders navigation link")
def click_orders_link(context):
    context.driver.find_element(*NAVIG_LINK_ORDERS).click()


@when("Click on Hamburger menu icon on the left")
def click_hamburger_menu(context):
    context.driver.find_element(*HAMBURGER_MENU).click()


@then("Verify ‘Shop by category’ text is present")
def verify_shop_by_category_header_present(context):
    context.driver.find_element(*SHOP_BY_CATEGORY_HEADER)


@when("Click on closing X of the side menu")
def click_x(context):
    context.driver.find_element(*HAMBURGER_MENU_X).click()
    context.driver.wait.until(EC.invisibility_of_element_located(HAMBURGER_MENU_X))


@when("Click on ‘Try Prime’ from Amazon logo")
def click_try_prime_link(context):
    context.driver.wait.until(EC.element_to_be_clickable(LOGO_TRY_PRIME_LINK))
    # context.driver.wait.until(EC.visibility_of_element_located(LOGO_TRY_PRIME_LINK)) # can use it - works
    context.driver.find_element(*LOGO_TRY_PRIME_LINK).click()


@when("Click on ‘Ad feedback’ link")
def click_on_ad_feedback_link(context):
    context.driver.wait.until(EC.element_to_be_clickable(AD_FEEDBACK_LINK))
    context.driver.find_element(*AD_FEEDBACK_LINK).click()




