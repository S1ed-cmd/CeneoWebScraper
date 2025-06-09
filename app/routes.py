import os
from flask import render_template, redirect, request, url_for
from app import app
from app.forms import ProductIdForm
from app.models import Product

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/extract")
def display_form():
    form = ProductIdForm()
    return render_template("extract.html", form=form)

@app.route("/extract", methods=['POST'])
def extract():
    form = ProductIdForm(request.form)
    if form.validate():
        product_id = form.product_id.data
        product = Product(product_id)
        product.extract_name()
        product.extract_opinions()
        print(product)
        product.calculate_stats()
        product.generate_charts()
        print(product)
        product.save_opinions()
        product.save_info()
        return redirect(url_for('product', product_id=product_id))
    else:
         return render_template("extract.html", form=form)


@app.route("/product/<product_id>")
def product(product_id):
    return render_template("product.html", product_id=product_id)

@app.route("/charts/<product_id>")
def charts(product_id):
    return render_template("charts.html", product_id=product_id)

@app.route("/products")
def products():
    product_list = []
    products_dir = os.path.join("app", "data", "products")
    if not os.path.exists(products_dir):
        return "Products directory not found", 404
    for fn in os.listdir(products_dir):
        fn = fn.split(".")[0]
        product = Product(product_id=fn)
        product.read_info()
        product_list.append(product)
    return render_template("products.html", products=product_list)

@app.route("/about")
def about():
    return render_template("about.html")