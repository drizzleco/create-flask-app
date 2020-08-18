import os
import random

class Config:
    {% if extras_includes('sqlite') -%}
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    {% elif extras_includes('mongodb') %}
    MONGO_URI = os.getenv("MONGO_URI") or "mongodb://localhost:27017/myDatabase"
    {% endif -%}
    SECRET_KEY = os.getenv("SECRET_KEY") or "".join(
        [chr(random.randint(65, 92)) for _ in range(50)]
    )
