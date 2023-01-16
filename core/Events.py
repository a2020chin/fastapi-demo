# -*- coding:utf-8 -*-
"""
@Created on : 2023/1/16 12:15
@Author: sshane258
@Des: fastapi事件監聽
"""

from typing import Callable
from fastapi import FastAPI


def startup(app: FastAPI) -> Callable:
    """
    FastApi 啟動完成事件
    :param app: FastAPI
    :return: start_app
    """
    async def app_start() -> None:
        # APP啟動完成後觸發
        print("啟動完畢")
        pass
    return app_start


def stopping(app: FastAPI) -> Callable:
    """
    FastApi 停止事件
    :param app: FastAPI
    :return: stop_app
    """
    async def stop_app() -> None:
        # APP停止時觸發
        print("停止")
        pass

    return stop_app
