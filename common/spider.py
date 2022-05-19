from urllib import request
from fake_useragent import UserAgent
from common.mysql_operate import db
import csv
import re
import requests
from io import BytesIO
import gzip


# 定义一个爬虫类
class Spider:

    # 请求url，得到页面，传统三步
    def get_html(self, url, encoding_type):
        ua = UserAgent().chrome
        req = request.Request(url=url, headers={'User-Agent': ua})
        res = request.urlopen(req)
        html = res.read()
        buff = BytesIO(html)
        f = gzip.GzipFile(fileobj=buff)
        htmls = f.read().decode(encoding_type)
        return htmls

    # 用request请求url，得到页面
    def get_request_html(self, url, encoding_type):
        # 使用requests模块得到响应对象，两个参数
        ua = UserAgent().chrome
        res = requests.get(url, headers={'User-Agent': ua}, auth=('13656640242', '22334455@x'))
        # 更改编码格式
        res.encoding = encoding_type
        # 得到html网页
        html = res.text
        return html

    def get_request_html(self, url, encoding_type, headers):
        # 使用requests模块得到响应对象,三个参数
        res = requests.get(url, headers=headers)
        # 更改编码格式
        res.encoding = encoding_type
        # 得到html网页
        html = res.text
        return html

    def post_request(self, url, data, headers):
        # post请求
        res = requests.post(
            url=url,
            data=data,
            headers=headers,
        )
        return res

    # 保存文件函数
    def save_html(self, filename, html, write_type):
        with open(filename, write_type)as f:
            f.writelines(html+'\n')

    # 保存CSV函数
    def save_csv(self, filename, result, write_type):
        with open(filename, write_type, newline='')as f:
            writer = csv.writer(f)
            writer.writerow(result)

    # 匹配正则表达式、返回结果
    def patton_result(self, patton_ex, html):
        patton = re.compile(patton_ex, re.S)
        return patton.findall(html)

    # 操作数据库
    def db_operate(self, sql):
        db_result = db.execute_db(sql)
        print(db_result)


spider = Spider()
