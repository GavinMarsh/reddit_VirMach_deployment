## MongoEngine Note: include db name in URI; it overwrites all others
import pymongo

##########################################################
## THIS CONFIG COPY IS HERE SO THAT WSGI LOCAL WILL RUN ##
##########################################################

class Config(object):
    #MONGODB_HOST = 'mongodb://localhost:27017/gm_sandbox'
    MONGODB_HOST = 'mongodb+srv://admin:P_12345678@cluster0-zhceb.mongodb.net/gm_sandbox'
    #client = pymongo.MongoClient("mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true")
    #MONGODB_HOST = client.gm_sandbox

    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    #MONGODB_HOST = 'mongodb://localhost:27017/gm_sandbox'
    MONGODB_HOST = 'mongodb+srv://admin:P_12345678@cluster0-zhceb.mongodb.net/gm_sandbox'
    #MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true'
    #client = pymongo.MongoClient("mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true")
    #MONGODB_HOST = client.gm_sandbox

# why is apache2 using this config ???
class DevelopmentConfig(Config):
    #MONGODB_HOST = 'mongodb://localhost:27017/gm_sandbox'
    MONGODB_HOST = 'mongodb+srv://admin:P_12345678@cluster0-zhceb.mongodb.net/gm_sandbox'
    #MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true'
    #client = pymongo.MongoClient("mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true")
    #MONGODB_HOST = client.gm_sandbox = client.gm_sandbox

    DEBUG = True

class TestingConfig(Config):
    TESTING = True
