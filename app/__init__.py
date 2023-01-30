from flask import Flask
from config import Config
from .user.models import db, User
from flask_migrate import Migrate
from flask_login import LoginManager

from .user.routes import user


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

login_manager.login_view = "user.loginPage"

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

from app.main.routes import main
# from app.search.routes import search
# from app.users.routes import users

app.register_blueprint(main)
# app.register_blueprint(search)
app.register_blueprint(user)