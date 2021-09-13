from flask import Flask
from typing import Optional
from dataclasses import asdict
import logging

from .AppConfig import AppConfig


def __register_blueprints__(app: Flask) -> None:
    from app import api

    app.register_blueprint(api.bp)


def create_app(test_conf: Optional[AppConfig] = None) -> Flask:
    app = Flask(__name__)

    if test_conf is None:
        app.config.from_pyfile('logging_conf.py')
    else:
        app.config.update(asdict(test_conf))  # type: ignore[misc]

    if not app.testing:
        if (
            (log_file_path := app.config.get('LOG_FILE_PATH'))
        ):
            logging.basicConfig(
                filename=log_file_path,
                level=logging.DEBUG,
            )

    __register_blueprints__(app)

    return app
