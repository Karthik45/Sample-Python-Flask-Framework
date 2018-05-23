import os

base_dir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgres://lpsrcipcyspdwa:e6cad96cf7ef7492a47e1dfb5bb10f57a026daf1c56fbc489533f796e5609c29@ec2-54-247-111-19.eu-west-1.compute.amazonaws.com:5432/'
database_name = 'd71nr0qkcvosp7'

class BaseConfig:
    """
    Base application configuration
    """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_strong_key')
    BCRYPT_HASH_PREFIX = 14
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTH_TOKEN_EXPIRY_DAYS = 30
    AUTH_TOKEN_EXPIRY_SECONDS = 3000

class DevelopmentConfig(BaseConfig):
    """
    Development application configuration
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', postgres_local_base + database_name)
    BCRYPT_HASH_PREFIX = 4
    AUTH_TOKEN_EXPIRY_DAYS = 1
    AUTH_TOKEN_EXPIRY_SECONDS = 20


class TestingConfig(BaseConfig):
    """
    Testing application configuration
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TEST', postgres_local_base + database_name + "_test")
    BCRYPT_HASH_PREFIX = 4
    AUTH_TOKEN_EXPIRY_DAYS = 0
    AUTH_TOKEN_EXPIRY_SECONDS = 3
    AUTH_TOKEN_EXPIRATION_TIME_DURING_TESTS = 5


class ProductionConfig(BaseConfig):
    """
    Production application configuration
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', postgres_local_base + database_name)
    BCRYPT_HASH_PREFIX = 13
    AUTH_TOKEN_EXPIRY_DAYS = 30
    AUTH_TOKEN_EXPIRY_SECONDS = 20