from os import path, environ


class Config(object):
    APPNAME = 'app'
    ROOT = path.abspath(APPNAME)
    UPLOAD_PATH = '/static/upload/'
    SERVER_PATH = ROOT + UPLOAD_PATH

    USER = environ.get('POSTGRES_USER', 'tyzhinov')
    PASSWORD = environ.get('POSTGRES_PASSWORD', 'ryodtery')
    HOST = environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = environ.get('POSTGRES_PORT', 5433)
    DB = environ.get('POSTGRES_DB', 'flask_test')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = ";EamJ$@2BR%BsB-"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
