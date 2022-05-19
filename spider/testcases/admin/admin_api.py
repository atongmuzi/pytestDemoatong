from lxml import etree
from common.spider import spider
from config.conf import config

host = config.MYSQL_HOST


class admin_api_get:

    def admin_modify_api(self):
        url = 'http://{}:9080/superdiamond/config/save'.format(host)
        headers = {
            # 将从登陆接口获取的cookie值放在此处
            'Cookie': admin.admin_login_jsessionid_get(),
            # 注意，user_agent不能改变，否则cookie失效
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/97.0.4692.71 Safari/537.36 '
        }
        # 获取configValue的值
        configValue = admin.admin_white_user_list_get(headers)
        for i in range(2090, 2096):
            configValue = configValue + "," + str(i)
            # 构建form表单数据
            data = {
                "moduleId": 737,
                "configType": "DRM",
                "visableType": "PUBLIC",
                "configId": 6172,
                "projectId": 167,
                "type": 'development',
                "page": 1,
                "selModuleId": "",
                "flag": "",
                "keyName": "user_check.white_user",
                "configKey": "user_check.white_user",
                "configValue": configValue,
                "configDesc": ""
            }
        # 使用 reqeusts.post()方法提交请求
        res = spider.post_request(url=url, data=data, headers=headers)
        print("更改user_check.white_user的值返回码:{}\n".format(res.status_code))
        # 全推变量，使其生效
        admin.admin_white_user_list_push(headers)

    def admin_login_jsessionid_get(self):
        url = 'http://{}:9080/superdiamond/login'.format(host)
        headers = {
            # 注意，useragent不能改变，否则cookie失效
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/97.0.4692.71 Safari/537.36 '
        }

        # 构建form表单数据
        data = {
            "userCode": "admin",
            "password": "0.123abc"
        }
        res = spider.post_request(url=url, data=data, headers=headers)
        return res.request.headers.get("Cookie")

    def admin_white_user_list_get(self, headers):
        url = 'http://{}:9080/superdiamond/profile/development/167?page=1&moduleId=&keyName=user_check' \
              '.white_user'.format(host)
        # 获得html数据
        html = spider.get_request_html(url, 'UTF-8', headers)
        spider.save_html("admin.html", html, 'w')
        parse_html = etree.HTML(html)
        # 书写xpath表达式,提取文本最终使用text()
        xpath_bds = '//*[@id="row-6172"]/td[3]/@title'
        r_list = parse_html.xpath(xpath_bds)
        print(r_list[0])
        return r_list[0]

    def admin_white_user_list_push(self, headers):
        url = 'http://{}:9080/superdiamond/globalPush/167/development/default'.format(host)
        # 构建form表单数据
        data = {
            "configKey": "user_check.white_user"
        }
        res = spider.post_request(url=url, data=data, headers=headers)
        print("全推返回码:{}\n".format(res.status_code))


admin = admin_api_get()
