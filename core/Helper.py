# -*- coding:utf-8 -*-
"""
@Created on : 2023/1/16 12:15
@Author: sshane258
@Des: 工具函數
"""

import hashlib
import uuid


def random_str():
    """
    唯一隨機字符串
    :return: str
    """
    only = hashlib.md5(str(uuid.uuid1()).encode(encoding='UTF-8')).hexdigest()
    return str(only)
