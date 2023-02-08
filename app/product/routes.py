from app import app
from flask import render_template, request, redirect, url_for, Blueprint
from .services import getProducts, getProductInfo
from .models import Product

product = Blueprint('product', __name__)

@product.route('/products/')
@product.route('/products')
def productsPage():
    content = getProducts()
    return render_template('products.html', content=content)

@product.route('/products/<int:prod_id>')
def getProduct(prod_id):
    data = getProductInfo(prod_id)
    name = data['title']
    price = data['price']
    description = data['description']
    image = data['image']
    product = Product(name, price, description, image)
    test = Product.query.filter_by(name=name).first()
    if test:
        pass
    else:
        Product.saveToDB()
    return render_template('singleproduct.html', data = data)