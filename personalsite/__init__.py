from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os
#from personalsite.config import Config


app = Flask(__name__)

# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'personalsite.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

mail = Mail(app)


from personalsite.users.routes import users
from personalsite.posts.routes import posts
from personalsite.main.routes import main
from personalsite.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)