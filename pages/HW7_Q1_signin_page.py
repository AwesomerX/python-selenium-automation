from selenium.webdriver.common.by import By
from pages.base_page import Page


class Q1SignInPage(Page):

    SIGN_IN = (By.CSS_SELECTOR, 'h1.a-spacing-small')

    def verify_sign_in_page(self):
        self.click(*self.SIGN_IN)
