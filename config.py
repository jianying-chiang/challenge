class Config(object):
    DEBUG = False
    TESTING = False

class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///temp_database.sqlite3"

class TestConfig(Config):
    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///temp_test_database.sqlite3"