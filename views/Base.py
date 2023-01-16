# -*- coding:utf-8 -*-
"""
@Created on : 2023/1/16 12:15
@Author: sshane258
@Des: 試圖路由
"""

from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config import settings

ViewsRouter = APIRouter()

templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)


@ViewsRouter.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})