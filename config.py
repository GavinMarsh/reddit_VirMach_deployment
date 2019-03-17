## MongoEngine Note: include db name in URI; it overwrites all others


###########################################################
## THIS CONFIG COPY IS HERE SO THAT APCHE2 WSGI WILL RUN ##
###########################################################


class Config(object):
    MONGODB_HOST = """
        const MongoClient = require(‘mongodb’).MongoClient;
const uri = "mongodb+srv://admin:<password>@cluster0-zhceb.mongodb.net/test?retryWrites=true";
const client = new MongoClient(uri, { useNewUrlParser: true });
client.connect(err => {
  const collection = client.db("test").collection("devices");
  // perform actions on the collection object
  client.close();
});
"""
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true'

class DevelopmentConfig(Config):
    MONGODB_HOST = 'mongodb+srv://admin:P=12345678@cluster0-zhceb.mongodb.net/test?retryWrites=true'
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
