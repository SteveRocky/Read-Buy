后端主要实现的功能

1. 接收路由请求，并且能返回相应的前端页面、数据，注册、登录、文件传输，将用户数据保存到数据库当中，图片视频资源上传到网络云存储当中，给前端提供下载链接。

2. 爬虫功能是在"豆瓣读书"上爬取一些图片以及详情信息的素材用于前端来展示，将其存储在网络云存储当中。

3. 验证码功能是在用户注册时防止爬虫攻击，后端产生一个图片，每当前端发送get请求之后就生成一张图片放在云存储中，并且保存具体内容，等待验证。

