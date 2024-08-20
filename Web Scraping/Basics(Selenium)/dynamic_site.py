from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

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
    
    dropdown_country = Select(driver.find_element(By.ID, 'country'))    # Find the dropdown menu to select the country
    dropdown_country.select_by_visible_text('Spain')    # Select England from the dropdown menu

    dropdown_league = Select(driver.find_element(By.ID, 'league'))
    dropdown_league.select_by_visible_text('La Liga')    # Select the Premier League from the dropdown menu 

    dropdown_season = Select(driver.find_element(By.ID, 'season'))    # Find the dropdown menu to select the season 
    dropdown_season.select_by_visible_text("22/23") 

    time.sleep(2)
    matches = driver.find_elements(By.TAG_NAME, "tr") # Click the button to show all matches

    date = []
    home_team = []  
    away_team = []
    score = []
    for match in matches:
        try:
            date.append(match.find_element(By.XPATH, "./td[1]").text)
        except:
            date.append("Not found")
        try:
            home_team.append(match.find_element(By.XPATH, "./td[2]").text)
        except:
            home_team.append("Not found")
        try:
            score.append(match.find_element(By.XPATH, "./td[3]").text)
        except:
            score.append("Not found")
        try:
            away_team.append(match.find_element(By.XPATH, "./td[4]").text)
        except: 
            away_team.append("Not found")  
    # time.sleep(10)   
    driver.quit()
except Exception as e:
    print(e)

df = pd.DataFrame({'Date': date, 'Home Team': home_team, 'Score': score, 'Away Team': away_team})    # Display the data in a DataFrame   
df.to_csv('football_data.csv', index=False)    # Save the data in a CSV file  
print(df)    # Display the data in the console  
