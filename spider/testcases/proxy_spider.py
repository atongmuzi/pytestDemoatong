import requests

url = 'http://httpbin.org/get'
headers = {
    'User-Agent':'Mozilla/5.0'
}
# 网上找的免费代理ip
proxies = {
    'http': 'http://191.231.62.142:8000',
    'https': 'https://191.231.62.142:8000'
}
html = requests.get(url, proxies=proxies, headers=headers, timeout=5).text
print(html)