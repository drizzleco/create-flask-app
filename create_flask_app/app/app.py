from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
{{ 'import flask_login' if extras_includes('flask-login') }}
{{ 'import flask_admin' if extras_includes('flask-admin') }}
{{ 'import flask_wtf' if extras_includes('flask-wtf') }}
{{ 'from flask_assets import Environment, Bundle' if extras_includes('sass') }}

{{ 'from models import db' if extras_includes('sqlite') }}
{{ 'from flask_pymongo import PyMongo' if extras_includes('mongodb') }}

from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
{% if extras_includes('sass') %}
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('scss/style.scss', filters='pyscss', output='css/style.css')
assets.register('scss_all', scss)
{% endif %}
{% if extras_includes('sqlite') %}
db.app = app
db.init_app(app)
{% elif extras_includes('mongodb') %}
mongo = PyMongo(app)
{% endif %}

@app.route("/", methods=["GET", 'POST'])
def home():
    """
    Home page route
    """
    if request.method == 'POST':
        message = request.form['message']
        return jsonify(your_message=message)
    return render_template("index.html")

@app.route("/hello", methods=["GET"])
def hello():
    """
    Hello route
    """
    return 'hello'

@app.route('/message', methods=['POST'])
def message():
    """
    Message route
    """
    message = request.json.get("message")
    return jsonify(your_message=message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
