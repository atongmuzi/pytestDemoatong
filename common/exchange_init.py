from common.mysql_operate import db
from common.redis_operate import rs
from common.logger import logger
import datetime


class Exchange_init():

    def all_init(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_second = "update item_sku_second_price  set refresh_times = '%s' " % now
        sql_wish = "update wish_exchange_item_sku  set refresh_times = '%s' " % now
        db.execute_db(sql_second)
        logger.info("===<清除item_sku_second_price成功>===")
        db.execute_db(sql_wish)
        logger.info("===<清除wish_exchange_item_sku成功>===")
        rs.exchange_token_delete()
        logger.info("===<清除item_sku_second_price缓存>===")


ex = Exchange_init()

if __name__ == '__main__':
    ex.all_init()
