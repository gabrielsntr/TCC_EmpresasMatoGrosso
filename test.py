from bs4 import BeautifulSoup
import requests
from unidecode import unidecode
from datetime import datetime
import re

URL_MAIN = 'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj'


page = BeautifulSoup(requests.get(URL_MAIN).content, "html.parser")

urls_soup = page.find_all("a", {"class": "external-link"})
urls = []
for url in urls_soup:
    file_name = unidecode(url.get_text()).strip().replace(' ', '_').replace('/', '-').lower()
    urls.append({'name': file_name, 'url': url['href']})

#for url in urls:
#    print("{'name': '" + url['name'] + "', 'url': '" + url['url'] + "'}")


# print("Getting date updated...")
date_updated_str = page.find("span", text=re.compile('^Data da última extração(.*)')).get_text()
print(datetime.strptime(date_updated_str.split(': ')[1], "%d/%m/%Y").date())