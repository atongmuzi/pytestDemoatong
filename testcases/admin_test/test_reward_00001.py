from common.logger import logger
from operation.admin import reward_task
from testcases.conftest import api_data
import pytest


class TestAdminReward:
    """
    主要是针对发放优惠券的
    """

    @pytest.mark.parametrize("user_id,v_type,num,coupon_id", api_data["test_reward_task"])
    def test_reward_task(self, user_id, v_type, num, coupon_id):
        logger.info("开始准备手工发放正常通用券")

        result = reward_task(user_id, v_type, num, coupon_id)
        assert result.success is True, result.error
        logger.info("已经发放正常通用券完成")
