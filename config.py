## MongoEngine Note: include db name in URI; it overwrites all others



###########################################################
## THIS CONFIG COPY IS HERE SO THAT APCHE2 WSGI WILL RUN ##
###########################################################


class Config(object):
    #MONGODB_HOST = 'mongodb://localhost:27017/gm_sandbox'
    MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true'
    #client = pymongo.MongoClient("mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true")
    db = MONGODB_HOST.gm_sandbox

    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    #MONGODB_HOST = 'mongodb://localhost:27017/gm_sandbox'
    MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true'
    #client = pymongo.MongoClient("mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true")
    db = MONGODB_HOST.gm_sandbox

# why is apache2 using this config ???
class DevelopmentConfig(Config):
    #MONGODB_HOST = 'mongodb://localhost:27017/gm_sandbox'
    MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true'
    #client = pymongo.MongoClient("mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true")
    db = MONGODB_HOST.gm_sandbox

    DEBUG = True

class TestingConfig(Config):
    TESTING = True
