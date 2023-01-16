# -*- coding:utf-8 -*-
"""
@Created on : 2023/1/16 12:15
@Author: sshane258
@Des: 基本路由
"""
from fastapi import APIRouter

from api.login import index, login

ApiRouter = APIRouter(prefix="/v1", tags=["api路由"])


@ApiRouter.get('/')
async def home(num: int):
    return {"num": num, "data": [{"num": num, "data": []}, {"num": num, "data": []}]}

ApiRouter.get("/index", tags=["api路由"], summary="註冊接口")(index)
ApiRouter.get("/login", tags=["api路由"], summary="登入接口")(login)
