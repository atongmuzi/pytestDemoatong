import pytest
import allure
import json
from operation.user import get_all_user_info, get_one_user_info
from testcases.conftest import api_data
from common.logger import logger


@allure.step("步骤1 ==>> 获取所有用户信息")
def step_1():
    logger.info("步骤1 ==>> 获取所有用户信息".f)


@allure.step("步骤1 ==>> 获取某个用户信息")
def step_2(username):
    logger.info("步骤1 ==>> 获取某个用户信息：{}".format(username))
    logger.info("dd".format())


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("获取用户信息模块")
class TestGetUserInfo():
    """获取用户信息模块"""

    @allure.story("用例--获取全部用户信息")
    @allure.description("该用例是针对获取所有用户信息接口的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.webtest
    @pytest.mark.parametrize("except_result, except_code, except_msg",
                             api_data["test_get_all_user_info"])
    def test_get_all_user_info(self, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        step_1()
        result = get_all_user_info()
        # print(result.__dict__)
        text = result.response.text
        textjson = json.loads(text)
        favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
        for name, language in favorite_languages.items():
            print(name.title())
            print(language.title())

        print(textjson['data'])

        print(result.msg)
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        # logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        # assert result.response.json().get("code") == except_code
        # assert except_msg in result.msg
        # logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--获取某个用户信息")
    @allure.description("该用例是针对获取单个用户信息接口的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {username}，{except_result}，{except_code}，{except_msg} 】")
    @pytest.mark.single1
    @pytest.mark.parametrize("username, except_result, except_code, except_msg",
                             api_data["test_get_get_one_user_info"])
    def test_get_get_one_user_info(self, username, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        print("atongtest")
    #     step_2(username)
    #     result = get_one_user_info(username)
    #     # print(result.__dict__)
    #     assert result.response.status_code == 200
    #     assert result.success == except_result, result.error
    #     logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
    #     assert result.response.json().get("code") == except_code
    #     assert except_msg in result.msg
    #     logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main([ "-s", "test_01_get_user_info.py", "-m=webtest"])
