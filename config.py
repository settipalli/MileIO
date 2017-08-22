from os import path, environ as env

basedir = path.abspath(path.dirname(__file__))

# helper method
get_from_env = lambda key: env[key] if key in env else ''


class Auth:
    CLIENT_ID = (get_from_env('GOOGLE_CLIENT_ID'))
    CLIENT_SECRET = get_from_env('GOOGLE_CLIENT_SECRET')
    REDIRECT_URI = get_from_env('GOOGLE_REDIRECT_URI')
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'


class Database:
    # we do not use the SQLAlchemy event system
    # turning it off saves some resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = get_from_env('DATABASE_URL')


class Security:
    SECURITY_PASSWORD_HASH = get_from_env('SECURITY_PASSWORD_HASH')
    SECURITY_PASSWORD_SALT = get_from_env('SECURITY_PASSWORD_SALT')
    SECURITY_RECOVERABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_POST_LOGIN = '/profile'
    # https://developers.google.com/identity/protocols/googlescopes
    SCOPES = ['https://www.googleapis.com/auth/drive.file',
              'https://www.googleapis.com/auth/spreadsheets']


class Mail:
    SECURITY_EMAIL_SENDER = get_from_env('SECURITY_EMAIL_SENDER')
    MAIL_USERNAME = get_from_env('MAIL_USERNAME')
    MAIL_PASSWORD = get_from_env('MAIL_PASSWORD')
    MAIL_SERVER = get_from_env('MAIL_SERVER')
    MAIL_PORT = get_from_env('MAIL_PORT')
    MAIL_USE_SSL = True
    ADMIN_MAIL_ID = get_from_env('ADMIN_MAIL_ID')
    ADMIN_MAIL_PASSWORD = get_from_env('ADMIN_MAIL_PASSWORD')


class Config(Auth, Database, Security, Mail):
    APP_NAME = 'MileIO'
    SECRET_KEY = get_from_env('APP_SECRET_KEY')


