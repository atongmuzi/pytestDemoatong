import os
from core.rest_client import RestClient
from config.conf import config

api_root_url = config.api_root_url


class Admin(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super().__init__(api_root_url, **kwargs)

    def refund(self, **kwargs):
        return self.post("/adm/order/refund", **kwargs)

    def reward(self, **kwargs):
        return self.post("/adm/reward_task/add", **kwargs)

    def ichiban(self, **kwargs):
        return self.post("/adm/series_reward/config_excel",**kwargs)


admin = Admin(api_root_url)
