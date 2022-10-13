import pytest
import os
import allure
from api.user import user
from common.mysql_operate import db
from common.read_data import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


base_data = get_data("base_data.yml")
api_data = get_data("api_test_data.yml")
scenario_data = get_data("scenario_test_data.yml")
table_data = get_data("table_data.yml")
user_id = base_data["init_user"]["user_id"]
friend_user_id = base_data["init_user"]["friend_id"]
coupon_id = base_data["init_coupon"]["coupon_id"]


@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 清理数据")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")


@allure.step("前置步骤 ==>> 管理员用户登录")
def step_login(username, password):
    logger.info("前置步骤 ==>> 管理员 {} 登录，返回信息 为：{}".format(username, password))


@pytest.fixture(scope="session")
def login_fixture():
    username = base_data["init_admin_user"]["username"]
    password = base_data["init_admin_user"]["password"]
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "username": username,
        "password": password
    }
    loginInfo = user.login(data=payload, headers=header)
    step_login(username, password)
    yield loginInfo.json()


@pytest.fixture(scope="function")
def insert_delete_user():
    """删除用户前，先在数据库插入一条用户数据"""
    insert_sql = base_data["init_sql"]["insert_delete_user"][0]
    db.execute_db(insert_sql)
    step_first()
    logger.info("删除用户操作：插入新用户--准备用于删除用户")
    logger.info("执行前置SQL：{}".format(insert_sql))
    yield
    # 因为有些情况是不给删除管理员用户的，这种情况需要手动清理上面插入的数据
    del_sql = base_data["init_sql"]["insert_delete_user"][1]
    db.execute_db(del_sql)
    step_last()
    logger.info("删除用户操作：手工清理处理失败的数据")
    logger.info("执行后置SQL：{}".format(del_sql))


@pytest.fixture(scope="function")
def delete_register_user():
    """注册用户前，先删除数据，用例执行之后，再次删除以清理数据"""
    del_sql = base_data["init_sql"]["delete_register_user"]
    db.execute_db(del_sql)
    step_first()
    logger.info("注册用户操作：清理用户--准备注册新用户")
    logger.info("执行前置SQL：{}".format(del_sql))
    yield
    db.execute_db(del_sql)
    step_last()
    logger.info("注册用户操作：删除注册的用户")
    logger.info("执行后置SQL：{}".format(del_sql))


@pytest.fixture(scope="function")
def update_user_telephone():
    """修改用户前，因为手机号唯一，为了使用例重复执行，每次需要先修改手机号，再执行用例"""
    update_sql = base_data["init_sql"]["update_user_telephone"]
    db.execute_db(update_sql)
    step_first()
    logger.info("修改用户操作：手工修改用户的手机号，以便用例重复执行")
    logger.info("执行SQL：{}".format(update_sql))


@pytest.fixture(scope="function")
def delete_user_share_discount_boost():
    """
    在助力领取大额券之前，因为不能重复领取，所以先清除好友助力记录，以及领取记录表
    """
    delete_sql_boost = "delete from  act_share_discount_friend_boost_log where user_id ='%s' " \
                       "and friend_user_id ='%s' " % (friend_user_id, user_id)

    delete_sql_discount_user = "delete from act_share_discount_user_log where user_id in('%s','%s')" % (
        friend_user_id, user_id)
    step_first()
    logger.info("=====开始清理act_share_discount_friend_boost_log表=====")
    db.execute_db(delete_sql_boost)
    logger.info("=====清理act_share_discount_friend_boost_log表结束=====")
    logger.info("=====开始清理act_share_discount_user_log表=====")
    db.execute_db(delete_sql_discount_user)
    logger.info("=====清理act_share_discount_user_log表结束=====")


@pytest.fixture(scope="function")
def delete_user_coupon():
    """
    领取大额券时，需要先清除已经领取的该大额券
    """
    delete_sql_coupon = "delete from user_coupon where user_id in('%s','%s') and coupon_id = '%s' " \
                        % (user_id, friend_user_id, coupon_id)
    step_first()
    logger.info("=====开始清理user_coupon表=====")
    db.execute_db(delete_sql_coupon)
    logger.info("=====清理user_coupon表结束=====")
    logger.info("=====清理表数据结束=====")


