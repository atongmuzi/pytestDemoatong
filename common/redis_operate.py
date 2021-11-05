import redis
from common.logger import logger
import os
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
data = data.load_ini(data_file_path)["redis"]


class RedisOperate:

    def test_redis(self, user_id):
        host = data["redis_host"]
        port = data["redis_port"]
        pwd = data["redis_pwd"]
        pool = redis.ConnectionPool(host=host, port=port, password=pwd, db=0)
        r = redis.Redis(connection_pool=pool)
        logger.info("redis缓存链接为：===>{}".format(r))
        hash_tokens_keys = "pookie:tokens:user_%s" % user_id
        token_key = "pookie:token:user_%s" % user_id
        r.delete(token_key)
        logger.info("----------清除user_id为{}的token成功----------".format(user_id))
        logger.info(len(r.hkeys(hash_tokens_keys)))
        if len(r.hkeys(hash_tokens_keys)) != 0:
            r.hdel(hash_tokens_keys, r.hkeys(hash_tokens_keys)[0])
            logger.info("----------清除user_id为{}的tokens成功----------".format(user_id))
        else:
            logger.info("----------无hash_tokens_keys为{}的tokens缓存----------".format(hash_tokens_keys))


rs = RedisOperate()
