from lxml import etree
from common.spider import spider
from config.conf import config
from spider.testcases.admin.common import admin_login_jsessionid_get, admin_white_user_list_push, \
    value_list_get, form_data_get

host = config.MYSQL_HOST
url = 'http://{}:9080/superdiamond/config/save'.format(host)


class admin_api_get:

    def modify_white_user_api(self, start, end):
        # 获取headers的值
        headers = admin_login_jsessionid_get()
        # 获取configValue的值
        keyName = 'user_check.white_user'
        configId = 6172
        configValue = value_list_get(headers, keyName, configId)
        for i in range(start, end):
            configValue = configValue + "," + str(i)
            # 根据参数获取form表单数据
            data = form_data_get(configId, keyName, configValue)
        # 使用 reqeusts.post()方法提交请求
        res = spider.post_request(url=url, data=data, headers=headers)
        print("更改user_check.white_user的值返回码:{}\n".format(res.status_code))
        # 全推变量，使其生效
        code = admin_white_user_list_push(headers, keyName)
        if code:
            return "添加成功"

    def select_white_user_last(self):
        # 获取headers的值得
        headers = admin_login_jsessionid_get()
        # 获取configValue的值
        keyName = 'user_check.white_user'
        configId = 6172
        configValue = value_list_get(headers, keyName, configId)
        last_user_id = configValue.split(',')[-1]
        return last_user_id

    def modify_login_white_phone_api(self, phone):
        # 获取header的值
        headers = admin_login_jsessionid_get()
        # 获取configValue的值
        keyName = 'login.white.list'
        configId = 5974
        configValue = value_list_get(headers, keyName, configId) + ',' + phone
        # 根据参数获取form表单数据
        data = form_data_get(configId, keyName, configValue)
        # 使用 reqeusts.post()方法提交请求
        res = spider.post_request(url=url, data=data, headers=headers)
        print("更改login.white.list的值返回码:{}\n".format(res.status_code))
        # 全推变量，使其生效
        code = admin_white_user_list_push(headers, keyName)
        if code:
            return "添加成功"

    def wish_exchage_switch_api(self):
        # 获取header的值
        headers = admin_login_jsessionid_get()
        keyName = 'wish.switch'
        configId = 6189
        configValue = 'true'
        # 根据参数获取form表单数据
        data = form_data_get(configId, keyName, configValue)
        # 使用 reqeusts.post()方法提交请求
        res = spider.post_request(url=url, data=data, headers=headers)
        print("更改wish.switch的值返回码:{}\n".format(res.status_code))
        # 全推变量，使其生效
        code = admin_white_user_list_push(headers, keyName)
        return code


admin = admin_api_get()
