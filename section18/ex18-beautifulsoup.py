import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver'

parm = {'query': '파이썬'}
response = requests.get(url, params= parm)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.find('a'))