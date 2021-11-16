import redis
from common.logger import logger
import os
from common.read_data import data
import re
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
data = data.load_ini(data_file_path)["redis"]
host = data["redis_host"]
port = data["redis_port"]
pwd = data["redis_pwd"]


class RedisOperate:
    def __init__(self):
        self.pool = redis.ConnectionPool(host=host, port=port, password=pwd, db=0)
        self.r = redis.Redis(connection_pool=self.pool)

    def test_redis(self, user_id):
        logger.info("redis缓存链接为：===>{}".format(self.r))
        hash_tokens_keys = "pookie:tokens:user_%s" % user_id
        token_key = "pookie:token:user_%s" % user_id
        self.r.delete(token_key)
        logger.info("----------清除user_id为{}的token成功----------".format(user_id))
        logger.info(len(self.r.hkeys(hash_tokens_keys)))
        if len(self.r.hkeys(hash_tokens_keys)) != 0:
            self.r.hdel(hash_tokens_keys, self.r.hkeys(hash_tokens_keys)[0])
            logger.info("----------清除user_id为{}的tokens成功----------".format(user_id))
        else:
            logger.info("----------无hash_tokens_keys为{}的tokens缓存----------".format(hash_tokens_keys))

    def test_token_get(self, user_id):
        logger.info("redis缓存链接为：===>{}".format(self.r))
        token_key = "pookie:token:user_%s" % user_id
        logger.info("token_key为===》{}".format(token_key))
        value = self.r.get(token_key)
        logger.info("value===》{}".format(value))
        value_str = str(value)
        logger.info("value_str==>{}".format(value_str))
        logger.info(type(value_str))
        result = re.findall(r"\"token\":\"(.*?)\"", value_str)
        logger.info("匹配结果是===》{}".format(result))
        logger.info(sys.getdefaultencoding())


rs = RedisOperate()

if __name__ == '__main__':
    rs.test_token_get(1478)
