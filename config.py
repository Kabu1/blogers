import os
class Config:
    '''
    General configuration parent class
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SECRET_KEY ='qwerty1234'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://k:qwerty1234@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
     #email config
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("flaskemailmoringa@gmail.com")
    MAIL_PASSWORD = os.environ.get("qazplm098")


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}