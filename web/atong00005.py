from flask import Flask, request
from flask_restplus import Resource, Api, fields
from operation.admin import ichiban_insert, item_upsert, ichiban_activity_add
from common.random import rm
from common.mysql_operate import db

app = Flask(__name__)
api = Api(app, version='1.0', title='AUTH API', description='A authenticate user and save cloud accounts API')
au = api.namespace('ichiban', path='/')
ca = api.namespace('cloud accounts', path='/')
acs = api.namespace('accounts', path='/')
bca = api.namespace('binding cloud accounts', path='/')

item = au.model("Item", {
    "mash": fields.String(example="a_reward"),
    "total_count": fields.Integer(example=30),
    "detail_img": fields.String(example="https://pookie-h5.oss-cn-hangzhou.aliyuncs.com/upload"
                                        "/2c6dc2e3f4394224a0d1ff2ea9296726.jpg"),
    "is_pre_sale": fields.Boolean(example=False),
    "w_count": fields.Integer(example=0),
    "series_reward_detail_img": fields.String(example="https://pookie-h5.oss-cn-hangzhou.aliyuncs.com/upload"
                                                      "/2c6dc2e3f4394224a0d1ff2ea9296726.jpg"),
    "sku_id": fields.Integer(example=6922),
})

ichiban_item = au.model("Ichiban", {
    "item_name": fields.String(example="atongtest一番赏" + rm.generate_random_str(2)),
    "round": fields.Integer(example=1),
    "notify_num": fields.Integer(example=1),
    "item_main_imgs": fields.String(example="https://pookie-h5.oss-cn-hangzhou.aliyuncs.com/static/ichibansho"
                                            "/ichibansho-main.jpg"),
    "price": fields.Float(example=0.01),
    "sku_list": fields.List(fields.Nested(item)),
})

ichiban_activity = au.model("Activity", {
    "title": fields.String(example="atong一番赏活动"),
    "ali_title": fields.String(example="atong一番赏活动"),
    "start_time": fields.Integer(example=1647532800000),
    "end_time": fields.Integer(example=1648656000000),
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
    "limit_num": fields.Integer(example=None),
    "special_rewards": fields.String(excmple=""),
    "item_id": fields.Integer(example=915),
    "item_id_list": fields.List(fields.Integer(example=915))

})


@au.route('/add_ichiban_item', doc={"description": "新增一番赏商品且上架，返回的item_id可用于一番赏活动接口"})
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
        ichiban_activity_add(json_data)
        return "成功"


if __name__ == '__main__':
    app.run(debug=True)
