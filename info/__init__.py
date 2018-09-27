from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from config import CONFIG

# 初始化数据库
db = SQLAlchemy()


def create_app(config_name):
    # 初始化app对象
    app = Flask(__name__)

    # 从对象中加载配置
    app.config.from_object(CONFIG[config_name])

    # 初始化db数据库对象
    # db = SQLAlchemy(app)
    # flask中很多扩展里面都可以先初始化扩展对象，然后再调用对象的init_app方法进行初始化
    db.init_app(app)
    # 创建redis存储对象
    redis_store = StrictRedis(host=CONFIG[config_name].REDIS_HOST, port=CONFIG[config_name].REDIS_PORT)
    # 开启当前项目CSRF保护， CSRFProtect只做验证工作，cookie中的 csrf_token 和表单中的 csrf_token 需要我们自己实现
    CSRFProtect(app)
    # 为app添加session存储位置Session类的作用，就是为为app指定session的存储位置的
    Session(app)

    return app