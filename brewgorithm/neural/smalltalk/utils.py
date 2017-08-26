import uuid


def create_session_id():
  """Return a 36 characters random session id string."""
  return str(uuid.uuid4())
