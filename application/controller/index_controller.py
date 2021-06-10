from flask import Flask, render_template, request, url_for
from application import app



@app.route("/")
@app.route('/index')
def index():
    return render_template("index.html")