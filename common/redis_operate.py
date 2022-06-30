import redis
from common.logger import logger
import re
from config.conf import config

host = config.redis_host
port = config.redis_port
pwd = config.redis_pwd


class RedisOperate:
    def __init__(self):
        self.pool = redis.ConnectionPool(host=host, port=port, password=pwd, db=0)
        self.r = redis.Redis(connection_pool=self.pool)
        logger.info("redis缓存链接为：=====>{}".format(self.r))

    def test_redis(self, user_id):
        hash_tokens_keys = "pookie:tokens:user_%s" % user_id
        token_key = "pookie:token:user_%s" % user_id
        self.r.delete(token_key)
        logger.info("=====清除user_id为{}的token成功=====".format(user_id))
        logger.info(len(self.r.hkeys(hash_tokens_keys)))
        if len(self.r.hkeys(hash_tokens_keys)) != 0:
            self.r.hdel(hash_tokens_keys, self.r.hkeys(hash_tokens_keys)[0])
            logger.info("=====清除user_id为{}的tokens成功=====".format(user_id))
        else:
            logger.info("=====无hash_tokens_keys为{}的tokens缓存=====".format(hash_tokens_keys))

    def test_fragment_redis(self, user_id):
        fragment_info = "pookie:fragment_user_fragment_info:%s" % user_id
        self.r.delete(fragment_info)
        logger.info("=====清除user_id为{}的fragment_info成功=====".format(user_id))

    def test_token_get(self, user_id, platform_type):
        """
        platform_type = 1表示小程序端，2表示管理端
        """
        if platform_type == 1:
            token_key = "pookie:token:user_%s" % user_id
        elif platform_type == 2:
            token_key = "pookie_admin:token:user_%s" % user_id
        logger.info("token_key为=====》{}".format(token_key))
        value = self.r.get(token_key)
        logger.info("token对应的value=====》{}".format(value))
        value_str = str(value)
        logger.info("value转为str类型后的值value_str=====>{}".format(value_str))
        result = re.findall(r'"token":"(.*?)"', value_str)
        logger.info("匹配结果是======》{}".format(result))
        logger.info(r'let\'s go!')
        if len(result) > 0:
            return result[0]
        else:
            return None

    def exchange_token_delete(self):
        list_keys = self.r.keys("pookie:item_sku_second_price:*")
        for key in list_keys:
            self.r.delete(key)
            logger.info("=====清除item_sku_second_price的缓存成功=====")


rs = RedisOperate()

if __name__ == '__main__':
    rs.exchange_token_delete()
