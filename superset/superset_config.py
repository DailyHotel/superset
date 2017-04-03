# -*- coding: utf-8 -*-

import os
from werkzeug.contrib.cache import RedisCache

#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
ROW_LIMIT = 15000
SUPERSET_WORKERS = int(os.getenv('WORKERS', '2'))
SUPERSET_CELERY_WORKERS = int(os.getenv('CELERY_WORKERS', '32'))

SUPERSET_WEBSERVER_PORT = 8088
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = os.getenv('SECRET_KEY', 'BzbMpmskLAwDtrb9rzdxoLmp')

redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', '6379'))
redis_db = int(os.getenv('REDIS_DB', '0'))
cache_default_timeout = 300
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': cache_default_timeout,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': redis_host,
    'CACHE_REDIS_PORT': redis_port,
    'CACHE_REDIS_DB': redis_db,
    'CACHE_REDIS_URL': 'redis://{0}:{1}/{2}'.format(redis_host, redis_port, redis_db)
    }

mysql_user = os.getenv('MYSQL_USER', 'superset')
mysql_password = os.getenv('MYSQL_PASSWORD')
mysql_host = os.getenv('MYSQL_HOST', 'superset')
mysql_port = int(os.getenv('MYSQL_PORT', '3306'))
mysql_database = os.getenv('MYSQL_DATABASE', 'superset')
SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4'.format(mysql_user, mysql_password, mysql_host, mysql_port, mysql_database)


celery_redis_host = os.getenv('CELERY_REDIS_HOST', redis_host)
celery_redis_port = int(os.getenv('CELERY_REDIS_PORT', redis_port))
celery_redis_db = int(os.getenv('CELERY_REDIS_DB', '1'))

celery_result_backend_redis_host = os.getenv('CELERY_RESULT_BACKEND_REDIS_HOST', celery_redis_host)
celery_result_backend_redis_port = int(os.getenv('CELERY_RESULT_BACKEND_REDIS_PORT', celery_redis_port))
celery_result_backend_redis_db = int(os.getenv('CELERY_RESULT_BACKEND_REDIS_DB', '2'))

class CeleryConfig(object):
  BROKER_URL = 'redis://{0}:{1}/{2}'.format(celery_redis_host, celery_redis_port, celery_redis_db)
  CELERY_IMPORTS = ('superset.sql_lab', )
  CELERY_RESULT_BACKEND = 'redis://{0}:{1}/{2}'.format(celery_result_backend_redis_host, celery_result_backend_redis_port, celery_result_backend_redis_db)
  CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}
CELERY_CONFIG = CeleryConfig

RESULTS_BACKEND = RedisCache(host=celery_result_backend_redis_host, port=celery_result_backend_redis_port, password=None, db=celery_result_backend_redis_db, default_timeout=cache_default_timeout)

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')

DEBUG = bool(os.getenv('SUPERSET_DEBUG', 'False'))


# smtp server configuration
EMAIL_NOTIFICATIONS = bool(os.getenv('EMAIL_NOTIFICATIONS', 'False'))  # all the emails are sent using dryrun
SMTP_HOST = os.getenv('SMTP_HOST', 'localhost')
SMTP_STARTTLS = bool(os.getenv('SMTP_STARTTLS', 'True'))
SMTP_SSL = bool(os.getenv('SMTP_SSL', 'False'))
SMTP_USER = os.getenv('SMTP_USER', 'superset')
SMTP_PORT = int(os.getenv('SMTP_PORT', '25'))
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', 'superset')
SMTP_MAIL_FROM = os.getenv('SMTP_MAIL_FROM', 'superset@superset.com')
