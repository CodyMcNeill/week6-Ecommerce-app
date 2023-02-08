from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from ..user import *

db = SQLAlchemy()
migrate = Migrate(db)

class Cart(db.Model):
    id = db.column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    


    
