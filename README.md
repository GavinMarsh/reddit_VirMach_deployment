# reddit
reddit is a flask web application wich has a model-view-controller layout:

Model       = MongoDB

View        = Jinja2

Controller  = Flask/apache2/wsgi

# local-mac apache2/wsgi-express/flask deployment
added a copy of config.py and has it's own wsgi.file called local-mac.wsgi, both files plased in the working directory reddit/reddit so that wsgi-express will work correctly.

### wsgi-express file
       
    import sys

    # add your project directory to the sys.path
    project_home = u'/var/www/reddit/'
    if project_home not in sys.path:
    sys.path = [project_home] + sys.path

    # You can't import a variable that is local to a function, instead call
    # the function inside the application-factory to buid and return the app.
    from __init__ import create_app
   
    application = create_app('config.DevelopmentConfig')
    
    application.secret_key = 'Add your secret key'

To run application, navigate to the source files directory reddit/reddit and enter into the cli: 
     mod_wsgi-express start-server local-mac.wsgi

# VirMach Ubuntu 16.04, apache2/wsgi/flask deployment
/etc/apache2/sites-available/sites.wsgi file
Place each site on it's own port and include it's own WSGI daemon process, this will prevent any data leakage between each site.
    
    Listen 80

    <VirtualHost *:80>
        WSGIDaemonProcess reddit display-name=%{GROUP}
        WSGIProcessGroup reddit

        ServerName 107.172.143.209
        WSGIScriptAlias /  /var/www/reddit/reddit.wsgi
        <Directory /var/www/reddit/reddit/>
                Order allow,deny
                Allow from all
        </Directory>
        Alias /static /var/www/reddit/reddit/static
        <Directory /var/www/reddit/reddit/static/>
                Order allow,deny
                Allow from all
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/error.log
        LogLevel info
        CustomLog ${APACHE_LOG_DIR}/access.log combined

    </VirtualHost>

    Listen 8080

    <VirtualHost *:8080>
        WSGIDaemonProcess reddit display-name=%{GROUP}
        WSGIProcessGroup reddit

        ServerName 107.172.143.209
        WSGIScriptAlias /  /var/www/reddit/reddit.wsgi
        <Directory /var/www/reddit/reddit/>
                Order allow,deny
                Allow from all
        </Directory>
        Alias /static /var/www/reddit/reddit/static
        <Directory /var/www/reddit/reddit/static/>
                Order allow,deny
                Allow from all
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/error.log
        LogLevel info
        CustomLog ${APACHE_LOG_DIR}/access.log combined

    </VirtualHost>


### If using a remote Mongo cluster via MongoDB Atlas
    change config.py file to show Mongo Atlas cluster address
        mongodb+srv://admin:<password>@cluster0-zhceb.mongodb.net/test?retryWrites=true
        
### If using a local instance of MongoDB
     change config.py file to show local MongoDB
        MONGODB_HOST = 'mongodb://localhost:27017/gm-sandbox'

### WSGI.file
/etc/apache2/sites-available/sites.wsgi

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


# Pythonanywhere wsgi deployment
To change the defoult bash python version use:
    
    alias python=python3

create a virtualenv

    virtualenv --python=python3.7 --no-site-packages pythonanywhere_venv
 
 add modules
    pip install pymongo
    pip install flask_mongoengine
    pip install dnspython
 
### wsgi file
    import sys

    # add your project directory to the sys.path
    project_home = u'/home/GMM/reddit_VirMach_deployment'
    if project_home not in sys.path:
        sys.path = [project_home] + sys.path

    # import flask app but need to call it "application" for WSGI to work
    from reddit import create_app
    application = create_app('config.DevelopmentConfig')
    
# TODO
- Get reddit-top-posts-scrapy script working by building it up piece by piece.
- Upload script to pythonanywhere to run as a cron job.
