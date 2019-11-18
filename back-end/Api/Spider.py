import requests
import re

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
        print(photo_url[0], book_url, name, author[0].replace(" ", ""), detail.replace(" ", ""))
        date = {
            "photo_url": photo_url[0],
            "book_url": book_url,
            "name": name,
            "author": author[0].replace(" ", ""),
            "detail": detail.replace(" ", "")
        }
        # 照片的二进制数据
        photo_base = get_data(photo_url[0]).content
        with open("../Resourse/Images/"+name+".jpg", 'wb') as ph:
            ph.write(photo_base)
        with open("../Resourse/Images/content.txt", 'a', encoding='utf-8') as cont:
            cont.write(str(date))


for result in results:
    judge(result)




