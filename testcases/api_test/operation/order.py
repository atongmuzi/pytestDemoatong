from core.result_base import ResultBase
from api.order import order
from common.logger import logger


def pre_trade(order_type, item_id, sku_type, sku_no, act_id_list, use_pcoin):
    """
    预下单，选择盲盒的盒子
    :return:自定义的关键字返回结果 result
    """
    json_data = {
        "order_type":order_type,
        "item_id":item_id,
        "sku_type":sku_type,
        "sku_no":sku_no,
        "act_id_list":act_id_list,
        "use_pcoin":use_pcoin
    }
    header = {
        "Authorization": "ODM3OjEzMDlVRWN5QmI3YnNPMm1WWXNIUkpjMjU3Njoy",
        "Content-Type": "application/json"

    }
    result = ResultBase()
    res = order.pre_order(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码：【 {} 】,返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    return result




