# Configuration-folder/settings/_development_settings.py
# Add security related items in this file such as passwords and keys

# Add this file in '.gitignore'

# import everything from settings.py i.e. import as etc.
from .settings import *


# Now overwrite necessary items

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
# Create new secret key (just add few more letters in original key)
# SECRET_KEY = os.environ.get(SECRET_KEY)
SECRET_KEY = '#3+=sz)bfg1o#sg(-1)+8zp#4wwzhl%xs7-mx-%=y-6n=g+mi*'


# Database: Add development database details here
# SQLite
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}


# # MySQL settings
# # mysqlclient is required: pip install mysqlclient
# # First, go to MySQL and create database
# # e.g. 'db_mysql' using query 'create database db_mysql;'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'db_mysql',
#         'USER' : 'root',
#         'PASSWORD' : 'root',
#         'HOST' : '', # leave blank for localhost
#         'PORT' : '', # leave blank for localhost
#     }
# }


# # Email
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True


# #crispy form settings
# CRISPY_TEMPLATE_PACK = 'bootstrap3'


# #django-registration-redux settings
# ACCOUNT_ACTIVATION_DAYS=7
# REGISTRATION_AUTO_LOGIN=True
# SITE_ID=1
# LOGIN_REDIRECT_URL='/'


# SITE_HOST = 'smtp.onlinebookstore.elasticbeanstalk.com'


# # add all sites for calling API
# CORS_ORIGIN_ALLOW_ALL = True
# # #API call for specific sites
# # CORS_ORIGIN_REGEX_WHITELIST = (  ## Test these regexes somewhere - if your API won't allow AJAX calls from a
# # whitelisted site your regexes are probably the problem
# #     r'^https?://(.+\.)?fake.co.nz',
# #     r'^https?://(.+\.)?fake.net.nz',
# # )
# # CORS_ALLOW_METHODS = (
# #     'GET',
# #     'OPTIONS',
# # )
