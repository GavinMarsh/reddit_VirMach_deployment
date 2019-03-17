## MongoEngine Note: include db name in URI; it overwrites all others


###########################################################
## THIS CONFIG COPY IS HERE SO THAT APCHE2 WSGI WILL RUN ##
###########################################################


class Config(object):
    MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true'
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true'

class DevelopmentConfig(Config):
    MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true'
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
