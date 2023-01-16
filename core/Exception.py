# -*- coding:utf-8 -*-
"""
@Created on : 2023/1/16 12:15
@Author: sshane258
@Des: 異常處理
"""

from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from typing import Union
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError


async def http_error_handler(_: Request, exc: HTTPException):
    """
    http異常處理
    :param _:
    :param exc:
    :return:
    """

    return JSONResponse({
        "code": exc.status_code,
        "message": exc.detail,
        "data": exc.detail
    }, status_code=exc.status_code)


class UnicornException(Exception):

    def __init__(self, code, errmsg, data=None):
        """
        失敗返回格式
        :param code:
        :param errmsg:
        """
        if data is None:
            data = {}
        self.code = code
        self.errmsg = errmsg
        self.data = data


async def unicorn_exception_handler(_: Request, exc: UnicornException):
    """
    unicorn 異常處理
    :param _:
    :param exc:
    :return:
    """
    return JSONResponse({
        "code": exc.code,
        "message": exc.errmsg,
        "data": exc.data,
    })


async def http422_error_handler(_: Request, exc: Union[RequestValidationError, ValidationError],) -> JSONResponse:
    """
    參數校正錯誤處理
    :param _:
    :param exc:
    :return:
    """
    return JSONResponse(
        {
            "code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "message": f"參數校正錯誤 {exc.errors()}",
            "data": exc.errors(),
        },
        status_code=422,
    )
