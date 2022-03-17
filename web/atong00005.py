from flask import Flask, request
from flask_restplus import Resource, Api, fields
from operation.admin import ichiban_insert

app = Flask(__name__)
api = Api(app, version='1.0', title='AUTH API', description='A authenticate user and save cloud accounts API')
au = api.namespace('auth', path='/')
ca = api.namespace('cloud accounts', path='/')
acs = api.namespace('accounts', path='/')
bca = api.namespace('binding cloud accounts', path='/')

person = au.model('Person', {
    'mash': fields.String(example='a_reward'),
    'total_count': fields.Integer(example=30),
    'detail_img': fields.String(example='https://pookie-h5.oss-cn-hangzhou.aliyuncs.com/upload'
                                        '/2c6dc2e3f4394224a0d1ff2ea9296726.jpg'),
    'is_pre_sale': fields.Boolean(example=False),
    'w_count': fields.Integer(example=0),
    'series_reward_detail_img': fields.String(example='https://pookie-h5.oss-cn-hangzhou.aliyuncs.com/upload'
                                                      '/2c6dc2e3f4394224a0d1ff2ea9296726.jpg'),
    'sku_id': fields.Integer(example=6922),
})

school = au.model('School', {
    'item_name': fields.String(example='atongtest一番赏'),
    'round': fields.Integer(example=1),
    'item_main_imgs': fields.String(example='https://pookie-h5.oss-cn-hangzhou.aliyuncs.com/static/ichibansho'
                                            '/ichibansho-main.jpg'),
    'price': fields.Float(example=0.01),
    'sku_list': fields.List(fields.Nested(person)),
})


@au.route('/hello')
class HelloWorld(Resource):
    @au.marshal_with(school, as_list=True)
    @au.expect(school)
    def post(self):
        json_data = request.json
        result = ichiban_insert(json_data)
        return result


if __name__ == '__main__':
    app.run(debug=True)
