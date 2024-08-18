from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
import json

driver = webdriver.Chrome()     

query = 'moniter'  # The query to search for
file = 1
for i in range(1, 5):
    try:
        driver.get(f"https://www.walmart.com/search?q={query}&page={i}")  # Open the website  
        # time.sleep(10)  # Wait for the page to load
        script_tags = driver.find_element(By.ID, '__NEXT_DATA__') 
        data = script_tags.get_attribute('innerHTML')  # Get the data from the script tag
        json_data = json.loads(data)  # Load the data into a json object 
        with open(f'Data/{query}_{i}.json', 'w') as f:
            f.write(json.dumps(json_data, indent=4))  # Convert dict to string and write to file
            file += 1   
    except Exception as e:
        print(e)
time.sleep(2)  # Wait for 2 seconds
driver.close()  # Close the browser