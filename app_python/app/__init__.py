from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app  # type: ignore[import]
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
        app.config.from_pyfile('conf.py')
    else:
        app.config.update(asdict(test_conf))  # type: ignore[misc]

    if not app.testing:  # type: ignore[misc]
        if log_file_path := app.config.get(
                'LOG_FILE_PATH'):  # type: ignore[misc]
            logging.basicConfig(
                filename=log_file_path,  # type: ignore[misc]
                level=logging.DEBUG,
            )
        app.wsgi_app = DispatcherMiddleware(  # type: ignore[assignment]
            app.wsgi_app,  # type: ignore[misc]
            {'/metrics': make_wsgi_app()})  # type: ignore[misc]

    __register_blueprints__(app)

    return app
