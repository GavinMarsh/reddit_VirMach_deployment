## When installing app locally then activate using
    python run.py

## When installing remotely on Ubuntu 16.04 server then use wsgi.file
    change config.py file to show local MongoDB
        MONGODB_HOST = 'mongodb://localhost:27017/gm-sandbox'

## If using a remote Mongo cluster via MongoDB Atlas
    change config.py file to show Mongo Atlas cluster address
        mongodb+srv://admin:<password>@cluster0-zhceb.mongodb.net/test?retryWrites=true

## When deploying via pythonanywhere
To change the defoult bash python version use:
    
    alias python=python3

create a virtualenv

    mkvirtualenv pythonanywhere_venv
 
 add modules
    pip install pymongo
    pip install flask_mongoengine
    pip install Flask
 
## text for pythonanywheres wsgi file
    import sys

    # add your project directory to the sys.path
    project_home = u'/home/GMM/reddit_VirMach_deployment'
    if project_home not in sys.path:
        sys.path = [project_home] + sys.path

    # import flask app but need to call it "application" for WSGI to work
    from reddit import create_app
    application = create_app('config.DevelopmentConfig')
