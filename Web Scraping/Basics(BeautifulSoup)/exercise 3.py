import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://keithgalli.github.io/web-scraping/webpage.html'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
	# Get the content of the response
	html_content = response.content
	
	# Parse the HTML content using Beautiful Soup
	soup = BeautifulSoup(html_content, 'html.parser')
	
	# Find the <ul> tag with class 'fun-facts'
	fun_facts = soup.find('ul', attrs={'class': 'fun-facts'})
	
	if fun_facts:
		# Find all <li> tags within the <ul> tag
		facts = fun_facts.find_all('li')
		
		# Iterate through each fact and print if it contains 'is'
		for fact in facts:
			if 'is' in fact.get_text():
				print(fact.get_text())
	else:
		print("No 'fun-facts' class found on the page.")
else:
	print(f"Failed to retrieve the webpage. Status code: {response.status_code}")