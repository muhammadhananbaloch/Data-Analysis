from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import time

try:
    website = 'https://www.adamchoi.co.uk/overs/detailed'
    path = r'C:\Users\HP\repos\chromedriver-win64\chromedriver.exe'
    
    # Create a Service object with the path to the ChromeDriver executable
    service = Service(executable_path=path)
    
    # Pass the Service object to the Chrome WebDriver
    driver = webdriver.Chrome(service=service)
    driver.get(website)

    all_matches_button = driver.find_element(By.XPATH, "//label[@analytics-event='All matches']")    
    all_matches_button.click()
    time.sleep(3)   
    # driver.quit()
except Exception as e:
    print(e)
