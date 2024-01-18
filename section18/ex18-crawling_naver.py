import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver'
param = {'query': '영화 기생충 리뷰'}

response = requests.get(url, params= param)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# print(soup)

review_lst = soup.find_all('span', class_ = 'this_text')

# print(review_lst)

for review in review_lst:
  result = review.get_text()
  print(result)