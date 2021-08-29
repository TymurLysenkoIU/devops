import pytest
from typing import Iterable
from flask import Flask
from flask.testing import FlaskClient

from app import create_app
from app import AppConfig

__test_config__ = AppConfig(TESTING=True, )


@pytest.fixture()
def client() -> Iterable[FlaskClient]:
    app: Flask = create_app(__test_config__)

    with app.test_client() as result_client:
        with app.app_context():
            pass  # For now there is nothing to do with this
        yield result_client
