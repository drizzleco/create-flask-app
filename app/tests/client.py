import os
import tempfile

import pytest

from app import app


@pytest.fixture
def client():
    {% if extras_includes('sqlite') or extras_includes('mongo') -%}
    db_fd, app.config["DATABASE"] = tempfile.mkstemp()
    {% endif -%}
    app.config["TESTING"] = True
    app.secret_key = "sekrit!"
    with app.test_client() as client:
        yield client
    {% if extras_includes('sqlite') or extras_includes('mongo') -%}
    os.close(db_fd)
    os.unlink(app.config["DATABASE"])
    {% endif -%}
