import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0'}
url = 'https://www.climatempo.com.br/'

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
