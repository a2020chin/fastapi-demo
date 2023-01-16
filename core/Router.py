# -*- coding:utf-8 -*-
"""
@Created on : 2023/1/16 12:15
@Author: sshane258
@Des: 路由整合
"""

from api.Base import ApiRouter
from views.Base import ViewsRouter
from fastapi import APIRouter

AllRouter = APIRouter()
# 視圖路由
AllRouter.include_router(ViewsRouter)
# API路由
AllRouter.include_router(ApiRouter)
