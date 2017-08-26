import pickle
from .config import MODEL_DIR, MODEL_NAME

beer_labels = pickle.load(open(MODEL_DIR + MODEL_NAME, "rb"))


def get_beer2vec():
  return beer_labels


