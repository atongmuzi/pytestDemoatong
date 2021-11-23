from common.redis_operate import rs
import base64
from common.logger import logger


class Authorization:

    def test_authorization_get(self, user_id, channel_type):
        token = rs.test_token_get(user_id)
        if token is None:
            logger.info("=====没有找到user_id为{}的token=====".format(user_id))
            return None
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
    au.test_authorization_get(1470, 2)
