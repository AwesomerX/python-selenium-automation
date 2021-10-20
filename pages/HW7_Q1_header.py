from pages.base_page import Page
from selenium.webdriver.common.by import By


class Q1Header(Page):

    ORDERS_BUTTON = (By.XPATH, "//a[@id='nav-orders']")

    def click_orders_button(self):
        self.click(*self.ORDERS_BUTTON)
