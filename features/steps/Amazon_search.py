from behave import given, when, then
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


#@given('Open Amazon homepage')
#def open_amazon_homepage(context):
#    context.driver.get("https://www.amazon.com")


@when('Input coffee into amazon search')
def search_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')


#@when('Click on Amazon search icon')
#def click_search_icon(context):
#    context.driver.find_element(By.CSS_SELECTOR, 'input#nav-search-submit-button.nav-input.nav-progressive-attribute')


#@then('Verify "coffee" text is shown')
#def verify_text_shown(context):
#    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
#    expected_result = '"coffee"'
#    assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result}'
