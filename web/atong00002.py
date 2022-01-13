from common.logger import logger
from flasgger import Swagger, swag_from
from flask import Flask, request
from common.mysql_operate import db

app = Flask(__name__)
Swagger(app)


@app.route('/api/userinfo/', methods=['GET'])
@swag_from('userinfo.yml')
def user_info():
    """根据手机号查询用户相关信息"""
    global user_id, nickname
    phone = request.args.get('phone', 1)
    sql = "select id as user_id,nickname from user where phone ='%s' " % phone
    data = db.select_db(sql)
    size = int(request.args.get('size', 1))
    logger.info("data===>{}".format(data))
    for i in range(len(data)):
        logger.info(data[i]["user_id"])
        user_id = data[i]["user_id"]
        nickname = data[i]["nickname"]
    json_data = {
        "用户ID": user_id,
        "用户昵称": nickname,
        "长度": size
    }
    return json_data


app.run(debug=True)
