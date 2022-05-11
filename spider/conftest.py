import pytest
import os
import allure
import csv
from common.mysql_operate import db
from common.read_data import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


spider_data = get_data("spider_data.yml")


@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 清理数据")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")


@allure.step("清理结束==>> 清理数据")
def step_over():
    logger.info("清理结束==>> 清理数据")


@pytest.fixture(scope="session")
def fund_info_delete():
    """
        在插入当日基金数据之前，先删除以前的数据
    """
    fund_indo_delete_sql = "delete from fund_info"
    "开始清理fund_info表的历史数据"
    step_first
    db.execute_db(fund_indo_delete_sql)
    step_over


@pytest.fixture(scope="module")
def fund_csv_header_write():
    """
        在csv写入数据之前，先写入表格头部
    """
    with open("result.csv", "w")as f:
        # 写入表格头部
        header_list = ['基金代码', '更新日期', '基金净值', '涨跌幅']
        writer = csv.writer(f)
        writer.writerow(header_list)


@pytest.fixture(scope="session")
def movie_csv_header_write():
    """
        在csv写入数据之前，先写入表格头部
    """
    with open("movie_test/result/result.csv", "w")as f:
        header_list = ['更新日期', '名字', '链接', '译名', '片名', '年代', '产地', '类别']
        # 先清空文件
        f.truncate()
        # 写入表格头部
        writer = csv.writer(f)
        writer.writerow(header_list)
