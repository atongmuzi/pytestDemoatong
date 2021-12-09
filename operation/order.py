from api.order import order
from common.res_deal import res_deal
from common.headers_get import headers

headers = headers.test_headers_get()


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


def pre_trade_wx(order_type, item_id, sku_type, sku_no, amount, act_id_list, app_allow_guess, use_pcoin):
    """
    预下单，微信支付的预下单
    :return:自定义的关键字返回结果 result
    """
    json_data = {
        "order_type": order_type,
        "item_id": item_id,
        "sku_type": sku_type,
        "sku_no": sku_no,
        "amount": amount,
        "act_id_list": act_id_list,
        "app_allow_guess": app_allow_guess,
        "use_pcoin": use_pcoin
    }
    res = order.pre_order_wx(json=json_data, headers=headers)
    return res_deal(res)


def trade_confirm(order_no):
    """
    订单回调确认
    :return:自定义的关键字返回结果 result
    """
    json_data = {
        "order_no": order_no
    }
    res = order.pre_order_wx(json=json_data, headers=headers)
    return res_deal(res)


