from flask import Flask
from config import Config
# from .models import db, Users
# from flask_migrate import Migrate
# from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# db.init_app(app)
# migrate = Migrate(app, db)
# login_manager = LoginManager(app)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

from app.main.routes import main
from app.user.routes import user
from app.product.routes import product
from app.cart.routes import cart

app.register_blueprint(main)
app.register_blueprint(user)
app.register_blueprint(product)
app.register_blueprint(cart)