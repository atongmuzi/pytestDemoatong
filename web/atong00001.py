from common.logger import logger
from flasgger import Swagger, swag_from
from flask import Flask

app = Flask(__name__)
Swagger(app)


@app.route('/api/<string:phone>/', methods=['GET'])
@swag_from('index.yml')
def index(phone):

    logger.info("phone===>{}".format(phone))
    if phone:
        return phone
    else:
        return "haha"


app.run(debug=True)
