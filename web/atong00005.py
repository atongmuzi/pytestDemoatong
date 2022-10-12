from flask import Flask, request, render_template
from flask_restplus import Resource, Api, fields

from common.refund import re
from common.user_init import init
from operation.admin import ichiban_insert, item_upsert, ichiban_activity_add
from common.random import rm
from common.mysql_operate import db
from spider.testcases.admin.admin_api import admin
from common.exchange_init import ex
import time
from common.common_snowflake_reward import snr

app = Flask(__name__)
api = Api(app, version='1.0', title='AUTH API', description='A authenticate user and save cloud accounts API')
au = api.namespace('ichiban', path='/')
ad = api.namespace('superdemo', path='/')
af = api.namespace('refund', path='/')
ai = api.namespace('user_init', path='/')
ae = api.namespace('exchange_init', path='/')
asr = api.namespace('snowflake_reward_init', path='/')

item1 = au.model("item1", {
    "mash": fields.String(example="c_reward"),
    "total_count": fields.Integer(example=30),
    "org_price": fields.Float(example=20.88),
    "detail_img": fields.String(example="https://pookie-h5.oss-cn-hangzhou.aliyuncs.com/upload"
                                        "/2c6dc2e3f4394224a0d1ff2ea9296726.jpg"),
    "is_pre_sale": fields.Boolean(example=False),
    "series_reward_detail_img": fields.String(example="https://pookie-h5.oss-cn-hangzhou.aliyuncs.com/upload"
                                                      "/2c6dc2e3f4394224a0d1ff2ea9296726.jpg"),
    "cost_price": fields.Float(example=20.99),
    "special_type": fields.String(example="mbox_bad"),
    "sku_id": fields.Integer(example=6922)
})

ichiban_item = au.model("Ichiban", {
    "item_name": fields.String(example="atongtest一番赏" + rm.generate_random_str(2)),
    "round": fields.Integer(example=1),
    "notify_num": fields.Integer(example=1),
    "item_main_imgs": fields.String(example="https://pookie-h5.oss-cn-hangzhou.aliyuncs.com/static/ichibansho"
                                            "/ichibansho-main.jpg"),
    "price": fields.Float(example=0.03),
    "sku_list": fields.List(fields.Nested(item1)),
    "support_three_choose": fields.Boolean(example=0),
    "three_choose_price": fields.Float(example=0),
    "three_choose_recovery_price": fields.Float(example=0),
    "notify_num": fields.Float(example=50),
    "series_recovery_amount": fields.Float(example=0.13)
    # "sku_list": fields.List(fields.Raw)
})

ichiban_activity = au.model("Activity", {
    "title": fields.String(example="atong一番赏活动"),
    "ali_title": fields.String(example="atong一番赏活动"),
    "start_time": fields.Integer(example=int(time.time() * 1000)),
    "end_time": fields.Integer(example=1689824012000),
    "price": fields.Float(example=1),
    "original_price": fields.Float(example=1),
    "status": fields.Boolean(example=False),
    "detail_image": fields.String(example="https://pookie-h5.oss-cn-hangzhou.aliyuncs.com/upload"
                                          "/459deb76a2814b169b2dbbeabd87d449.jpeg"),
    "share_title": fields.String(example="我是atong一番赏活动分享标题"),
    "share_pic": fields.String(example="https://pookie-h5.oss-cn-hangzhou.aliyuncs.com/upload"
                                       "/bd0e7135822f47918a008bc372d728a3.png"),
    "image": fields.String(example="https://pookie-h5.oss-cn-hangzhou.aliyuncs.com/upload"
                                   "/0a4acfaee477448cac852f683a5972f2.png"),
    "tags": fields.String(example="[]"),
    "description": fields.String(example="atong一番赏活动"),
    "limit_num": fields.Integer(example=2),
    "special_rewards": fields.String(example=""),
    "item_id": fields.Integer(example=915),
    "item_id_list": fields.List(fields.Integer(example=915))

})


@au.route('/add_ichiban_item_nomal', doc={"description": "新增一番赏(普通且非三选一)商品且上架，返回的item_id可用于一番赏活动接口"})
class HelloWorld(Resource):
    # @au.marshal_with(school, as_list=True)
    @au.expect(ichiban_item)
    def post(self):
        json_data = request.json
        '新增一番赏商品--尚未上架'
        ichiban_insert(json_data)
        '上架新增的一番赏商品--上架功能'
        sql = 'select id from item where bg_category_id = 4 order by id desc limit 1'
        data = db.select_db(sql)
        item_upsert(data[0]["id"], 2)
        return {"item_id": data[0]["id"]}


@au.route("/add_ichiban_activity")
class ichiban_activity(Resource):
    @au.expect(ichiban_activity)
    def post(self):
        json_data = request.json
        result = ichiban_activity_add(json_data)
        if result.error:
            return result.error
        else:
            return "成功"


@ad.route("/add_white_user")
@ad.param("user_id", "需要添加进入白名单的user_id", required=True)
class white_user_add(Resource):
    def get(self):
        data = request.args
        user_id = int(data.get("user_id"))
        result = admin.modify_white_user_api(user_id, user_id + 1)
        return result


@ad.route("/select_white_user_list")
class select_white_user(Resource):
    def get(self):
        result = admin.select_white_user_last()
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


@af.route('/refund')
@af.param("refund_num", "需退款数量,默认为5条")
@af.param("refund_amount", "最小退款金额，默认为0.02")
@af.param("userID", "需退款用户的ID", required=True)
class user_refund_test(Resource):
    def get(self):
        user_id = request.args.get("userID")
        refund_num = int(request.args.get("refund_num")) if request.args.get("refund_num") is not None else 5
        refund_amount = float(request.args.get("refund_amount")) if request.args.get(
            "refund_amount") is not None else 0.02
        result = re.test_refund(user_id, refund_num, refund_amount)
        return result


@ai.route('/user_init')
@ai.param("user_id", "需初始化用户的ID", required=True)
class user_init(Resource):
    def get(self):
        user_id = request.args.get("userID")
        init.init_wx_userID(user_id)


@ae.route('/exchange_init')
class exchange_init(Resource):
    def get(self):
        code = ex.all_init()
        if code:
            return "许愿换娃数据初始化成功"


@asr.route('/reward_config_init')
@asr.param("type", "活动类型", required=True)
@asr.param("reward_type", "需要初始化的奖励类型，1-实物 2-技能卡 3-优惠券", required=True)
class snowflake_reward_init(Resource):
    def get(self):
        type = request.args.get("type")
        reward_type = request.args.get("reward_type")
        result = snr.common_snowflake_reward(type, reward_type)
        return result


@asr.route('/consumption_value_init')
@asr.param("user_id", "用户user_id", required=True)
@asr.param("value", "可用消费值", required=True)
@asr.param("rest_num", "可用体力等数量", required=True)
class snowflake_reward_init(Resource):
    def get(self):
        user_id = request.args.get("user_id")
        value = int(request.args.get("value"))
        rest_num = int(request.args.get("rest_num"))
        result = snr.common_consumption_value(user_id, value, rest_num)
        return result


if __name__ == '__main__':
    app.run(debug=True)
