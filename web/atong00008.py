from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)
# app.config['ERROR_404_HELP'] = False

todos = {"a": "haha", "b": "hehe"}


@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        print("atong"+todos)
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


if __name__ == '__main__':
    app.run(debug=True)
