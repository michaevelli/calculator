from flask import Flask, redirect, render_template, request, url_for
from server import *
from calc import *

@app.route("/", methods=["GET", "POST"])
def index():
    display = ""
    if request.method == "POST":
        x = request.form["bt"]
        display = displa(x)
        return render_template("index.html", inpu = display)
    return render_template("index.html", inpu = display)
