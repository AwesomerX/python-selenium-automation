from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResults
'''
from pages.hw7_q1_main_page import Q1MainPage
from pages.hw7_q1_header import Q1Header
from pages.hw7_q1_signin_page import Q1SignInPage
from pages.hw7_q2_main_page import Q2MainPage
from pages.hw7_q2_header import Q2Header
from pages.hw7_q2_cart import Q2Cart

'''
class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResults(self.driver)
'''     self.hw7_main_page = Q1MainPage(self.driver)
        self.hw7_header = Q1Header(self.driver)
        self.hw7_signin_page = Q1SignInPage(self.driver)
        self.hw7_main_page = Q2MainPage(self.driver)
        self.hw7_header = Q2Header(self.driver)
        self.hw7_cart = Q2Cart(self.driver)
'''
