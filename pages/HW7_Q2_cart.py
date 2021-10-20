from pages.base_page import Page
from selenium.webdriver.common.by import By


class Q2Cart(Page):

    CART_PAGE = (By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty")

    def verify_cart_page_displayed(self):
        self.click(*self.CART_PAGE)