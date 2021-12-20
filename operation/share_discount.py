from api.share_discount import discount
from testcases.conftest import base_data
from common.headers_get import headers
from api.share_discount import discount
from common.res_deal import res_deal

header = headers.test_headers_get()
user_id = base_data["init_user"]["user_id"]
headers_friend = headers.test_headers_get_friend()


def share_item_status(item_id, **kwargs):
    """
    进入盲盒详情页时，查看该状态
    """


def share_friend_boost_param(item_id):
    """
    给好友助力大额券
    """
    json_data = {
        "item_id": item_id,
        "friend_uid": user_id
    }
    res = discount.share_friend_boost(headers=headers_friend, json=json_data)
    result = res_deal(res)
    return result




