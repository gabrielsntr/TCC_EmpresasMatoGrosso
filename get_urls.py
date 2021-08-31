import requests
import wget
from datetime import datetime
from bs4 import BeautifulSoup
from pathlib import Path
from unidecode import unidecode
import zipfile
import multiprocessing

url = 'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj'

page = BeautifulSoup(requests.get(url).content, "html.parser")
urls_soup = page.find_all("a", {"class": "external-link"})
urls = []
for url in urls_soup:
    #size = round(int((requests.head(url['href']).headers['Content-Length']))/1024)
    size = 0
    file_name = unidecode(url.get_text()).strip().replace(' ', '_').replace('/', '-').lower()
    urls.append({'name': file_name, 'url': url['href'], 'size_kb': size})
    print(file_name)


