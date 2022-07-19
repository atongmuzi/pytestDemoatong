from common.mysql_operate import db
from common.redis_operate import rs
from common.logger import logger
import datetime
from spider.testcases.admin.admin_api import admin


class Exchange_init():

    def all_init(self):
        # 先修改superdemo中许愿池的开关为true，即可以许愿
        admin.wish_exchage_switch_api()
        # 修改许愿池数据库中相关数据
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_second = "update item_sku_second_price  set refresh_times = '%s' " % now
        sql_wish = "update wish_exchange_item_sku  set refresh_times = '%s' " % now
        db.execute_db(sql_second)
        logger.info("===<清除item_sku_second_price成功>===")
        db.execute_db(sql_wish)
        logger.info("===<清除wish_exchange_item_sku成功>===")
        # 清除相关缓存
        rs.exchange_token_delete()
        logger.info("===<清除item_sku_second_price缓存>===")
        admin.wish_exchage_switch_api()
        return True


ex = Exchange_init()

if __name__ == '__main__':
    ex.all_init()
