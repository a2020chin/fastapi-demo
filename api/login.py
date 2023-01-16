# -*- coding:utf-8 -*-
"""
@Created on : 2023/1/16 12:15
@Author: sshane258
@Des: 登入測試
"""

from typing import List
from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str
    user: List[int]


def index(age: int):
    return {"fun": "/index", "age": age}


def login(data: Login):
    return data
