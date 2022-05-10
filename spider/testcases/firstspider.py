import urllib.request
from fake_useragent import UserAgent
from urllib import parse

ua = UserAgent()
print(ua.chrome)
print(ua.ie)
print(ua.firefox)

qurey_str = {
    'wd': '爬虫'
}
request = parse.urlencode(qurey_str)

url = 'http://www.baidu.com/s?{}'.format(request)

print(url)
print(parse.unquote(url))

# url = 'http://httpbin.org/get'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/97.0.4692.71 Safari/537.36 '
# }
# req = urllib.request.Request(url=url, headers=headers)
# res = urllib.request.urlopen(req)
# html = res.read().decode('utf-8')
# print(html)