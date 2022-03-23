import requests

# 转换查询GET Python示例代码
if __name__ == '__main__':
    url = 'https://pdfconvert.api.bdymkt.com/v1/query'
    params = {}
    params['token'] = '0a321c5608ad408131497f346944535c3'

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Bce-Signature': 'AppCode/a59c1078a322462783e2d0f8c024eb2d'
    }
    r = requests.request("GET", url, params=params, headers=headers)
    print(r.content)