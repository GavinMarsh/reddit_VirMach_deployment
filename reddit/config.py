## MongoEngine Note: include db name in URI; it overwrites all others
import pymongo

##########################################################
## THIS CONFIG COPY IS HERE SO THAT WSGI LOCAL WILL RUN ##
##########################################################

class Config(object):
    #MONGODB_HOST = 'mongodb://localhost:27017/gm_sandbox'
    # below line is working for reading from MongoDB Atlas collection.
    MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/admin'

    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    #MONGODB_HOST = 'mongodb://localhost:27017/gm_sandbox'
    # below line is working for reading from MongoDB Atlas collection.
    MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/admin'

# why is apache2 using this config ???
class DevelopmentConfig(Config):
    #MONGODB_HOST = 'mongodb://localhost:27017/gm_sandbox'
    # below line is working for reading from MongoDB Atlas collection.
    MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/admin'


    DEBUG = True

class TestingConfig(Config):
    TESTING = True
