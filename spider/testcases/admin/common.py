from lxml import etree

from common.spider import spider
from config.conf import config

host = config.MYSQL_HOST


def admin_login_jsessionid_get():
    url = 'http://{}:9080/superdiamond/login'.format(host)
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 ' \
         'Safari/537.36 '
    headers = {
        # 注意，useragent不能改变，否则cookie失效
        'User-Agent': ua
    }

    # 构建form表单数据
    data = {
        "userCode": "admin",
        "password": "0.123abc"
    }
    res = spider.post_request(url=url, data=data, headers=headers)
    sessionid = res.request.headers.get("Cookie")
    headers_get = {
        # 将从登陆接口获取的cookie值放在此处
        'Cookie': sessionid,
        # 注意，user_agent不能改变，否则cookie失效
        'User-Agent': ua
    }
    return headers_get


def admin_white_user_list_push(headers, configkey):
    url = 'http://{}:9080/superdiamond/globalPush/167/development/default'.format(host)
    # 构建form表单数据
    data = {
        "configKey": configkey
    }
    res = spider.post_request(url=url, data=data, headers=headers)
    print("全推返回码:{}\n".format(res.status_code))
    return res.status_code


def login_white_phone_list_get(headers, keyName, number):
    url = 'http://{}:9080/superdiamond/profile/development/167?page=1&moduleId=&keyName={}'.format(
        host, keyName)
    # 获得html数据
    html = spider.get_request_html(url, 'UTF-8', headers)
    spider.save_html("admin.html", html, 'w')
    parse_html = etree.HTML(html)
    # 书写xpath表达式,提取文本最终使用text()
    xpath_bds = '//*[@id="row-{}"]/td[3]/@title'.format(number)
    r_list = parse_html.xpath(xpath_bds)
    print(r_list[0])
    return r_list[0]
