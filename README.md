## When installing app locally then activate using
    python run.py

## When installing remotely on Ubuntu 16.04 server then use wsgi.file
    change config.py file to show local MongoDB
        MONGODB_HOST = 'mongodb://localhost:27017/gm-sandbox'

## If using a remote Mongo cluster via MongoDB Atlas
    change config.py file to show Mongo Atlas cluster address
        mongodb+srv://admin:<password>@cluster0-zhceb.mongodb.net/test?retryWrites=true

## sites.conf
    <VirtualHost *:80>
                ServerName 107.172.143.209
                ServerAdmin admin@mywebsite.com
                WSGIScriptAlias /flaskr /var/www/flaskr/flaskr.wsgi
                <Directory /var/www/flaskr/flaskr/>
                    Order allow,deny
                    Allow from all
                </Directory>
                Alias /static /var/www/flaskr/flaskr/static
                <Directory /var/www/flaskr/flaskr/static/>
                        Order allow,deny
                        Allow from all
                </Directory>

                WSGIScriptAlias /reddit /var/www/reddit/reddit.wsgi
                <Directory /var/www/reddit/reddit/>
                    Order allow,deny
                    Allow from all
                </Directory>
                 Alias /static1 /var/www/reddit/reddit/static
                <Directory /var/www/reddit/reddit/static/>
                        Order allow,deny
                        Allow from all
                </Directory>


                ErrorLog ${APACHE_LOG_DIR}/error.log
                LogLevel info
                CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>


## When deploying via pythonanywhere
To change the defoult bash python version use:
    
    alias python=python3

create a virtualenv

    virtualenv --python=python3.7 --no-site-packages pa_venv
 
 add modules
    pip install pymongo
    pip install flask_mongoengine
    pip install dnspython
 
## text for pythonanywheres wsgi file
    import sys

    # add your project directory to the sys.path
    project_home = u'/home/GMM/reddit_VirMach_deployment'
    if project_home not in sys.path:
        sys.path = [project_home] + sys.path

    # import flask app but need to call it "application" for WSGI to work
    from reddit import create_app
    application = create_app('config.DevelopmentConfig')
