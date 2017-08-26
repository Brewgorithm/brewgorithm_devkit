from .api_ops import query_agent


def process(text):
  """Process the query text and return an appropriate response."""
  return query_agent(text)
