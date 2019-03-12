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
