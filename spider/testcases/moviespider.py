from urllib import request, parse
from fake_useragent import UserAgent
import re
from common.mysql_operate import db
import csv


# 定义一个爬虫类
class FundSpider:
    # 初始化URL属性
    def __init__(self, url):
        self.url = url

    # 请求url，得到页面，传统三步
    def get_html(self, url):
        ua = UserAgent().chrome
        req = request.Request(url=url, headers={'User-Agent': ua})
        res = request.urlopen(req)
        html = res.read().decode('GBK')
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

    # 匹配需要的数据
    def parse_html(self, html):
        # 创建正则表达式对象
        patton = re.compile(r'<a href="(.*?)".*?>(.*?)</a>.*?◎译 名 (.*?)◎片 名', re.S)
        re_list = patton.findall(html)
        # 定义路径
        csv_name = 'result.csv'
        for r_info in re_list:
            link = r_info[0]
            movie_name = r_info[1]
            movie_rename = r_info[2]
            print("link:{},movie_name:{},movie_rename:{}".format(link, movie_name, movie_rename))
            self.save_csv(csv_name, [link, movie_name, movie_rename], 'a')

    # 操作数据库
    def db_operate(self, sql):
        db_result = db.execute_db(sql)
        print(db_result)

    # 入口函数
    def test_run(self, page):
        # 拼接url
        url = self.url.format(page)
        # 发请求
        html = self.get_html(url)
        # 打印匹配数据
        self.parse_html(html)
        # 定义路径
        filename = 'new_movie.html'
        self.save_html(filename, html, 'a')


fund = FundSpider()
if __name__ == '__main__':
    for i in range(1, 4):
        fund.test_run(i)
        i += 1
