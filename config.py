from redis import StrictRedis


class Config(object):
    """项目的配置"""
    DEBUG = True
    SECRET_KEY = '8Q63yvFuBbhjXIRQc8H96Yr0LvGXPwmthzalCoQUNto9J9cTD+ChKxb7Yk3RcvzlmIfZvUWPAxPeIg/J/1aV6A=='
    # mysql数据库配置项
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information777"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis数据库配置项
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 指定session的存储位置
    SESSION_TYPE = "redis"
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 指定存储在哪一个redis中
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2