# -*- coding: utf-8 -*-
'''
PROJECT_NAME：login-flask 
FILE:__init__.py 
USERNAME: 李宏伟
DATE:2020/1/16 
TIME:上午9:53 
PRODUCT_NAME:PyCharm 
'''


from flask import Blueprint

user_blue = Blueprint('user', __name__, url_prefix='/user')

from . import views