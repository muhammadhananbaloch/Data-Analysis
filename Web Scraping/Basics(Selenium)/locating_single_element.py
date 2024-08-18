from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = 'laptop'
driver.get(f"https://www.amazon.com/s?k={query}&ref=cs_503_search")
time.sleep(15)
elem =  driver.find_element(By.CLASS_NAME, 'puis-card-container')
# print(elem.text)
print(elem.get_attribute('outerHTML'))

driver.close()