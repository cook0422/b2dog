    
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = 'testkey'
DATABASE_URI = 'mysql+pymysql://root:Cook21!!@cook0422.mysql.rds.aliyuncs.com/taobao'
DATABASE_CONNECT_OPTIONS = {}
ADMINS = frozenset(['http://lucumr.pocoo.org/'])

WHOOSH_INDEX = os.path.join(_basedir, 'flask-website.whoosh')
DOCUMENTATION_PATH = os.path.join(_basedir, '../flask/docs/_build/dirhtml')

print(_basedir)
del os