from flask import Flask
from typing import Optional
from dataclasses import asdict

from .AppConfig import AppConfig


def __register_blueprints__(app: Flask) -> None:
    from app import api

    app.register_blueprint(api.bp)


def create_app(test_conf: Optional[AppConfig] = None) -> Flask:
    app = Flask(__name__)

    if test_conf is None:
        pass  # for now no configuration for application is setup
    else:
        app.config.update(asdict(test_conf))  # type: ignore[misc]

    __register_blueprints__(app)

    return app
