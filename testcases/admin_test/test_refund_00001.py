from common.logger import logger
from operation.admin import refund_admin
from common.mysql_operate import db


class TestAdminRefund:

    def test_refund(self):
        sql = "select order_no from user_order where user_id =1187 and" \
              " status not in(0,30,31,300) and real_price >= 0.1 limit 5 "
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


