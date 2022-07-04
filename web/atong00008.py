from flask import Flask
from flask_restplus import Api, fields, Resource, marshal

app = Flask(__name__)
api = Api()
api.init_app(app)

metadata_model = api.model("metadata", {
    'file': fields.String()
})

user_model = api.model('UserModel', {
          "user_id": fields.Integer(required=True, description=''),
          "user_name": fields.String(required=True, description=''),
          "user_role": fields.String(required=False, description='')
})

response_model = api.model("Result", {
    'metadata': fields.List(fields.Nested(metadata_model)),
    'result': fields.Raw()
})


@api.route("/test")
class ApiView(Resource):

    @api.marshal_with(response_model)
    def get(self):

        data = {'metadata': {},
                'result': self.get_user()}
        return data


    def get_user(self):
        # Access database and get data
        user_data = [{'user_id': 1, 'user_name': 'John', 'user_role': 'editor'},
                     {'user_id': 2, 'user_name': 'Sue', 'user_role': 'curator'}]

        # The kwarg envelope does the trick
        return marshal(user_data, user_model, envelope='data')


app.run(host='127.0.0.1', debug=True)
