# create-flask-app

autogenerate boilerplate code for a flask app

![version](https://img.shields.io/pypi/v/new-flask-app)

# `pip install new-flask-app`

![demo](https://raw.githubusercontent.com/drizzleco/create-flask-app/master/img/demo.gif)

## Features

- Generate a basic Flask app with:

  - app.py
  - config.py
  - static folder
  - templates folder
  - README.md
  - Makefile
  - setup.py
  - requirements.txt
  - .gitignore

  and optional extras including:

  - Test suite(tox, pytest)
  - Docker
  - Heroku
  - Job Scheduler
  - Flask-Login
  - Flask-Admin
  - Flask-WTF
  - Vue.js(CDN version)
  - jQuery
  - Sass
  - Bootstrap
  - SQLite(Flask-SQLAlchemy)
  - MongoDB(Flask-PyMongo)

- Automatically install pip dependencies in a venv
- Makefile with useful commands(starting server, lint code, test code)

## Getting Started

1. `pip install new-flask-app` to install the `create-flask-app` console script
2. run `create-flask-app`
3. after selecting extras, `cd` into the new directory and `make start` to start flask server
4. done!

**OR**

For development:

1. `make install`
2. `source .env/bin/activate`
3. `create-flask-app` **or** `python create_flask_app.py`
