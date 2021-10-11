import pytest
import allure
from operation.order import pre_trade
from common.logger import logger


@allure.step("步骤1：下一个盲盒详情")
def step_1():
    logger.info("步骤1：下一个盲盒详情")


@allure.step("步骤2：pick一个盒子")
def step_2():
    logger.info("步骤2：pick一个盒子")


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("真正下单之前的预下单--获取一些关键信息")
class TestTradePreOrder:
    """真正下单之前的预下单--获取一些关键信息"""
    def test_trade_preorder(self, testcase_data):
        order_type = testcase_data["order_type"]
        tem_id = testcase_data["tem_id"]
        sku_type = testcase_data["sku_type"]
        sku_no = testcase_data["sku_no"]
        act_id_list = testcase_data["act_id_list"]
        use_pcoin = testcase_data["use_pcoin"]
        except_result = testcase_data["except_result"]
        except_code = testcase_data["except_code"]
        logger.info("*************** 开始执行用例 *************** /n")
        logger.info(order_type)
        result = pre_trade(order_type, tem_id, sku_type, sku_no, act_id_list, use_pcoin)
        logger.info(result.success)
        logger.info(result.data)

