from core.result_base import ResultBase
from api.order import order
from common.res_deal import res_deal
from common.logger import logger

TYPE_APPLICATION_JSON_ = {
    "Authorization": "MTE5NzozNTcweHdIb2VVUlV2c2kxS21XRWtIZTcwNTU6Mg==",
    "Content-Type": "application/json"

}


def pre_trade(order_type, item_id, sku_type, sku_no, act_id_list, use_pcoin):
    """
    预下单，选择盲盒的盒子
    :return:自定义的关键字返回结果 result
    """
    result = ResultBase()
    json_data = {
        "order_type": order_type,
        "item_id": item_id,
        "sku_type": sku_type,
        "sku_no": sku_no,
        "act_id_list": act_id_list,
        "use_pcoin": use_pcoin
    }
    header = TYPE_APPLICATION_JSON_
    res = order.pre_order(json=json_data, headers=header)
    return res_deal(res)

