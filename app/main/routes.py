from app import app
from flask import render_template, request, redirect, url_for, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def homePage():
    return render_template('index.html')
