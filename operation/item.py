from api.item import item
from core.result_base import ResultBase
from testcases.conftest import base_data
from common.res_deal import res_deal


headers = {
    "Authorization": base_data["init_admin_user"]["Authorization"]
}


def item_next_true(item_id, first_random):
    """
    用户第一次进来随机选中的一个线盒
    :return: 自定义返回字段 result
    """
    result = ResultBase()
    params = {
         "first_random": first_random
    }
    res = item.item_next(item_id=item_id, headers=headers, params=params)
    return res_deal(res)


def item_pick_sku(item_id, sku_no):
    """
      用户第一次进来随机选中的一个线盒
      :return: 自定义返回字段 result
      """
    result = ResultBase()
    item_id = item_id
    sku_no = sku_no
    res = item.item_pick(headers=headers, item_id=item_id, sku_no=sku_no)
    return res_deal(res)



