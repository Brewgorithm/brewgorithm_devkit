import requests
from .config import API_AI_ACCESS_TOKEN, API_AI_VERSION, API_AI_BASEURL
from .utils import create_session_id


def perform_request(query_text):
  """Perform the actual GET request to the API and return the response."""
  headers = {
      'Authorization': 'Bearer {}'.format(API_AI_ACCESS_TOKEN)
      }

  # TODO check if session id exists in user dict
  params = {
      'v': API_AI_VERSION,
      'query': query_text,
      'lang': 'en',
      'sessionId': create_session_id()
      }

  response = requests.get(API_AI_BASEURL, headers=headers, params=params)
  response_json = response.json()
  return response_json


def retrieve_text_from_response(response_json):
  """Retrieve the text part of the API.ai response."""
  try:
    print(response_json)
    # TODO save session id from response to user dict
    return response_json['result']['fulfillment']['speech']
  except KeyError as e:
    print("Could not get relevant information from the API.ai response: {}"
          .format(e))
    return None


def query_agent(query_text):
  """Query the api.ai agent with the input query text.

  return text part of the API.ai response
  """
  # perform the request
  try:
    response_json = perform_request(query_text)
  except requests.exceptions.RequestException as e:
    print("Error occured when querying API.ai: {}".format(e))
    return ""

  # return the relevant information from the response JSON
  return retrieve_text_from_response(response_json)
