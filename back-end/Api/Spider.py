import requests
import re


# url = "http://book.douban.com/latest?icn=index-latestbook-all"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Mobile Safari/537.36'
# }
# response = requests.get(url, headers=headers)
# response.encoding = 'utf-8'
# print(response.text)
with open("../Resourse/html.txt", 'r', encoding='utf-8') as fp:
    response = fp.read()

result = re.findall("<li>(.*?)</li>", response, re.S)


def judge(result):
    photo_url = re.findall('<img src="(.*?)"/>', result)
    if photo_url == []:
        return False
    try:
        book_url = re.search(r'https://(.*?)"', result).group(0)
    except AttributeError:
        pass
    name = re.findall(str(book_url)+">(.*?)</a>", result)[1]
    author = re.findall(r'color-gray">\n(.*?)\n', result)
    detail = re.findall(r'<p.*?>\n\s(.*?)\n', result)[2]
    print(photo_url, book_url, name, author, detail)


for i in result:
    judge(i)
