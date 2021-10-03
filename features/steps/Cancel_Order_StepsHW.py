from behave import given, when, then
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

@given('Open Amazon Help page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input Cancel order into Amazon Help Search')
def verify_cancel_order_input(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order', Keys.ENTER)

sleep(2)

@then('Verify Cancel Items or Orders text is displayed')
def verify_cancel_order_text(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
    expected_result = 'Cancel Items or Orders'
    assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result}'

