# instance

import os

class Config(object):
    """parent cofiguration"""
    DEBUG = True
    CSRF_ENABLED = True
    SECRET = os.getenv('\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8')

class DevelopmentConfig(Config):
    """development configurations"""
    DEBUG = True

class TestingConfig(Config):
    """testing configurations"""
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    """staging configurations"""
    DEBUG = True

class ProductionConfig(Config):
    """production configurations"""
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}