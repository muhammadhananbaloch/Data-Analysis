from bs4 import BeautifulSoup
import requests

walmart_url = 'https://www.walmart.com/ip/Simzlife-12-Volt-Refrigerator-19QT-18L-Portable-Car-4-50-12-24V-DC-110-240V-AC-Mini-Fridge-Camping-Travel-Truck-Home-Black/5323034796?classType=REGULAR'

HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

# script_tag = soup.find('script', id='__NEXT_DATA__')     
# html = script_tag.string

# print(html)
def get_product_links(query, page_numeber=1):
    search_url = f"https://www.walmart.com/search?q={query}&page={page_numeber}" 
    print(search_url)
    response = requests.get(search_url, headers=HEADERS)    

    soup = BeautifulSoup(response.content, 'html.parser') 

    links = soup.find_all('a', href=True)

    product_links = []

    for link in links:
        if '/ip/' in link['href']:
            if 'https' in link['href']:
                full_link = link['href']    
            else:
                full_link = 'https://www.walmart.com' + link['href']
            
            product_links.append(full_link)
    return product_links
def main():
    print(get_product_links('playstation'))

if __name__ == '__main__':
    main()