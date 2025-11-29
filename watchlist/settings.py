import os

MYSQL_PREFIX = 'mysql://xun:_Aa7835381@localhost:3306'


class BaseConfig:  # 创建配置基类
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')


class DevelopmentConfig(BaseConfig):  # 开发配置
    SQLALCHEMY_DATABASE_URI = MYSQL_PREFIX + '/data'


class TestingConfig(BaseConfig):  #测试配置
    TESTING = True
    SQLALCHEMY_DATABASE_URI = MYSQL_PREFIX + '/test'


class ProductionConfig(BaseConfig):  # 生产配置
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', MYSQL_PREFIX + '/data')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
