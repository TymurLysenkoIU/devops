import pytest

from app import create_app

__test_config__ = {
  'TESTING': True
}


@pytest.fixture
def client():
  app = create_app(__test_config__)

  with app.test_client() as result_client:
    with app.app_context():
      pass  # For now there is nothing to do with this
    yield result_client
