from api.order import order
from common.res_deal import res_deal
from testcases.conftest import base_data

headers = {
    "Authorization": base_data["init_admin_user"]["Authorization"]
}


def pre_trade(order_type, item_id, sku_type, sku_no, act_id_list, use_pcoin):
    """
    预下单，选择盲盒的盒子
    :return:自定义的关键字返回结果 result
    """
    json_data = {
        "order_type": order_type,
        "item_id": item_id,
        "sku_type": sku_type,
        "sku_no": sku_no,
        "act_id_list": act_id_list,
        "use_pcoin": use_pcoin
    }
    res = order.pre_order(json=json_data, headers=headers)
    return res_deal(res)

