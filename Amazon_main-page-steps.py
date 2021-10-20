from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


# init driver

driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)
# driver.implicitly_wait(10)


# wait(4)
# sleep(4)



# Given statements

@given('Open Amazon homepage')
def open_amazon_homepage(context):
    context.app.main_page.open_main_page()

 # When statements


@when('Store product name')
def get_product_name(context):
    context.current_product_name = context.driver.find_elements(*PRODUCT_NAME)
    print(f'Current product: {context.current_product_name}')

@when('Click Cart Icon')
def click_cart_icon(context):
    context.app.q2header.click_cart_icon()

# Then statements

@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(*CART_COUNT).text
    assert actual_count == expected_count, f'Expected {expected_count} item(s), but got {actual_count}'


@then('Verify cart has correct product')
def verify_product_name(context):
    cart_product_name = context.driver.find_element(*PRODUCT_NAME)
    print(f'Product name in the cart: {cart_product_name}')
    assert cart_product_name == context.current_product_name, \
        f'Expected {context.current_product_name}, but got {cart_product_name}'


