from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
{{ 'import flask_login' if extras_includes('flask-login') }}
{{ 'import flask_admin' if extras_includes('flask-admin') }}
{{ 'import flask_wtf' if extras_includes('flask-wtf') }}

{{ 'from models import db' if extras_includes('sqlite') }}
{{ 'from flask_pymongo import PyMongo' if extras_includes('mongodb') }}

from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
{% if extras_includes('sqlite') %}
db.app = app
db.init_app(app)
{% elif extras_includes('mongodb') %}
mongo = PyMongo(app)
{% endif %}

@app.route("/", methods=["GET"])
def home():
    """
    Home page route
    """
    return render_template("index.html")

@app.route("/hello", methods=["GET"])
def hello():
    return 'hello'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
