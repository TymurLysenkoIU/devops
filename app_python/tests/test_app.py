import datetime
from flask.testing import FlaskClient


def test_root(client: FlaskClient) -> None:
    """Check that / endpoint returns datetime as a string"""
    root_endpoint_result: str = client.get('/').get_data(as_text=True)
    parsed_date_time: datetime.datetime = datetime.datetime.fromisoformat(
        root_endpoint_result)
    assert isinstance(parsed_date_time, datetime.datetime)
