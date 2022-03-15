from common.logger import logger
from operation.admin import refund_admin
from common.mysql_operate import db


class TestAdminRefund:

    def test_refund(self, user_id, refund_num, refund_amount):
        sql = "select order_no from user_order where user_id =%s and" \
              " status not in(0,30,31,300) and real_price >= %s limit %s "\
              % (user_id, refund_amount, refund_num)
        data = db.select_db(sql)
        len_data = len(data)
        logger.info("data===>{}".format(data))
        for i in range(len_data):
            logger.info(data[i]["order_no"])
            order_no = data[i]["order_no"]
            logger.info("*************** 开始执行用例 *************** /n")
            result = refund_admin(order_no)
            assert result.success is True, result.error
            logger.info("接口返回信息：code期望结果【0】,实际结果【{}】；msg期望结果【success】，实际结果【{}】".format(result.code, result.msg))
            logger.info("接口返回data信息：==》{}".format(result.data))
        if len_data > 0:
            return "退款成功条数: "+str(len_data)+" 条"
        else:
            return "暂无需要退款的订单"


re = TestAdminRefund()
