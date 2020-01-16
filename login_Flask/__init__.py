# -*- coding: utf-8 -*-
'''
PROJECT_NAME：login-flask 
FILE:__init__.py 
USERNAME: 李宏伟
DATE:2020/1/16 
TIME:上午9:44 
PRODUCT_NAME:PyCharm 
'''
import redis
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect, generate_csrf

from config import config_map

db = SQLAlchemy()
redis_store = None


def create_app(config_name):
	app = Flask(__name__)
	config_class = config_map.get(config_name)
	app.config.from_object(config_class)
	db.init_app(app)
	
	global redis_store
	redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_POST, decode_responses=True)
	
	@app.after_request
	def after_request(response):
		csrf_token = generate_csrf()
		response.set_cookie('csrf_token', csrf_token)
		return response
	
	
	
	from login_Flask.user import user_blue
	app.register_blueprint(user_blue)
	

	
	CSRFProtect(app)
	Session(app)
	return app
