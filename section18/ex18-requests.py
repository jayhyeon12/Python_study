import requests

url = 'https://search.naver.com/search.naver'
# 주소 창에는 아스키코드 문자만 인식됨(URL이 ASCII 코드로 인코딩)

parm = {'query': '파이썬'}
response = requests.get(url, params= parm)

print(response.text)

