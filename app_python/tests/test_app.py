import datetime


def test_root(client):
  """Check that / endpoint returns datetime as a string"""
  root_endpoint_result = client.get('/').get_data(as_text=True)
  parsed_date_time = datetime.datetime.fromisoformat(root_endpoint_result)
  assert isinstance(parsed_date_time, datetime.datetime)
