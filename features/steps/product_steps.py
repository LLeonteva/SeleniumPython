from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

ADD_CART_BTN = (By.CSS_SELECTOR, "input#add-to-cart-button")
ADDED_TO_CARD_LABEL = (By.CSS_SELECTOR, "div#huc-v2-order-row-confirm-text")
CART_COUNT = (By.CSS_SELECTOR, "span#nav-cart-count")

COLOR_OPTIONS = (By.CSS_SELECTOR, 'div#variation_color_name li')
COLOR = [By.CSS_SELECTOR, "div#variation_color_name li[title='Click to select {}']"]
SELECTED_COLOR = (By.CSS_SELECTOR, 'div#variation_color_name span.selection')


@when("Click Add to cart button")
def add_to_cart(context):
    context.driver.find_element(*ADD_CART_BTN).click()


@then("Label 'Added to card' is present")
def verify_label_added_to_card(context):
    context.driver.find_element(*ADDED_TO_CARD_LABEL)


@then("Item has been added to the cart")
def verify_item_added(context):
    count = context.driver.find_element(*CART_COUNT).text
    assert int(count) == 1, "Expected item is 1, but actual items: '{}' ".format(count)


def create_locator_color(color) -> list:
    """

    :param color: this is a string to put into COLOR locator
    :return: full locator searching for a certain color
    """
    # print(color)
    return [COLOR[0], COLOR[1].format(color)]


@when("Click on color {color}")
def click_color(context, color):
    locator = create_locator_color(color)
    context.driver.find_element(*locator).click()


@then("Verify color is updated to {color_expected}")
def verify_color_updated(context, color_expected):
    color_actual = context.driver.find_element(*SELECTED_COLOR).text
    # print(color_actual)
    assert color_expected == color_actual, "Expected color is '{}', but got: '{}' ".format(color_expected, color_actual)


@then("Verify user can select dress colors")
def verify_color_selections(context):
    expected_colors = ['Black', 'Emerald', 'Navy', 'Winter White']
    color_webelements = context.driver.find_elements(*COLOR_OPTIONS)
    print('\n\nWebElements:\n', color_webelements)

    for x in range(len(color_webelements)):
        print('\nWebElement:', color_webelements[x])
        color_webelements[x].click()

        actual_color_text = context.driver.find_element(*SELECTED_COLOR).text
        print("Actual color: ", actual_color_text)

        print("Expected color: ", expected_colors[x])
        assert actual_color_text == expected_colors[x], \
            "Expected color {}, but got {} ".format(expected_colors[x], actual_color_text)


# @then("Verify user can select through colors")
# def verify_color_selections(context):
#     expected_colors = ['Black', 'Emerald', 'Navy', 'Winter White']
#     colors = context.driver.find_elements(*COLOR_OPTIONS)
#     for color in colors:
#         color.click()
#         assert context.driver.find_element(*SELECTED_COLOR).text == expected_colors[colors.index(color)]

@then("Verify user can select backpack colors")
def verify_color_selections_backpack(context):
    expected_colors = ["Black", "Blue", "Wine Red"]
    color_webelements = context.driver.find_elements(*COLOR_OPTIONS)

    for x in range(len(color_webelements)):
        color_webelements[x].click()

        actual_color_text = context.driver.find_element(*SELECTED_COLOR).text
        print("Actual backpack color: ", actual_color_text)

        print("Expected backpack color: ", expected_colors[x])
        assert actual_color_text == expected_colors[x], \
            "Expected backpack color {}, but got {}".format(expected_colors[x], actual_color_text)

