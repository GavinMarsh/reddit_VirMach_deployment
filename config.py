## MongoEngine Note: include db name in URI; it overwrites all others


###########################################################
## THIS CONFIG COPY IS HERE SO THAT APCHE2 WSGI WILL RUN ##
###########################################################


class Config(object):
    MONGODB_HOST = 'mongodb://localhost:27017/gm-sandbox'
    #MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true'
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    MONGODB_HOST = 'mongodb://localhost:27017/gm-sandbox'
    #MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true'

# why is apache2 using this config ???
class DevelopmentConfig(Config):
    #MONGODB_HOST = 'mongodb://localhost:27017/gm-sandbox'
    MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true'
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
