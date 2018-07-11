import os

WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ['SECRET_KEY']

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = os.environ['HEROKU_POSTGRESQL_BLACK_URL']
