import requests
from bs4 import BeautifulSoup
import json

html_content = requests.get('https://www.atlasdasaude.pt/doencasAaZ').text

soup = BeautifulSoup(html_content, 'html.parser')

list = []
divs = soup.find_all('div', class_="views-row")
for div in divs:
    title = div.div.h3.a.text
    desc = div.find("div", class_='views-field-body').text
    list.append({title.strip():desc.strip()})

with open('dict.json','w', encoding='utf-8') as file:
    json.dump(list,file, indent=6, ensure_ascii=True)