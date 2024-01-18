import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:5500/section18/test2.html'

parm = {'query': '파이썬'}
response = requests.get(url, params= parm)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.find('a').get('href'))

print(soup.find_all('div', class_='purple'.text))