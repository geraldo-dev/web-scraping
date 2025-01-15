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

    temperature_min = soup.find('span',id='min-temp-1').text
    temperature_max = soup.find('span',id='max-temp-1').text

    rain = soup.find_all('span',class_='_margin-l-5')[1].text.replace('\t', '').replace('\n','')

    weather_SP = {'title':[], 'temperature_min':[], 'temperature_max':[], 'rain':[]}
    
    weather_SP['title'].append(title)
    weather_SP['temperature_min'].append(temperature_min)
    weather_SP['temperature_max'].append(temperature_max)
    weather_SP['rain'].append(rain)
      

    df = pd.DataFrame(weather_SP)
    df.to_csv('weather.csv', encoding='utf-8', sep=';')


teste()