import os

class Config:

    SECRET_KEY = '7f0c2f57938476cca8a1b7a88854b3c8'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    #SECRET_KEY = os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    #print ('###############################################')
    #print (SECRET_KEY)
    #print ('###############################################')

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')