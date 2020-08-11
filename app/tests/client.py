import os
import tempfile

import pytest

from app import app


@pytest.fixture
def client():
    db_fd, app.config["DATABASE"] = tempfile.mkstemp()
    app.config["TESTING"] = True
    app.secret_key = "sekrit!"
    with app.test_client() as client:
        yield client
    os.close(db_fd)
    os.unlink(app.config["DATABASE"])
