import requests
import re
from Image_store import image_store

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Mobile Safari/537.36'
}


# url请求函数
def get_data(url):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response


with open("../Resourse/html.txt", 'r', encoding='utf-8') as fp:
    html = fp.read()
results = re.findall("<li>(.*?)</li>", html, re.S)


def judge(result):
    photo_url = re.findall('<img src="(.*?)"/>', result)

    if photo_url == []:
        print('url无效')
    else:

        try:
            book_url = re.search(r'https://(.*?)"', result).group(0)
        except AttributeError:
            pass
        name = re.findall(str(book_url)+">(.*?)</a>", result)[1]
        author = re.findall(r'color-gray">\n(.*?)\n', result)
        detail = re.findall(r'<p.*?>\n\s(.*?)\n', result)[2]
        photo_data = get_data(photo_url[0]).content
        cloud_name = image_store(photo_data)
        date = {
            "photo_url": photo_url[0],
            "book_url": book_url,
            "name": name,
            "cloud_url": "http://q17qc0xmu.bkt.clouddn.com/"+cloud_name,
            "author": author[0].replace(" ", ""),
            "detail": detail.replace(" ", "")

        }
        print(date['cloud_url'])
        # 相当于把数据存入数据库,之后需要把这些数据存储到mysql、redis中
        with open("../Resourse/Images/content.txt", 'a', encoding='utf-8') as cont:
            cont.write(str(date))


for result in results:
    judge(result)




