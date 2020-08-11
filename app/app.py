from flask import (
    Flask,
    jsonify,
    request,
    render_template,
)
from flask_cors import CORS
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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
