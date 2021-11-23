#!/usr/bin/env python3
# coding: utf-8
# 配置文件
import os
import sys
from common.logger import logger


class Config(object):  # 默认配置
    DEBUG = False

    # get attribute
    def __getitem__(self, key):
        return self.__getattribute__(key)


class ProductionConfig(Config):  # 测试环境2
    # url地址
    api_root_url = "https://test2api.pookie.com.cn"
    # redis 地址配置
    redis_host = "192.168.4.5"
    redis_port = 6379
    redis_pwd = "0.123abc"
    # mysql 地址配置
    MYSQL_HOST = "192.168.4.5"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PASSWD = "0.123abc"
    MYSQL_DB = "pookie"


class DevelopmentConfig(Config):  # 测试环境
    # url地址
    api_root_url = "https://testapi.pookie.com.cn"
    # redis 地址配置
    redis_host = "192.168.4.4"
    redis_port = 6379
    redis_pwd = "0.123abc"
    # mysql 地址配置
    MYSQL_HOST = "192.168.4.4"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PASSWD = "0.123abc"
    MYSQL_DB = "pookie"


# 环境映射关系
mapping = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
#
# 一键切换环境
APP_ENV = os.environ.get('APP_ENV', 'production').lower()  # 设置环境变量为default
config = mapping[APP_ENV]()  # 获取指定的环境

# 根据脚本参数，来决定用那个环境配置

#
# print(sys.argv)
# logger.info("环境是:{}".format(sys.argv))
# logger.info("sys.argv[1]是{}".format(sys.argv[1]))
# num = len(sys.argv) - 1  # 参数个数
# if num < 1 or num > 1:
#     exit("参数错误,必须传环境变量!比如: python xx.py dev|pro|default")
#
# env = sys.argv[1]  # 环境
# # print(env)
# APP_ENV = os.environ.get('APP_ENV', env).lower()
# config = mapping[APP_ENV]()  # 实例化对应的环境
