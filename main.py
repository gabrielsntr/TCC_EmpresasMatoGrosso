import requests
import wget
from datetime import datetime
from bs4 import BeautifulSoup
from pathlib import Path
from unidecode import unidecode
import zipfile
import multiprocessing

# constants
url_main = 'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj'
dl_directory = './files/'


# get page content for beautifulsoup
def get_page(url):
    print("Getting page html...")
    return BeautifulSoup(requests.get(url).content, "html.parser")


# get date updated
def get_updated_date(page):
    print("Getting date updated...")
    date_updated_str = page.find("span", {"class": "documentModified"}).find("span", {"class": "value"}).get_text()
    return datetime.strptime(date_updated_str.split(' ')[0], "%d/%m/%Y").date()


# get urls
def get_files_to_download(page):
    print("Getting urls...")
    urls_soup = page.find_all("a", {"class": "external-link"})
    urls = []
    for url in urls_soup:
        #size = round(int((requests.head(url['href']).headers['Content-Length']))/1024)
        size = 0
        file_name = unidecode(url.get_text()).strip().replace(' ', '_').replace('/', '-').lower()
        urls.append({'name': file_name, 'url': url['href'], 'size_kb': size})
    return urls


# extract files
def extract_file(file_name, file_dir):
    print("\nExtracting...")
    zipdata = zipfile.ZipFile(file_dir)
    zipinfos = zipdata.infolist()
    for zipinfo in zipinfos:
        zipinfo.filename = file_name + ".csv"
        zipdata.extract(zipinfo, path='./files/extracted/')


# download files
def download_file(f, directory):
    Path(directory).mkdir(parents=True, exist_ok=True)
    print("\nDownloading file " + str(f['name']) + "...")
    wget.download(f['url'], directory + str(f['name']) + '.zip')
    extract_file(f['name'], directory + str(f['name']) + '.zip')
    print("\nFile " + str(f['name']) + " download completed.")


if __name__ == "__main__":
    page_soup = get_page(url_main)
    date_updated = get_updated_date(page_soup)
    files_to_download = get_files_to_download(page_soup)

    cpus = multiprocessing.cpu_count()
    max_pool_size = 4
    pool = multiprocessing.Pool(cpus if cpus < max_pool_size else max_pool_size)
    for f in files_to_download:
        pool.apply_async(download_file, args=(f, dl_directory))
    pool.close()
    pool.join()
