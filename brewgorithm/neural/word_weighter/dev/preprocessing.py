import numpy as np
from ..access_ext import language
from ..access_ext import beer_emb
from . import data

cleaning = language.cleaning
parsing = language.parsing


def get_word_vector(word, used_words):
  """For an input data word, return the word vector if possible, None if not."""
  words = parsing.parse_doc(word)
  # no multi word datapoints
  if len(words) != 1:
    return None

  token = words[0]
  # no duplicate datapoints
  if cleaning.clean_word(token.text) in used_words:
    return None

  word_vector = beer_emb.embed_word(token.text)
  # if an embedding doesn't exist for a word, ignore
  if not word_vector.any():
    return None
  else:
    used_words.append(cleaning.clean_word(token.text))
    return word_vector


def get_training_data():
  """Create inputs and labels as numpy arrays."""
  beer_words, non_beer_words = data.get_data()

  used_words = []
  training_X, training_Y = [], []

  # positive samples
  for word in beer_words:
    word_vector = get_word_vector(word, used_words)
    if word_vector is not None:
      training_X.append(word_vector)
      training_Y.append(1)

  # negative samples
  for word in non_beer_words:
    word_vector = get_word_vector(word, used_words)
    if word_vector is not None:
      training_X.append(word_vector)
      training_Y.append(0)

  training_X = np.array(training_X)
  training_Y = np.array(training_Y)

  # Verify that no nan's are in training data
  assert not np.isnan(np.min(training_X))
  assert not np.isnan(np.min(training_Y))

  return unison_shuffled_copies(training_X, training_Y)


def unison_shuffled_copies(a, b):
  """Return shuffled copies of a and b."""
  assert len(a) == len(b)
  p = np.random.permutation(len(a))
  return a[p], b[p]
