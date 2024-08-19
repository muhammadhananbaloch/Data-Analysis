from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import random

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=options)

# Disable WebDriver detection
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

query = 'monitor'  # The query to search for
file = 1
while True:
    try: 
        driver.get(f"https://www.walmart.com/search?q={query}&page={file}")  # Open the website

        # Random delay to simulate human behavior
        time.sleep(random.uniform(3, 6))
        
        # Simulate mouse movement to an element
        element_to_hover_over = driver.find_element(By.CSS_SELECTOR, 'body')
        action = ActionChains(driver)
        action.move_to_element(element_to_hover_over).perform()

        # Check if CAPTCHA is present
        if "captcha" in driver.page_source.lower():
            input("CAPTCHA detected. Please complete the CAPTCHA and press Enter to continue...")

        # Extract data
        script_tags = driver.find_element(By.ID, '__NEXT_DATA__')
        data = script_tags.get_attribute('innerHTML')  # Get the data from the script tag
        json_data = json.loads(data)  # Load the data into a JSON object
        
        # Save data to file
        with open(f'Data/{query}_{file}.json', 'w') as f:
            f.write(json.dumps(json_data, indent=4))  # Convert dict to string and write to file

        # Check for the "Next" button
        try:
            next_button = driver.find_element(By.CLASS_NAME, 'ld ld-ChevronRight pv1 primary')
            if not next_button.is_enabled():
                print('No more pages to scrape')
                break
        except Exception as e:
            print('No more pages to scrape or an error occurred.')
            print(e)
            break
        
        file += 1  # Move to the next page

    except Exception as e:
        print(e)
        print('outside error')
        break

time.sleep(2)  # Wait for 2 seconds
driver.close()  # Close the browser
