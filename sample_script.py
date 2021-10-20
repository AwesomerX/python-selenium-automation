from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# init driver
service = Service('C:/Users/Chopp/Automation/python-selenium-automation/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)
#driver.implicitly_wait(10)


# open the url
driver.get('https://www.google.com/')


search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')


# wait for 4 sec
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Error, Search button not clickable')
# sleep(4)


# click search
driver.find_element(By.NAME, 'btnK').click()


# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()

