from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('page/home.html')


@page.route('/about')
def about():
    return render_template('page/about.html')


@page.route('/services')
def services():
    return render_template('page/services.html')


@page.route('/contact')
def contact():
    return render_template('page/contact.html')