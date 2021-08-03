import requests
from bs4 import BeautifulSoup
import csv
import time
import re


CSV = 'namainuomai20210721.csv'
URL = 'https://www.aruodas.lt/butai-vilniuje-santariskese-daujoto-g-parduodamas-5751-kv-m-dvieju-kambariu-butas-1-2979085/'
HEADERS = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}


# puslapiu_skaicius = int(soup.find('div', class_="pagination").getText()[-5:-3])

# https://www.aruodas.lt/butai/vilniuje/?FPriceMax=100000
# https://www.aruodas.lt/butai/vilniuje/?FPriceMax=1500000

c = []
links = []

def get_links():
    # n = input('iveskite puslapiu skaiciu:')
    # n = int(n.strip())
    pradinis_linkas = 'https://www.aruodas.lt/namu-nuoma/vilniuje/puslapis/1/?FRegionArea=462'
    html = get_html(pradinis_linkas)
    soup = BeautifulSoup(html.text, 'html.parser')
    puslapiu_skaicius = int(soup.find('div', class_="pagination").getText()[-5:-3])

    for page in range(1, puslapiu_skaicius + 1 ):
        abc = 'https://www.aruodas.lt/namu-nuoma/vilniuje/puslapis/' + str(page) +' /?FRegionArea=462'

        html = get_html(abc)
        time.sleep(1)
        soup = BeautifulSoup(html.text, 'html.parser')
        items = soup.find_all('tr', class_="list-row")
        for item in items:
            try:
                links.append(item.find('div', class_='list-photo').find('a').get('href'))
            except:
                continue


    else:
          print("Viskas super good")
    print(links)
    return links

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def parser_konkret():
    c=[]
    for link in links:

        html = get_html(link)
        time.sleep(1)
        soup = BeautifulSoup(html.text, 'html.parser')

        aprasymas = soup.find('h1', class_="obj-header-text").getText().strip().lstrip('Vilniaus r. sav.,')
        aprasymas = aprasymas.split()
        apras1 = aprasymas[0]
        apras2 = aprasymas[1:]
        buto_kaina = soup.find('span', class_="price-eur").getText().strip().strip('€').replace(" ", "")
        plotas = soup.find('dl', class_="obj-details").find('dd', text=re.compile("m²")).getText().strip().strip("m²")
        sklypo_plotas = soup.find ('dl', class_="obj-details").find('dt', text=re.compile("Sklypo plotas")).find_next().getText().strip()
        statybos_metai = soup.find ('dl', class_="obj-details").find('dt', text=re.compile("Metai")).find_next().getText().strip()
        irengimas = soup.find ('dl', class_="obj-details").find('dt', text=re.compile("Įrengimas:")).find_next().getText().strip()

        try:
            a = soup.find('div', class_="obj-stats simple").find_all('dd')
        except:
            a = soup.find('div', class_="obj-stats").find_all('dd')

        nuoroda = a[0].text.strip()

        try:
            sirdutes = soup.find('span', class_='remembered-heart').getText().strip()
        except :
            sirdutes = 0

        try :
            sildymas = soup.find ('dl', class_="obj-details").find('dt', text=re.compile("Šildymas:")).find_next().getText().strip()
        except :
            sildymas = 0

        kortele = []
        kortele.append(
                    {
                    'apras1': apras1,
                    'apras2': apras2,
                    'aprasymas' : aprasymas,
                    'link_buto' : nuoroda,
                    'kaina' : buto_kaina,
                    'plotas' : plotas,
                    'sirdutes' : sirdutes,
                    'sklypo_plotas' : sklypo_plotas,
                    'statybos_metai' : statybos_metai,
                    'sildymas' : sildymas,
                    'irengimas' : irengimas,

                              }
                             )
        c += kortele

    save_doc(c, CSV)


def save_doc(items, path):
    with open(path, 'w', newline = '') as file:
        writer = csv.writer(file, delimiter=';')



        writer.writerow(['Rajonas','Gatvė','Aprašymas', 'Buto nuoroda', 'Namo kaina', 'Plotas','Širdutės','Sklypo plotas','Statybos metai','Šildymas',
                         'Irengimas'])
        for item in items:
            writer.writerow([item['apras1'],item['apras2'], item['aprasymas'],item['link_buto'],item['kaina'],item['plotas'],item['sirdutes'],item['sklypo_plotas'],item['statybos_metai'],item['sildymas'],
                            item['irengimas']])

def parser():
    get_links()
    parser_konkret()

if __name__ == '__main__':
    parser()
