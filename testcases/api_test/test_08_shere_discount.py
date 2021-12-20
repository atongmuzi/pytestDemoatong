from common.logger import logger
from operation.share_discount import share_friend_boost_param
import pytest
import allure
from testcases.conftest import base_data


@allure.step("步骤1：好友给用户助力")
def step_1():
    logger.info("步骤1：好友给用户助力")


class TestShareDiscount:

    @allure.story("好友给用户助力")
    @pytest.mark.usefixtures("delete_user_share_discount_boost")
    def test_share_friend_boost(self):
        item_id = base_data["init_item"]["item_id"]
        """
        好友给用户助力
        """
        logger.info("*************** 开始执行用例 *************** /n")
        result = share_friend_boost_param(item_id)
        assert result.success is True, result.error
        logger.info("接口返回信息：code期望结果【0】,实际结果【{}】；msg期望结果【success】，实际结果【{}】".format(result.code, result.msg))
        logger.info(result.data)
        logger.info("*************** 执行用例结束 *************** /n")



