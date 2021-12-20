from core.rest_client import RestClient
from config.conf import config

api_root_url = config.api_root_url


class ShareDiscount(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(ShareDiscount, self).__init__(api_root_url, **kwargs)

    """
    大额券==》好友助力接口
    """

    def share_friend_boost(self, **kwargs):
        return self.post("/share_discount/boost", **kwargs)

    """
    状态查询==》查询大额券领取状态
    """

    def share_item_status(self, item_id, **kwargs):
        return self.get("/share_discount/{}/status".format(item_id), **kwargs)


discount = ShareDiscount(api_root_url)
