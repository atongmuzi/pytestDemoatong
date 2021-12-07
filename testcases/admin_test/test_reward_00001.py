from common.logger import logger
from operation.admin import reward_task
from testcases.conftest import api_data
import pytest
from __future__ import division


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