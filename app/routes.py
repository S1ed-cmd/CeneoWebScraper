
from app import app
from flask import Flask, render_template

@app.route("/")
def hello():
    return render_template("index.html" )

@app.route("/extract/")
def hello():
    return render_template("extract.html" )

@app.route("/product/<product_id>")
def hello(product_id):
    return render_template("product.html", product_id=product_id )

@app.route("/charts/<product_id>")
def hello(product_id):
    return render_template("charts.html" , product_id=product_id)

@app.route("/products")
def hello():
    return render_template("products.html")

@app.route("/about")
def hello():
    return render_template("about.html")