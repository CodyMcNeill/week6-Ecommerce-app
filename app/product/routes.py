from app import app
from flask import render_template, request, redirect, url_for, Blueprint
from .services import getProducts
products = Blueprint('main', __name__)


@products.route('/products')
def productsPage():
    content = getProducts()
    
    return render_template('index.html', content=content)