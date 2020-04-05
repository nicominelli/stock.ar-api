from app.utils.environment import Environment


class Config:
    DEBUG = True
    TESTING = False
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', 3306)
    DB_NAME = os.getenv('DB_NAME', 'test')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASS = os.getenv('DB_PASS', 'root')
    # BACKUP_PATH = '/var/backup/ehome/'
    # UPLOAD_PATH = '/srv/http/ehome/app/frontend/planos'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'sarakatunga katunga katunga todos queremos sarakatunga')


class ProductionConfig(Config):
    LOG_LEVEL = 'WARNING'
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%d/%s' % (DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
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
