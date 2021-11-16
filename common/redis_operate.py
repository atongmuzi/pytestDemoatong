import redis
from common.logger import logger
import os
from common.read_data import data
import re
import sys

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

    def test_token_get(self, user_id):
        host = data["redis_host"]
        port = data["redis_port"]
        pwd = data["redis_pwd"]
        pool = redis.ConnectionPool(host=host, port=port, password=pwd, db=0)
        r = redis.Redis(connection_pool=pool)
        logger.info("redis缓存链接为：===>{}".format(r))
        token_key = "pookie:token:user_%s" % user_id
        logger.info("token_key为===》{}".format(token_key))
        value = r.get(token_key)
        logger.info("value===》{}".format(value))
        value_new = value.decode("utf-16")
        logger.info("解码后的value_new为：===》{}，type是{}".format(value_new, type(value_new)))
        result = re.findall(r"\"token\":\"(.*)\"", value_new)
        logger.info("匹配结果是===》{}".format(result))
        s_str = "中文"
        b_str = bytes(s_str, encoding="utf-16")
        logger.info(b_str)
        str_new = str(b_str, encoding="utf-16")
        logger.info(str_new)
        logger.info(sys.getdefaultencoding())


rs = RedisOperate()

if __name__ == '__main__':
    rs.test_token_get(1478)
