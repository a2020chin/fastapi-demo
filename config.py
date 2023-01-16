# -*- coding:utf-8 -*-
"""
@Created on : 2023/1/16 12:15
@Author: sshane258
@Des: 基本配置文件
"""

import os.path
from pydantic import BaseSettings
from typing import List


class Config(BaseSettings):
    # 調適模式
    APP_DEBUG: bool = True
    # 項目訊息
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "光遇fastapi-demo"
    DESCRIPTION: str = '光遇api'
    # 靜態資源目錄
    STATIC_DIR: str = os.path.join(os.getcwd(), "static")  # os模塊系統配置 getcwd獲取工作目錄(app.py)
    TEMPLATE_DIR: str = os.path.join(STATIC_DIR, "templates")

    # 跨域請求
    CORS_ORIGINS: List[str] = ['*']
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ['*']
    CORS_ALLOW_HEADERS: List[str] = ['*']


settings = Config()
