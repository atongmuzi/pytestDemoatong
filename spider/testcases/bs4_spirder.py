# 导入解析包
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>"c语言中文网"</title></head>
<body>
<p class="title"><b>c.biancheng.net</b></p>
<p class="website">一个学习编程的网站</p>
<a href="http://c.biancheng.net/python/" id="link1">python教程</a>
<a href="http://c.biancheng.net/c/" id="link2">c语言教程</a>
<a href="http://c.biancheng.net/django/" id="link3">django教程</a>
<p class="vip">加入我们阅读所有教程</p>
<a href="http://vip.biancheng.net/?from=index" id="link4">成为vip</a>
<p class="introduce">介绍:
<a href="http://c.biancheng.net/view/8066.html" id="link5">关于网站</a>
<a href="http://c.biancheng.net/view/8092.html" id="link6">关于站长</a>
</p>
"""

# 创建beautifulsoup解析对象
soup = BeautifulSoup(html_doc, 'html.parser')
# # print(soup)
# # print(soup.title.text, soup.title.name, soup.title.string)
# # print(soup.p['class'])
# # # print(soup.a)
# # print(soup.findAll('a'))
# # print(soup.find(id='link1'))
# # for link in soup.findAll('a'):
# #     print(link.get('href'))
# # print(soup.text)
# tag = soup.body
# # print(tag.name)
# # print(tag)
# # print(tag['class'])
# # print(tag.attrs)
# print(tag.contents)
# title_list = soup.select('title')
# for title in title_list:
#     print(title.text)


print(soup.select('p ~ #link3'))
print(soup.select('p ~ a:nth-of-type(1)'))

