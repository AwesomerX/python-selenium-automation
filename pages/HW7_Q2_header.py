from pages.base_page import Page
from selenium.webdriver.common.by import By


class Q2Header(Page):

    CART_ICON = (By.ID, 'nav-cart')

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

