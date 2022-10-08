from flask import Flask, request, render_template
from flask_restplus import Resource, Api

app = Flask(__name__)
# api = Api(app)


@app.route('/', methods=['GET', 'POST'])
def index(download_xml=None):
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
