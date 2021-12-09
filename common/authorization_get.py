from common.redis_operate import rs
import base64
from common.logger import logger


class Authorization:
    """
    platform_type = 1表示微信小程序端，2表示管理端
    """
    def test_authorization_get(self, user_id, platform_type, **kwargs):
        token = rs.test_token_get(user_id, platform_type)
        channel_type = dict(**kwargs).get("channel_type")
        if token is None:
            logger.info("=====没有找到user_id为{}的token=====".format(user_id))
            return None
        elif channel_type is None:
            logger.info("token=====》{}".format(token))
            token_new = str(user_id) + ":" + token
            token_new_encode = token_new.encode("utf-8")
            logger.info("token_new_encode=====》{}".format(token_new_encode))
            authorization = base64.b64encode(token_new_encode)
            authorization_new = authorization.decode("utf-8")
            logger.info("Authorization为=====》{}".format(authorization_new))
            return authorization_new
        else:
            logger.info("token=====》{}".format(token))
            token_new = str(user_id) + ":" + token + ":" + str(channel_type)
            token_new_encode = token_new.encode("utf-8")
            logger.info("token_new_encode=====》{}".format(token_new_encode))
            authorization = base64.b64encode(token_new_encode)
            authorization_new = authorization.decode("utf-8")
            logger.info("Authorization为=====》{}".format(authorization_new))
            return authorization_new


au = Authorization()

if __name__ == '__main__':
    au.test_authorization_get(57, 2)
