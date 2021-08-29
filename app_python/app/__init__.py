from flask import Flask
from typing import Optional


def __register_blueprints__(app: Flask) -> None:
  from app import api

  app.register_blueprint(api.bp)


def create_app(test_conf: Optional[dict] = None) -> Flask:
  app = Flask(__name__)

  if test_conf is None:
    pass  # for now no configuration for application is setup
  else:
    app.config.update(test_conf)

  __register_blueprints__(app)

  return app
