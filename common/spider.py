from urllib import request
from fake_useragent import UserAgent
from common.mysql_operate import db
import csv
import re


# 定义一个爬虫类
class Spider:

    # 请求url，得到页面，传统三步
    def get_html(self, url, encoding_type):
        ua = UserAgent().chrome
        req = request.Request(url=url, headers={'User-Agent': ua})
        res = request.urlopen(req)
        html = res.read().decode(encoding_type)
        return html

    # 保存文件函数
    def save_html(self, filename, html, write_type):
        with open(filename, write_type)as f:
            f.writelines(html + "\n")

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
