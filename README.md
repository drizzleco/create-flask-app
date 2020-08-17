# create-flask-app

autogenerate boilerplate code for a flask app

## Features

- Generate a Flask app with project files:

  - static folder
  - templates folder
  - README.md
  - Makefile
  - setup.py
  - requirements.txt

  and optional extras including:

  - Test suite(tox, pytest)
  - Docker
  - Heroku
  - Job Scheduler

    Flask Libraries

  - Flask-Login
  - Flask-Admin
  - Flask-WTF

    JS Libraries

  - Vue.js(CDN version)
  - jQuery

    CSS

  - Sass
  - Bootstrap

    Databases

  - SQLite(Flask-SQLAlchemy
  - MongoDB(Flask-PyMongo)

- Automatically install pip dependencies

## Getting Started

1. `pip install .` to install the `create-flask-app` console script
2. run `create-flask-app`
3. after selecting extras, `cd` into the new directory and `make start` to start flask server
4. done!

**OR**

1. `python3 create_flask_app.py`

**OR**

To run in development:

1. `make install`
2. `source .env/bin/activate`
3. `python create_flask_app.py`

## Screenshots
