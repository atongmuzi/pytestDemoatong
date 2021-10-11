from common.res_deal import res_deal
from testcases.conftest import base_data
from api.admin import admin

headers = {
    "Authorization": base_data["init_admin_user"]["adminAuthorization"]
}


def refund_admin(order_no):
    """
    退款，管理端退款
    :return:自定义的关键字返回结果 result
    """
    json_data = {
        "order_no": order_no,
        "out_refund_reason": "test",
        "refund_reason": "test",
        "refund_type": 2,
        "return_stock": True,
    }
    res = admin.refund(json_data=json_data, headers=headers)
    return res_deal(res)