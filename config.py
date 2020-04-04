from app.utils.environment import Environment


class Config:
    DEBUG = True
    TESTING = False
    LOG_LEVEL = 'DEBUG'
    # DB_HOST = 'localhost'
    # DB_NAME = 'test'
    # DB_USER = 'root'
    # DB_PASS = 'root'
    # BACKUP_PATH = '/var/backup/ehome/'
    # UPLOAD_PATH = '/srv/http/ehome/app/frontend/planos'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "sarakatunga katunga katunga todos queremos sarakatunga"


class ProductionConfig(Config):
    LOG_LEVEL = 'WARNING'
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/stock.ar'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    CACHE_TYPE = 'simple'


class TestingConfig(DevelopmentConfig):
    TESTING = True


app_config = {
    Environment.PRODUCTION: ProductionConfig,
    Environment.DEVELOPMENT: DevelopmentConfig,
    Environment.TESTING: TestingConfig
}
