import os
from flask_uploads import IMAGES


class Dev:
    MONGO_URI = "mongodb://127.0.0.1:27017/pyfly"
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.qq.com')
    MAIL_PROT = 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEBUG = True
    MAIL_SUBJECT_PREFIX = '[PyFly]-'
    WTF_CSRF_ENABLED = False
    UPLOADED_PHOTOS_ALLOW = IMAGES
    UPLOADED_PHOTOS_DEST = os.path.join(os.getcwd(), 'uploads')
    WHOOSH_PATH = os.path.join(os.getcwd(), 'whoosh_indexes')

    USE_CACHE = True
    # CACHE_TYPE = 'redis'
    CACHE_TYPE = 'simple'
    CACHE_REDIS_HOST = '172.16.1.202'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_PASSWORD = '456123'
    CACHE_REDIS_DB = '0'


class Pud:
    pass


config = {
    "Dev": Dev,
    "Pud": Pud
}
