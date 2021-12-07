from common.res_deal import res_deal
from testcases.conftest import base_data
from api.admin import admin
import random
from common.logger import logger

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
        "out_refund_reason": "测试",
        "refund_reason": "test",
        "refund_type": 2,
        "return_stock": True,
    }
    res = admin.refund(json=json_data, headers=headers)
    return res_deal(res)


def reward_task(user_id, v_type, coupon_id):
    """
    手工发放，优惠券
    :return:自定义的关键字返回结果 restult
    """
    num = random.randint(1, 9)
    logger.info("=====>发券数量为{}".format(num))
    json_data = {
        "remark": "社群活动111",
        "user_id_list": [
            user_id
        ],
        "user_tag": 0,
        "prize_list": [
            {
                "type": v_type,
                "num": num,
                "coupon_id": coupon_id,
                "skill_card_id": None,
                "item_id": None,
                "item_sku_id": None,
                "name": None,
                "skillCardId": None
            }
        ]
    }
    res = admin.reward(json=json_data, headers=headers)
    return res_deal(res)
