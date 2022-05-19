# 导入解析包
from bs4 import BeautifulSoup
# 创建beautifulsoup解析对象
soup = BeautifulSoup('<p class="Web site url"><b>c.biancheng.net</b></p>', 'html.parser')
#获取整个p标签的html代码
print(soup.p)
print(soup.p.b)
print(soup.p.b.text)
print(soup.p.attrs)