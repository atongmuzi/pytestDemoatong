import pytest
from spider.conftest import spider_data


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return spider_data.get(testcase_name)