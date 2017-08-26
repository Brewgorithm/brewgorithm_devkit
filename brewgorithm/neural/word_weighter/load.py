from keras.models import load_model
from .config import MODEL_DIR, MODEL_NAME, EMB_DIM

model = load_model(MODEL_DIR + MODEL_NAME)


def get_model():
  """Return the keras model used for beer relatedness classification."""
  return model


def is_beer_related(word_vector, threshold=0.8):
  """Return True if the word_vector is beer related, False otherwise."""
  # when the word_vector is a zero vector
  if not word_vector.any():
    return False
  score = model.predict(word_vector.reshape((-1, EMB_DIM)))[0][0]
  return score > threshold
