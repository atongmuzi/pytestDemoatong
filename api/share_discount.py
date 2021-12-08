from core.rest_client import RestClient
from config.conf import config
api_root_url = config.api_root_url


class ShareDiscount(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(ShareDiscount, self).__init__(api_root_url, **kwargs)

    """大额券-》好友助力接口"""
    def share_friend_boost(self, item_id, friend_uid, **kwargs):
        return self.post("/share_discount/boost", item_id, friend_uid, **kwargs)
