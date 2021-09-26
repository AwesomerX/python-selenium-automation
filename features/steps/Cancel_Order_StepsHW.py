from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when


@given('Open Amazon Help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input Cancel order into amazon help search')
def search_amazon(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order')


@when('Click on Amazon Help Search icon')
def click_search(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys(Keys.ENTER)
