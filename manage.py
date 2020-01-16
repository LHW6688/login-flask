# -*- coding: utf-8 -*-
'''
PROJECT_NAME：login-flask 
FILE:manage 
USERNAME: 李宏伟
DATE:2020/1/16 
TIME:上午9:26 
PRODUCT_NAME:PyCharm 
'''

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from login_Flask import create_app, db
from login_Flask import models
from login_Flask.models import User

app = create_app('development')
manager = Manager(app)
Migrate(app, db)
manager.add_command('mysql', MigrateCommand)

@manager.option('-n', '--name', dest='name')
@manager.option('-p', '--password', dest='password')
def create_admin(name, password):
    user = User()
    user.nick_name = name
    user.mobile = name
    user.password = password
    user.is_admin = True
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    print(app.url_map)
    manager.run()