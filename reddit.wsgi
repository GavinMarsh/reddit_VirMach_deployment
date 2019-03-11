## This wsgi works with virmach.com remote server Ubuntu 16.04
## Can also work with pythonanywhere if you change the project_home folder to u'/home/GMM/flaskr/'

import sys

# add your project directory to the sys.path
project_home = u'/var/www/reddit/'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# You can't import a variable that is local to a function, so we need to call
# the function inside the application-factory to buid and return the app.


from reddit import create_app
if __name__ == "__main__": #added
    application = create_app('config.DevelopmentConfig')
#    app.run() # added
