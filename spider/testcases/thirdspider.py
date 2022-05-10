from urllib import request, parse
from fake_useragent import UserAgent
import re
from common.mysql_operate import db
import csv


# 定义一个爬虫类
class FundSpider:
    # 初始化URL属性
    def __init__(self):
        self.url = 'http://fund.eastmoney.com/{}.html?spm=search'

    # 请求url，得到页面，传统三步
    def get_html(self, url):
        ua = UserAgent().chrome
        req = request.Request(url=url, headers={'User-Agent': ua})
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
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
    def parse_html(self, code, html):
        # 创建正则表达式对象
        patton = re.compile(r'<span class="fix_date">(.*?)：</span>.*?>(.*?)</span>.*?">(.*?)</span>', re.S)
        re_list = patton.findall(html)
        # 定义路径
        filename = '{}-result.html'.format(code)
        csvname = '{}-result.csv'.format(code)
        csvname_only = 'result.csv'
        for r_info in re_list:
            fund_date = r_info[0]
            fund_net_value = float(r_info[1])
            fund_up_down = r_info[2]
            # self.save_html(filename, "更新日期：{}".format(fund_date), 'w')
            # self.save_html(filename, "基金净值: {}".format(fund_net_value), 'a')
            # self.save_html(filename, "涨跌幅度: {}".format(fund_up_down), 'a')
            # self.save_csv(csvname, [fund_date, fund_net_value, fund_up_down], 'a')
            self.save_csv(csvname_only, [code, fund_date, fund_net_value, fund_up_down], 'a')
            sql = "insert into fund_info(FUND_DATE,FUND_CODE,FUND_NET_VALUE,FUND_UP_DOWN) " \
                  "VALUES('%s','%s','%f','%s')" % (fund_date, code, fund_net_value, fund_up_down)
            self.db_operate(sql)

    # 操作数据库
    def db_operate(self, sql):
        db_result = db.execute_db(sql)
        print(db_result)

    # 入口函数
    def test_run(self, code):
        # 拼接URL地址
        # params = parse.urlencode(code)
        url = self.url.format(code)
        # 发请求
        html = self.get_html(url)
        # 打印匹配数据
        self.parse_html(code, html)
        # 定义路径
        filename = '{}.html'.format(code)
        self.save_html(filename, html, 'w')


fund = FundSpider()

# if __name__ == '__main__':
#     fund.db_operate()
