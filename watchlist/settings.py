import os

class BaseConfig:  # 创建配置基类
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')


class DevelopmentConfig(BaseConfig):  # 开发配置
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', 'mysql://xun:_Aa7835381@localhost:3306/data')


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'mysql://xun:_Aa7835381@localhost:3306/data')



class ProductionConfig(BaseConfig):  # 生产配置
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
