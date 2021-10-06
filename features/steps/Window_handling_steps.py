from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, "[href*='https://www.amazon.com/privacy']")
PRIVACY_NOTICE = (By.CSS_SELECTOR, "div.help-content h1")


@given('Open Amazon T&C page')
def open_amazon_homepage(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original window')
def store_current_window(context):
    context.original_window = context.driver.current_window_handle
    print(f'Current window handle: {context.original_window}')


@when('Click on Amazon Privacy Notice link')
def click_privacy_link(context):
    context.driver.find_element(*PRIVACY_NOTICE_LINK).click()
    context.driver.wait.until(EC.new_window_is_opened)


@when('Switch to new window')
def switch_window(context):
    all_window_handles = context.driver.window_handles
    print(all_window_handles)
    context.driver.switch_to.window(all_window_handles[1])
    print('Current window handle (after switch) {context.driver.current_window_handle}')


@then('Verify Amazon Privacy Notice page is open')
def verify_privacy_notice_page_open(context):
    assert 'https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ' in context.driver.current_url,\
    f'Error, https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ not opened'


@then('User can close new window and return to original window')
def close_window_and_switch_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.driver.window_handles[0])

