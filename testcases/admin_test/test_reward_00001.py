from common.logger import logger
from operation.admin import reward_task
from testcases.conftest import api_data
import pytest


class TestAdminReward:
    """
    主要是针对发放优惠券
    """

    @pytest.mark.parametrize("user_id,v_type,coupon_id", api_data["test_reward_task"])
    def test_reward_task_com(self, user_id, v_type, coupon_id):
        """
        发放券===》1元通用券
        """
        logger.info("开始准备手工发放正常通用券")
        result = reward_task(user_id, v_type, coupon_id)
        assert result.success is True, result.error
        logger.info("已经发放正常通用券完成")

    @pytest.mark.parametrize("user_id,v_type,coupon_id", api_data["test_reward_task_exp"])
    def test_reward_task_exp(self, user_id, v_type, coupon_id):
        """
        发放券===》体验券
        """
        logger.info("开始准备手工发放正常通用券")
        result = reward_task(user_id, v_type, coupon_id)
        assert result.success is True, result.error
        logger.info("已经发放正常通用券完成")

    @pytest.mark.parametrize("user_id,v_type,skill_card_id,valid_day", api_data["test_reward_task_tips_card"])
    def test_reward_task_tips_card(self, user_id, v_type, skill_card_id, valid_day):
        """
        发放技能卡===》提示卡
        """
        logger.info("开始准备发放技能卡===》提示卡")
        result = reward_task(user_id, v_type, skill_card_id, valid_day=valid_day)
        assert result.success is True, result.error
        logger.info("接口返回信息：code期望结果【0】,实际结果【{}】；msg期望结果【success】，实际结果【{}】".format(result.code, result.msg))
        logger.info("接口返回data信息：==》{}".format(result.data))
        logger.info("已经发放技能卡==》提示卡完成")
