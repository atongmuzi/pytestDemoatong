from common.mysql_operate import db
from common.logger import logger
from common.random import rm
import pytest
from testcases.conftest import api_data
from common.redis_operate import rs


class TestInitPhone:
    @pytest.mark.parametrize("phone", api_data["test_init_wx"])
    def test_init_wx(self, phone):
        """批量初始化手机号为新用户"""
        sql = "select id as user_id from user where phone ='%s' " % phone
        data = db.select_db(sql)
        logger.info("data===>{}".format(data))
        for i in range(len(data)):
            logger.info(data[i]["user_id"])
            user_id = data[i]["user_id"]
            rm_result = rm.generate_random_str(10)
            phone_new = "atong"+phone + rm_result
            logger.info("随机数===>{}".format(rm_result))
            logger.info("随机更新的手机号===>{}".format(phone_new))
            sql_up_user = "update user set phone = '%s' where id ='%s'" % (phone_new, user_id)
            sql_up_wx = "update user_wechat_channel set open_id ='%s',union_id = '%s' " \
                        "where user_id ='%s'" % (phone_new, phone_new, user_id)
            logger.info("----------开始更新user表----------")
            db.execute_db(sql_up_wx)
            logger.info("----------执行更新user表成功----------")
            logger.info("----------开始更新user_wechat_channel表----------")
            db.execute_db(sql_up_user)
            logger.info("----------执行更新user_wechat_channel表成功----------")
            logger.info("----------执行清除缓存的操作----------")
            rs.test_redis(user_id)
            logger.info("----------执行清除缓存操作成功----------")

    @pytest.mark.parametrize("userID", api_data["test_init_wx_userID"])
    def test_init_wx_userID(self, userID):
        """批量初始化userID为新用户"""
        rm_result = rm.generate_random_str(10)
        phone_new = "atongtest"+userID + rm_result
        logger.info("随机数===>{}".format(rm_result))
        logger.info("随机更新的手机号===>{}".format(phone_new))
        sql_up_user = "update user set phone = '%s' , phone_encrypt = '%s'  where id ='%s'" \
                      % (phone_new, phone_new, userID)
        sql_sl_wx = "select id from user_wechat_channel where user_id = '%s' " % userID
        logger.info("----------开始更新user表----------")
        db.execute_db(sql_up_user)
        logger.info("----------执行更新user表成功----------")
        data = db.select_db(sql_sl_wx)
        for i in range(len(data)):
            wechat_id = data[i]["id"]
            logger.info("----------开始更新user_wechat_channel表----------")
            rm_result = rm.generate_random_str(10)
            phone_new = "atongtest"+userID + rm_result
            sql_up_wx = "update user_wechat_channel set open_id ='%s',union_id = '%s' " \
                        "where id ='%s'" % (phone_new, phone_new, wechat_id)
            db.execute_db(sql_up_wx)
            logger.info("----------执行更新user_wechat_channel表成功----------")
        logger.info("----------执行清除缓存的操作----------")
        rs.test_redis(userID)
        logger.info("----------执行清除缓存操作成功----------")
