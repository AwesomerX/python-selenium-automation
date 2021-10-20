# generic script for connecting Page object pattern with behave

from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, '(whatever locator goes here)')
    SEARCH_ICON = (By.ID, '(whatever locator goes here)')

    def input_search(self):
        # 'coffee' is a placeholder here for any text
        self.input_text('coffee', *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)
