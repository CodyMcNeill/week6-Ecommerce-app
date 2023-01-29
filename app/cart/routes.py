from app import app
from flask import render_template, request, redirect, url_for, Blueprint

cart = Blueprint('cart', __name__)


@cart.route('/cart')
def cartPage():
    
    return render_template('cart.html')