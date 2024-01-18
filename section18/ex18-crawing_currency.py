import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver'
param = {'query': '환율'}

response = requests.get(url, params= param)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

URL = soup.find('ul', class_ = 'list_item _panel')

# [()]

li_lst = URL.find_all('li')

result = []

for li in li_lst:
  if li.find('span'):
    result.append((li.find('span').text, li.find('strong').text, float(li.find('strong').text.replace(',', ''))))



# print(result)

print('='*30)
print(f'{'환율 변환기':|^25}')
print('='*30)

for i, v in enumerate(result):
  print(f'{i+1}', {v[0]}, end= ':')
  print(v[1], 'KRW')

money = int(input('변환을 원하는 통화를 선택하세요: ')) - 1
amount = float(input(f'변환하려는 {result[money][0]} 금액을 입력하세요'))

if result[money][0] == '일본':
  print('일본 JPY 100 변환 결과: ', f'{result[money][2] *amount / 100:0,.2f}')
print(f'{result[money][0]} 변환 결과: ', f'{result[money][2] * amount: 0,.2f}', 'KRW')