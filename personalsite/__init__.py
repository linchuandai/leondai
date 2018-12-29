from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
#from personalsite.config import Config

from flask.ext.heroku import Heroku

app = Flask(__name__)

app.config['SECRET_KEY'] = '7f0c2f57938476cca8a1b7a88854b3c8'

heroku = Heroku(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

#app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
#app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


from personalsite.users.routes import users
from personalsite.posts.routes import posts
from personalsite.main.routes import main
from personalsite.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)


# db = SQLAlchemy()
# bcrypt = Bcrypt()
# login_manager = LoginManager()
# login_manager.login_view = 'users.login'
# login_manager.login_message_category = 'info'
#
# mail = Mail()
#
# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(config_class)
#
#     db.init_app(app)
#     bcrypt.init_app(app)
#     login_manager.init_app(app)
#     mail.init_app(app)
#
#     from personalsite.users.routes import users
#     from personalsite.posts.routes import posts
#     from personalsite.main.routes import main
#     from personalsite.errors.handlers import errors
#
#     app.register_blueprint(users)
#     app.register_blueprint(posts)
#     app.register_blueprint(main)
#     app.register_blueprint(errors)
#
#     return app