from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR,  "#variation_color_name .selection")
product_id = 'B07HD226RC'


@given('Open Amazon product B07HD226RC page')
def open_product(context):
    context.driver.get('https://www.amazon.com/B07HD226RC/')
#    context.driver.wait.until(EC.element_to_be_clickable(f'https://www.amazon.com/B07HD226RC/'))
    context.driver.refresh()

@then('Verify user can click through colors')
def verify_can_click_through_colors(context):
    expected_colors = ['Black Split/Orange' 'Black/White Split' 'Black/White/Black' 'Grey/Carbon' 'Griffin/White']
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for i in range(len(colors)):
        colors[i].click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        assert current_color == expected_colors[i], f'Error expected {expected_colors[i]} did not match {current_color}'


#works