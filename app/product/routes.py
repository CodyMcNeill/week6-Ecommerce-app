from app import app
from flask import render_template, request, redirect, url_for, Blueprint
from .services import getProducts, getProductID

product = Blueprint('product', __name__)


@product.route('/products')
def productsPage():
    content = getProducts()
    prod_id = getProductID()
    return render_template('products.html', content=content, prod_id=prod_id)

@product.route('/products/<prod_id>')
def getProduct(prod_id):
    prod_id = getProductID()
    return render_template('singleproduct.html', prod_id = prod_id)
