import requests
from bs4 import BeautifulSoup
import pandas as pd


def teste():

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0'}
    url = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/6699/saopedrodopiaui-pi'

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    # print(soup.prettify())

    title = soup.find('h1').text.replace('\t', '').replace('\n','')

    temperatura_min = soup.find('span',id='min-temp-1').text
    temperatura_max = soup.find('span',id='max-temp-1').text

    chuva = soup.find_all('span',class_='_margin-l-5')[1].text.replace('\t', '').replace('\n','')

teste()