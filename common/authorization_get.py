from common.redis_operate import rs
import base64
from common.logger import logger


def test_authorization_get(user_id, channel_type):
    token = rs.test_token_get(user_id)
    logger.info("token===》{}".format(token))
    token_new = str(user_id) + ":" + token + ":" + str(channel_type)
    token_new_encode = token_new.encode("utf-8")
    logger.info("token_new_encode===》{}".format(token_new_encode))
    authorization = base64.b64encode(token_new_encode)
    authorization_new = authorization.decode("utf-8")
    logger.info("authorization为===》{}".format(authorization_new))


class Authorization:
    pass


au = Authorization()

if __name__ == '__main__':
    test_authorization_get(1528, 2)
