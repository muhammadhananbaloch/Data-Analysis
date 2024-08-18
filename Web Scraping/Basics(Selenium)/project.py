from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = 'laptop'
file = 0
for i in range(1, 20):
    driver.get(f"https://www.amazon.com/s?k={query}&page={i}&crid=1SGJ8PCYMRDRO&qid=1723988433&ref=sr_pg_{i}")
    # time.sleep(5)

    elems =  driver.find_elements(By.CLASS_NAME, 'puis-card-container')
    print(f"{len(elems)} elements found")  
    for elem in elems:
        data = elem.get_attribute('outerHTML')
        with open(f'data/{query}_{file}.html', 'w', encoding='utf-8') as f:
            f.write(data)
            file += 1
    
    time.sleep(2)
driver.close()