import requests
import wget
from datetime import datetime
from bs4 import BeautifulSoup
from pathlib import Path
from unidecode import unidecode
import zipfile
import multiprocessing
import process_files
import database
import re
import os


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
    #date_updated_str = page.find("span", {"class": "documentModified"}).find("span", {"class": "value"}).get_text()
    date_updated_str = page.find("span", text=re.compile('^Data da última extração(.*)')).get_text()
    return datetime.strptime(date_updated_str.split(': ')[1], "%d/%m/%Y").date()


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


# run transformations
def run_transform(file_name):
    process_files.run_transform(file_name)

# download files
def download_file(f, directory):
    Path(directory).mkdir(parents=True, exist_ok=True)
    print("\nDownloading file " + str(f['name']) + "...")
    wget.download(f['url'], directory + str(f['name']) + '.zip')
    extract_file(f['name'], directory + str(f['name']) + '.zip')
    run_transform(str(f['name']) + ".csv")
    print("\nFile " + str(f['name']) + " download completed.")


def delete_old_files():
    zip_files = os.listdir(dl_directory)
    csv_files = os.listdir(dl_directory + 'extracted/')
    for f in zip_files:
        if f.endswith('.zip'):
            os.remove(dl_directory + f)
    for f in csv_files:
        if f.endswith('.csv'):
            os.remove(dl_directory + 'extracted/' + f)


if __name__ == "__main__":
    page_soup = get_page(url_main)
    date_updated = get_updated_date(page_soup)
    
    last_data_update = database.run_query('select max(data_dados) as data_dados from sync_dates;', 'cnpj_dw')[0]
    if last_data_update is None or last_data_update != date_updated:
        print("Atualizando dados...")
        files_to_download = get_files_to_download(page_soup)        
        if files_to_download:
            with open("./sql/staging_area_truncate_all.sql", 'r') as f:
                sql = f.read()
            database.run_sql(sql, 'cnpj_staging_area')
            delete_old_files()

            cpus = multiprocessing.cpu_count()
            max_pool_size = 3
            pool = multiprocessing.Pool(cpus if cpus < max_pool_size else max_pool_size)
            for f in files_to_download:
                pool.apply_async(download_file, args=(f, dl_directory))
            pool.close()
            pool.join()
            process_files.run_dw_transform(date_updated.strftime('%Y-%m-%d'))
    else:
        print("Dados em dia...")
    
