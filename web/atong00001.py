from common.logger import logger
from flasgger import Swagger, swag_from
from flask import Flask
from common.random import rm
from common.mysql_operate import db
from common.redis_operate import rs
app = Flask(__name__)
Swagger(app)


@app.route('/api/<string:phone>/', methods=['GET'])
@swag_from('index.yml')
def test_init_wx(phone):
    """批量初始化手机号为新用户"""
    sql = "select id as user_id from user where phone ='%s' " % phone
    data = db.select_db(sql)
    logger.info("data===>{}".format(data))
    for i in range(len(data)):
        logger.info(data[i]["user_id"])
        user_id = data[i]["user_id"]
        rm_result = rm.generate_random_str(10)
        phone_new = phone + rm_result
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
    return "初始化成功"


app.run(debug=True)
