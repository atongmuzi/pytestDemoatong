from flasgger import Swagger, swag_from
from flask import Flask, request
from common.mysql_operate import db
from common.redis_operate import rs
from common.refund import re

app = Flask(__name__)
app.config["SWAGGER"] = {
    "title": "fragment",
    "version": "0.0.1"
}
Swagger(app)


@app.route('/api/fragment/', methods=['GET'])
@swag_from('/web/xml/fragment_info.yml')
def user_fragment_info():
    """
    给用户添加增加各类型碎片
    """
    userID = request.args.get("userID")
    any_fragment = request.args.get("any_fragment")
    red_fragment = request.args.get("red_fragment")
    blue_fragment = request.args.get("blue_fragment")
    purple_fragment = request.args.get("purple_fragment")
    green_fragment = request.args.get("green_fragment")
    pink_fragment = request.args.get("pink_fragment")
    white_fragment = request.args.get("white_fragment")
    black_fragment = request.args.get("black_fragment")
    brown_fragment = request.args.get("brown_fragment")
    gray_fragment = request.args.get("gray_fragment")
    if userID:
        if any_fragment:
            fragment_update(userID, any_fragment, 0)
        if red_fragment:
            fragment_update(userID, red_fragment, 1)
        if blue_fragment:
            fragment_update(userID, blue_fragment, 2)
        if purple_fragment:
            fragment_update(userID, purple_fragment, 3)
        if green_fragment:
            fragment_update(userID, green_fragment, 4)
        if pink_fragment:
            fragment_update(userID, pink_fragment, 5)
        if white_fragment:
            fragment_update(userID, white_fragment, 6)
        if black_fragment:
            fragment_update(userID, black_fragment, 7)
        if brown_fragment:
            fragment_update(userID, brown_fragment, 8)
        if gray_fragment:
            fragment_update(userID, gray_fragment, 9)
        rs.test_fragment_redis(userID)
        return "更新成功"
    else:
        return "请输入用户的userID"


def fragment_update(userID, amount, fragment_type):
    sql = "update user_fragment_info set count = count + '%s' where user_id = '%s' and type = '%s'" \
          % (amount, userID, fragment_type)
    db.execute_db(sql)


@app.route('/api/refund/', methods=['GET'])
@swag_from('/web/xml/refund_info.yml')
def user_fragment_test():
    user_id = request.args.get("userID")
    refund_num = int(request.args.get("refund_num")) if request.args.get("refund_num") is not None else 5
    refund_amount = float(request.args.get("refund_amount")) if request.args.get("refund_amount") is not None else 0.02
    result = re.test_refund(user_id, refund_num, refund_amount)
    return result


@app.route('/api/ichiban')
@swag_from('/web/xml/ichiban.yml')
def user_ichiban_test():
    return "test"


app.run(debug=True)
