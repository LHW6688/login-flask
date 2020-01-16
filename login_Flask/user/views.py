# -*- coding: utf-8 -*-
'''
PROJECT_NAME：login-flask 
FILE:viwes 
USERNAME: 李宏伟
DATE:2020/1/16 
TIME:上午9:56 
PRODUCT_NAME:PyCharm 
'''
from flask import request, jsonify, current_app
from werkzeug.security import check_password_hash

from login_Flask.user import user_blue
from login_Flask.utils import response_code


@user_blue.route('/user/login', methods=['POST'])
def login():
    """登录"""
    # 接受参数（账号，密码）
    id = request.json.get('id')
    pwd = request.json.get('pwd')
    # 校验参数是否缺少
    if not all([id, pwd]):
        return jsonify(err_code=response_code.RET.PARAMERR, content='缺少参数')
    try:
        id = str(id)
        pwd = str(pwd)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(err_code=response_code.RET.PARAMERR, content='参数类型错误')
    if check_str_is_cn(id):
        return jsonify(err_code=response_code.RET.PARAMERR, content='账号格式错误')
    if not id.replace('_', '').isalnum():
        return jsonify(err_code=response_code.RET.PARAMERR, content='账号格式错误')
    if len(id) > ID_MAX_LEN or len(id) < ID_MIN_LEN:
        return jsonify(err_code=response_code.RET.PARAMERR, content='账号长度请设置在{}到{}之间'.format(ID_MIN_LEN, ID_MAX_LEN))
    if check_str_is_cn(pwd):
        return jsonify(err_code=response_code.RET.PARAMERR, content='密码格式错误')
    if len(pwd) > PWD_MAX_LEN or len(pwd) < PWD_MIN_LEN:
        return jsonify(err_code=response_code.RET.PARAMERR, content='密码长度请设置在{}到{}之间'.format(PWD_MIN_LEN, PWD_MAX_LEN))
    # 链接数据库
    curs = g.db_obj.curs
    # 查询此次注册的账号是否已经使用
    try:
        curs.execute("select PASSWORD, STATUS, IS_ADMIN, ID, NAME, MOBILE from EC_USER WHERE ID = '{}'".format(id))
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(err_code=response_code.RET.DBERR, content='查询数据失败')
    user = curs.fetchone()
    if not user:
        return jsonify(err_code=response_code.RET.NODATA, content='用户名或密码错误')
    # 如果用户存在，校验密码是否正确
    if not check_password_hash(user[0], pwd):
        return jsonify(err_code=response_code.RET.PWDERR, content='用户名或密码错误')
    status = user[1]
    is_admin = True if user[2] else False
    # 生成token
    auto = Auth()
    try:
        id_code = auto.encode_auth_token(id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(err_code=response_code.RET.LOGINERR)