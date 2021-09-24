"""

@Time: 2021/1/20 14:56
@Author:
@File: register.py
"""
from pyfuseki import config

def register_common_prefix(common_prefix: str):
    """
    注册公有的前缀
    :param common_prefix: 注册值
    """
    config.COMMON_PREFIX = common_prefix
