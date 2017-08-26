import unittest
from brewgorithm import smalltalk

query_agent = smalltalk.api_ops.query_agent
perform_request = smalltalk.api_ops.perform_request
retrieve_text_from_response = smalltalk.api_ops.retrieve_text_from_response


class TestApiOps(unittest.TestCase):
  """Test the api ops."""

  def test_query_agent(self):
    """Test that query_agent returns relevant information."""
    query = "Hey there!"
    response = query_agent(query)
    self.assertTrue(isinstance(response, str))

  def test_perform_request(self):
    """Test that perform_request returns relevant information."""
    query = "Hey there!"
    response = perform_request(query)
    self.assertTrue(isinstance(response, dict))

  def test_retrieve_text_from_response(self):
    """Test that retrieve_text_from_response returns relevant information."""
    query = "Hey there!"
    response_json = perform_request(query)
    self.assertIn('result', response_json)
    self.assertIn('fulfillment', response_json['result'])
    self.assertIn('speech', response_json['result']['fulfillment'])
    response = retrieve_text_from_response(response_json)
    self.assertTrue(isinstance(response, str))


if __name__ == '__main__':
  unittest.main()
