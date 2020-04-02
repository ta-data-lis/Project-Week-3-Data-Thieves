import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://pt.wikipedia.org/wiki/Lista_das_cidades_mais_populosas_do_mundo'
response = requests.get(url, headers = headers).content
soup = BeautifulSoup(response, 'html.parser')
table = soup.find_all('table', attrs = {'class':'sortable wikitable'})[0]



for tr in table.tbody.find_all('tr'):
    column = tr.find_all('td')
    if len(column) == 0:
        continue
    city = tr.findAll('td')[1].a.get_text()
    country = tr.findAll('td')[7].a.get_text()
    parsed_population = 0.0
    try:
        population = tr.findAll('td')[3]
        parsed_population = float(population.span.text.replace("&",""))
    except:
        parsed_population = 0.0
    print(f"{city} - {parsed_population} - {country}")

