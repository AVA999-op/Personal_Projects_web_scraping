import requests
from bs4 import BeautifulSoup
import db_hmw

url = 'https://www.technolife.com/category/mobile/mobile-phone'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

cards = soup.select('section.relative.w-full.rounded-\\[10px\\]')

for card in cards[:100]:
    title_tag = card.find('h2')
    
    if title_tag is None:
        continue
    
    title = title_tag.get_text(strip=True)
    
    link_tag = card.select_one('a[href^="/product-"]')
    
    if link_tag is None:
        continue
    
    link = 'https://www.technolife.com' + link_tag.get('href') 
    
    print('TITLE:', title)
    print('LINK:', link)
    product_response = requests.get(link, headers=headers)
    product_soup = BeautifulSoup(
        product_response.text,
        'html.parser'
    )
    text = product_soup.get_text(" ", strip=True)[:2000]
    print(text)
    db_hmw.save_product(
        title,
        link,
        text
    )
    print('=' * 80)