#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """To show Hello HBNB"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def home2():
    """To show HBNB"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def homeC(text):
    """Passing variable"""
    return ("C {}".format(text.replace('_', ' ')))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
