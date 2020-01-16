# -*- coding: utf-8 -*-
'''
PROJECT_NAME：login-flask 
FILE:config 
USERNAME: 李宏伟
DATE:2020/1/16 
TIME:上午9:37 
PRODUCT_NAME:PyCharm 
'''
import redis as redis


class Config(object):
	"""工程配置信息"""
	SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
	
	# 数据库的配置信息
	SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/login_flask"
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	
	# redis配置
	REDIS_HOST = "127.0.0.1"
	REDIS_PORT = 6379
	
	# session 配置
	SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
	SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
	SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
	PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒


class DevelopmentConfig(Config):
	DEBUG = True


class ProduactionConfig(Config):
	DEBUG = False


config_map = {
	'development': DevelopmentConfig,
	'production': ProduactionConfig,
}
