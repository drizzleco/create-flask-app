import pytest
import tempfile
import os
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
