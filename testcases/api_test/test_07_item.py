import pytest
import allure
from operation.item import item_next_true,item_pick_sku
from common.logger import logger


@allure.step("步骤1：下一个盲盒详情")
def step_1():
    logger.info("步骤1：下一个盲盒详情")


@allure.step("步骤2：pick一个盒子")
def step_2():
    logger.info("步骤2：pick一个盒子")


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("下一个盲盒详情")
class TestTradePreOrder:
    """下一个盲盒详情"""
    def test_item_next(self):
        item_id = 378
        first_random = True
        logger.info("*************** 开始执行用例 *************** /n")
        result = item_next_true(item_id, first_random)
        logger.info(result.success)
        logger.info(result.data)

    def test_item_pick(self):
        item_id = 378
        sku_no = "20210910424640020014373-1"
        logger.info("*************** 开始执行用例 *************** /n")
        result = item_pick_sku(item_id, sku_no)
        logger.info(result.success)
        logger.info(result.data)





