import os
from core.rest_client import RestClient
from common.read_data import data

# 获取该项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 获取ini配置信息路径
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
# 获取项目请求基础地址
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class Item(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Item, self).__init__(api_root_url, **kwargs)

    def item_next(self, item_id, **kwargs):
        return self.get("/item/mbox/{}/next/v5".format(item_id), **kwargs)

    def item_pick(self, item_id, sku_no, **kwargs):
        return self.get("/item/mbox/pick?item_id={}&sku_no={}".format(item_id, sku_no), **kwargs)


item = Item(api_root_url)
