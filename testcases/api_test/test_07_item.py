import pytest
import allure
from operation.item import item_next_true, item_pick_sku
from common.logger import logger
import random


@allure.step("步骤1：下一个盲盒详情")
def step_1():
    logger.info("步骤1：下一个盲盒详情")


@allure.step("步骤2：盲盒的最新状态")
def step_2():
    logger.info("步骤2：盲盒的最新状态")


@allure.step("步骤3：pick一个盒子")
def step_3():
    logger.info("步骤3：pick一个盒子")


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("盲盒详情")
class TestTradePreItem:
    sku_no = ""
    box_no = ""
    """下一个盲盒详情"""
    @allure.story("下一个盲盒详情")
    @pytest.fixture()
    def test_item_next(self):
        step_1()
        item_id = 378
        first_random = True
        logger.info("*************** 开始执行用例 *************** /n")
        result = item_next_true(item_id, first_random)
        itemSelect.box_no = result.data["mbox"]["box_no"]
        index = random.randint(0, 5)
        itemSelect.sku_no = result.data["mbox"]["cell_list"][index]["sku_no"]
        logger.info(itemSelect.sku_no)
        logger.info("*************** 结束执行用例 *************** /n")
        if result.success:
            return True
        else:
            return False

    """选中其中一个盒子"""
    @allure.story("选中一个盒子")
    def test_item_pick(self, test_item_next):
        next_result = test_item_next
        step_3()
        if next_result:
            item_id = 378
            sku_no_pick = itemSelect.sku_no
            logger.info("*************** 开始执行用例 *************** /n")
            result = item_pick_sku(item_id, sku_no_pick)
            logger.info(result.success)
            logger.info(result.data)
            logger.info("*************** 结束执行用例 *************** /n")
        else:
            logger.info("**********该案例的前置案例--》test_item_next未执行或执行失败************")


itemSelect = TestTradePreItem()




