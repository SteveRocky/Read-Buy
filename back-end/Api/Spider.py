import requests
import re


url = "http://www.zongheng.com/"
response = requests.get(url)
response.encoding = 'utf-8'
with open("../Resourse/html.txt", 'w', encoding='utf-8') as fp:
    fp.write(response.text)
