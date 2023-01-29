from app import app
from flask import render_template, request, redirect, url_for, Blueprint
from .services import getProducts

product = Blueprint('product', __name__)


@product.route('/products')
def productsPage():
    content = getProducts()
    return render_template('products.html', content=content)