class Config:
    DEBUG = False
    TESTING = False
    CACHE_TYPE = 'RedisCache'
    CACHE_DEFAULT_TIMEOUT = 300

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'