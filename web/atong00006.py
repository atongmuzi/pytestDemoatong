from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {"todo1":"hahha", "tudo2":"heheh"}


@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        a = todos.get("todo1")
        return {todo_id: a}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


if __name__ == '__main__':
    app.run(debug=True)
