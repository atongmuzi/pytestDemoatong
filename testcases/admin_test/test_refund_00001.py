import allure
from common.logger import logger
from operation.admin import refund_admin
from common.mysql_operate import db
import pytest


@allure.epic("针对单个接口的测试")
@allure.feature("退款模块的测试")
class TestAdminRefund:

    @allure.story("用例--通过userID退款")
    @allure.description("该用例是针对获取单个用户信息接口的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    def test_refund_userID(self):
        sql = "select order_no from user_order where user_id =1528 and" \
              " status not in(0,30,31,300) and real_price >= 0.02 limit 2 "
        data = db.select_db(sql)
        logger.info("data===>{}".format(data))

        for i in range(len(data)):
            logger.info(data[i]["order_no"])
            order_no = data[i]["order_no"]
            logger.info("*************** 开始执行用例 *************** /n")
            result = refund_admin(order_no)
            assert result.success is True, result.error
            logger.info("接口返回信息：code期望结果【0】,实际结果【{}】；msg期望结果【success】，实际结果【{}】".format(result.code, result.msg))
            logger.info("接口返回data信息：==》{}".format(result.data))

    @allure.story("用例--通过手机号退款")
    @allure.description("该用例是针对获取单个用户信息接口的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.phone
    def test_refund_phone(self):
        sql = "select order_no from user_order where user_id =1528 and" \
              " status not in(0,30,31,300) and real_price >= 0.02 limit 2 "
        data = db.select_db(sql)
        logger.info("data===>{}".format(data))

        for i in range(len(data)):
            logger.info(data[i]["order_no"])
            order_no = data[i]["order_no"]
            logger.info("*************** 开始执行用例 *************** /n")
            result = refund_admin(order_no)
            assert result.success is True, result.error
            logger.info("接口返回信息：code期望结果【0】,实际结果【{}】；msg期望结果【success】，实际结果【{}】".format(result.code, result.msg))
            logger.info("接口返回data信息：==》{}".format(result.data))


if __name__ == '__main__':
    pytest.main(["-v", "test_refund_00001.py", "-m=phone"])
