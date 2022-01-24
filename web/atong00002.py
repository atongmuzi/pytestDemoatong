from common.logger import logger
from flasgger import Swagger, swag_from
from flask import Flask, request
from common.mysql_operate import db

app = Flask(__name__)
app.config["SWAGGER"] = {
    "title": "pookie API",
    "version": "1.0.0"
}
Swagger(app)


@app.route('/api/userinfo/', methods=['GET'])
@swag_from('userinfo.yml')
def user_info():
    """根据手机号查询用户相关信息"""
    global user_id, nickname, phone
    phone = request.args.get("phone")
    nickname = request.args.get("nickname")
    if phone and nickname:
        sql = "select id as user_id,nickname from user where nickname ='%s' and phone = '%s' " % (nickname, phone)
        data = db.select_db(sql)
        if data:
            for i in range(len(data)):
                logger.info(data[i]["user_id"])
                user_id = data[i]["user_id"]
                nickname = data[i]["nickname"]
            json_data = {
                "手机号": phone,
                "用户ID": user_id,
                "用户昵称": nickname,
            }
            return json_data

        else:
            return "请检查输入的手机号或者昵称有无问题"
    elif phone is not None:
        sql = "select id as user_id,nickname from user where phone ='%s' " % phone
        data = db.select_db(sql)
        if data:
            for i in range(len(data)):
                logger.info(data[i]["user_id"])
                user_id = data[i]["user_id"]
                nickname = data[i]["nickname"]
            json_data = {
                "手机号": phone,
                "用户ID": user_id,
                "用户昵称": nickname,
            }
            return json_data

        else:
            return "无该手机号用户相关信息，请重新输入手机号或者昵称"
    elif nickname is not None:
        sql = "select id as user_id,nickname from user where nickname ='%s' " % nickname
        data = db.select_db(sql)
        logger.info("data===>{}".format(data))
        for i in range(len(data)):
            user_id = data[i]["user_id"]
            nickname = data[i]["nickname"]
        json_data = {
            "用户ID": user_id,
            "用户昵称": nickname
        }
        return json_data
    else:
        return "麻烦输入手机号或者昵称"


app.run(debug=True)
