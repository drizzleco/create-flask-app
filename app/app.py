from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import flask_login
import flask_admin
import flask_wtf
import flask_sqlalchemy

from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)


# db.app = app
# db.init_app(app)


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
