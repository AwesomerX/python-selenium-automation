from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART_COUNT = (By.XPATH, "//span[@id='nav-cart-count']")
PRODUCT_NAME = (By.XPATH, "//span[@class='a-truncate-cut']")
PRODUCT_PRICE = (By.XPATH,  "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")


@given('Open Amazon homepage')
def open_amazon_hp(context):
    context.driver.get('https://www.amazon.com/')


@when('Input coffee mug into amazon search')
def search_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee mug', Keys.ENTER)


sleep(2)



#@when('Click on Amazon search icon')
#def click_search_icon(context):
#    context.driver.find_element(By.CSS_SELECTOR, 'input#nav-search-submit-button.nav-input.nav-progressive-attribute')



@when('Click on first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).send_keys(Keys.ENTER)


@when('Store product name')
def get_product_name(context):
    context.current_product_name = context.driver.find_elements(*PRODUCT_NAME)
    print(f'Current product: {context.current_product_name}')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(1)


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


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
