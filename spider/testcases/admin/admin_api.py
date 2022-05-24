from lxml import etree
from common.spider import spider
from config.conf import config
from spider.testcases.admin.common import admin_login_jsessionid_get, admin_white_user_list_push,\
    login_white_phone_list_get

host = config.MYSQL_HOST
url = 'http://{}:9080/superdiamond/config/save'.format(host)


class admin_api_get:

    def modify_white_user_api(self, start, end):
        headers = admin_login_jsessionid_get()
        # 获取configValue的值
        keyName = 'user_check.white_user'
        configId = 6172
        configValue = login_white_phone_list_get(headers, keyName, configId)
        for i in range(start, end):
            configValue = configValue + "," + str(i)
            # 构建form表单数据
            data = {
                "moduleId": 737,
                "configType": "DRM",
                "visableType": "PUBLIC",
                "configId": configId,
                "projectId": 167,
                "type": 'development',
                "page": 1,
                "selModuleId": "",
                "flag": "",
                "keyName": keyName,
                "configKey": keyName,
                "configValue": configValue,
                "configDesc": ""
            }
        # 使用 reqeusts.post()方法提交请求
        res = spider.post_request(url=url, data=data, headers=headers)
        print("更改user_check.white_user的值返回码:{}\n".format(res.status_code))
        # 全推变量，使其生效
        code = admin_white_user_list_push(headers, keyName)
        if code:
            return "添加成功"

    def modify_login_white_phone_api(self, phone):
        # 获取configValue的值
        keyName = 'login.white.list'
        configId = 5974
        headers = admin_login_jsessionid_get()
        configValue = login_white_phone_list_get(headers, keyName, configId) + ',' + phone
        # 构建form表单数据
        data = {
            "moduleId": 737,
            "configType": "DRM",
            "visableType": "PUBLIC",
            "configId": configId,
            "projectId": 167,
            "type": 'development',
            "page": 1,
            "selModuleId": "",
            "flag": "",
            "keyName": "login.white.list",
            "configKey": "login.white.list",
            "configValue": configValue,
            "configDesc": ""
        }
        # 使用 reqeusts.post()方法提交请求
        res = spider.post_request(url=url, data=data, headers=headers)
        print("更改login.white.list的值返回码:{}\n".format(res.status_code))
        # 全推变量，使其生效
        code = admin_white_user_list_push(headers, keyName)
        if code:
            return "添加成功"


admin = admin_api_get()