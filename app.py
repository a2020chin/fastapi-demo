# -*- coding:utf-8 -*-
"""
@Created on : 2023/1/16 12:15
@Author: sshane258
@Des: app運行時文件
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from config import settings
from fastapi.staticfiles import StaticFiles
from api.Base import ApiRouter
from core.Events import startup, stopping
from core.Exception import http_error_handler, http422_error_handler, unicorn_exception_handler, UnicornException
from core.Middleware import Middleware

application = FastAPI(
    debug=settings.APP_DEBUG,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    title=settings.PROJECT_NAME
    )


# 事件監聽
application.add_event_handler("startup", startup(application))
application.add_event_handler("shutdown", stopping(application))


# 異常錯誤處理
application.add_exception_handler(HTTPException, http_error_handler)
application.add_exception_handler(RequestValidationError, http422_error_handler)
application.add_exception_handler(UnicornException, unicorn_exception_handler)

# 路由
application.include_router(ApiRouter)

# 中間件
application.add_middleware(Middleware)
application.add_middleware(
    SessionMiddleware,
    secret_key="session",
    session_cookie="f_id",
    # max_age=4
)
application.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

# 靜態資源目錄
application.mount('/static', StaticFiles(directory=os.path.join(os.getcwd(), "static")))

app = application
