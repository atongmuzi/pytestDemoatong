from api.item import item
from common.res_deal import res_deal
from common.headers_get import headers

headers = headers.test_headers_get()


def item_next_true(item_id, first_random):
    """
    用户第一次进来随机选中的一个线盒
    :return: 自定义返回字段 result
    """
    params = {
         "first_random": first_random
    }
    res = item.item_next(item_id=item_id, headers=headers, params=params)
    return res_deal(res)


def item_status(item_id, box_no):
    """
    实时查看线盒的状态
    :return: 自定义返回字段 result
    """
    res = item.item_status(item_id=item_id, box_no=box_no, headers=headers)
    return res_deal(res)


def item_pick_sku(item_id, sku_no):
    """
      用户第一次进来随机选中的一个线盒
      :return: 自定义返回字段 result
      """
    item_id = item_id
    sku_no = sku_no
    res = item.item_pick(headers=headers, item_id=item_id, sku_no=sku_no)
    return res_deal(res)


def item_release_sku(item_id, sku_no):
    """
    用户释放选中的盒子
    :return: 自定义返回字段 result
    """
    item_id = item_id
    sku_no = sku_no
    res = item.item_release(headers=headers, item_id=item_id, sku_no=sku_no)
    return res_deal(res)




