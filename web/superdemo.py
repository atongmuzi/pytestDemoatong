from flask import Flask, request
from flask_restplus import Resource, Api, fields
from spider.testcases.admin.admin_api import admin

app = Flask(__name__)
api = Api(app, version='1.0', title='superdemo api', description='更新super demo中的一些字段')
ad = api.namespace('superdemo', '/')


@ad.route("/add_white_user")
@ad.param("user_id", "需要添加进入白名单的user_id", required=True)
class white_user_add(Resource):
    def get(self):
        data = request.args
        user_id = int(data.get("user_id"))
        result = admin.modify_white_user_api(user_id, user_id + 1)
        return result


@ad.route("/add_white_user_batch")
@ad.param("end_user_id", "不包含", required=True)
@ad.param("start_user_id", "包含", required=True)
class white_user_add(Resource):
    def get(self):
        data = request.args
        start_user_id = int(data.get("start_user_id"))
        end_user_id = int(data.get("end_user_id"))
        result = admin.modify_white_user_api(start_user_id, end_user_id)
        return result


@ad.route("/add_login_white_phone")
@ad.param("phone", required=True)
class login_white_phone_add(Resource):
    def get(self):
        data = request.args
        phone = data.get("phone")
        result = admin.modify_login_white_phone_api(phone)
        return result


if __name__ == '__main__':
    app.run(debug=True)
