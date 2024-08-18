from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = 'laptop'
for i in range(1, 20):
    driver.get(f"https://www.amazon.com/s?k={query}&page={i}&crid=1X3DRMOPGQL66&qid=1723971457&sprefix=lap%2Caps%2C485&ref=sr_pg_2")
    time.sleep(2)

    elems =  driver.find_elements(By.CLASS_NAME, 'puis-card-container')
    print(f"{len(elems)} elements found")  
    for elem in elems:
        print(elem.text)
    driver.close()