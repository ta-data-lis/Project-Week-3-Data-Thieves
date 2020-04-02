import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#url = 'https://pt.wikipedia.org/wiki/Lista_das_cidades_mais_populosas_do_mundo'
url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests.get(url, headers = headers).content
soup = BeautifulSoup(response, 'html.parser')
table = soup.find(id='example2')

#print(soup.prettify())
for tr in table.tbody.find_all('tr'):
    country = tr.find_all('td')[1].a.get_text()
    population = tr.find_all('td')[2].get_text()
    yearly_change = tr.find_all('td')[3].get_text()
    print(f"{country} - {population} - \"{yearly_change}\"")