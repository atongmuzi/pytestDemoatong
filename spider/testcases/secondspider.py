from urllib import request
from fake_useragent import UserAgent
from urllib import parse

# 拼接URL
url = 'https://www.iconfont.cn/search/index?searchType=icon&q={}'
search = "长方形"
params = parse.quote(search)
full_url = url.format(params)

# 重构请求头
ua = UserAgent().chrome
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/97.0.4692.71 Safari/537.36 "
}
# 创建对应请求信息
req = request.Request(url=full_url, headers=headers)
# 获取相应对象
res = request.urlopen(full_url)
# 获取相应内容
html = res.read().decode("utf-8")

# 保存结果到文件里
filename = search + '.html'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)
