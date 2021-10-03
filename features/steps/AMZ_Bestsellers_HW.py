from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BESTSELLERS_LINKS = (By.CSS_SELECTOR, '#zg_header li')


@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers')
    context.driver.refresh()

#sleep(3)


@then('Verify there are {expected_links} links')
def verify_links_count(context, expected_links):
    actual_links = context.driver.find_elements(*BESTSELLERS_LINKS)
    assert len(actual_links) == int(expected_links), f' Expected {expected_links} links, but got {actual_links}'







