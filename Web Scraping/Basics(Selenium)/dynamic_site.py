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

    all_matches_button = driver.find_element(By.XPATH, "//label[@analytics-event='All matches']")    # Find the button to show all matches  
    all_matches_button.click() # Click the button to show all matches

    # select_season_button = driver.find_element(By.XPATH, '//*[@id="season"]')    # Find the button to show all seasons
    # select_season_button.click() # Click the button to show all seasons

    choose_season_button = driver.find_element(By.XPATH, '//*[@label="21/22"]')    # Find the button to show the 21/22 season
    choose_season_button.click() # Click the button to show the 21/22 season
    time.sleep(2)
    matches = driver.find_elements(By.TAG_NAME, "tr") # Click the button to show all matches
    for match in matches:
        print(match.text)
    time.sleep(10)   
    driver.quit()
except Exception as e:
    print(e)
