import requests
from bs4 import BeautifulSoup

def get_links(pradinis_linkas):
    # n = input('iveskite puslapiu skaiciu:')
    # n = int(n.strip())
    # pradinis_linkas = 'https://www.aruodas.lt/namu-nuoma/vilniuje/puslapis/1/?FRegionArea=462'
    html = get_html(pradinis_linkas)
    soup = BeautifulSoup(html.text, 'html.parser')
    puslapiu_skaicius = int(soup.find('div', class_="pagination").getText()[-5:-3])
    print (puslapiu_skaicius)

def get_html(url, params=''):
    HEADERS = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}

    r = requests.get(url, headers=HEADERS, params=params)
    return r
