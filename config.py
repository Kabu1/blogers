import os
class Config:
    '''
    General configuration parent class
    '''
    QUOTES_API_KEY = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://k:qwerty1234@localhost/blog'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
