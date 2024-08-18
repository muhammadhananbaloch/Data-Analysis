from bs4 import BeautifulSoup
import os
import pandas as pd 

data = {'title':[], 'price':[], 'link':[]}
for file in os.listdir('data'):
    try:
        with open(f'data/{file}', 'r', encoding='utf-8') as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        # print(soup.prettify())

        t = soup.find('h2')
        title = t.get_text().strip() #if t else 'Not found'

        l = t.find('a')
        link = 'https://www.amazon.com/'+ l['href'] #if l else 'Not found'

        p = soup.find('span', attrs={'class':'a-price-whole'})
        price =    p.get_text() #if p else 'Not found'
        data['title'].append(title)
        data['price'].append(price) 
        data['link'].append(link)
    except Exception as e:
        print(e)
pd.DataFrame(data).to_csv('data.csv', index=False)



# CAN ALSO CONTINUE LIKE THIS:
#     try:
#         [price.append(p.find('span', class_='a-price').find('span', class_='a-offscreen').text) for p in soup]
#     except:
#         price.append('Not found')
# print(len(price))