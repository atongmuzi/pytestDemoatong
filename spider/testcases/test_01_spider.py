import pytest
from spider.conftest import spider_data
from spider.testcases.thirdspider import fund


class TestSpider:
    @pytest.mark.parametrize("code", spider_data["test_01_fund"])
    @pytest.mark.usefixtures("fund_info_delete", "fund_csv_header_write")
    def test_01_fund(self, code):
        fund.test_run(code)
