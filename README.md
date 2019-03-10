## When installing app locally then activate using
    python run.py

## When installing remotely on Ubuntu 16.04 server then use wsgi.file
    change config.py file to show local MongoDB
        MONGODB_HOST = 'mongodb://localhost:27017/gm-sandbox'

## If using a remote Mongo cluster via MongoDB Atlas
    change config.py file to show Mongo Atlas cluster address
        mongodb+srv://admin:<password>@cluster0-zhceb.mongodb.net/test?retryWrites=true
