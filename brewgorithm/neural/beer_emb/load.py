from gensim.models import Word2Vec
import numpy as np
from .config import MODEL_NAME, MODEL_DIR, EMB_DIM
from .access_ext import language

clean_word = language.cleaning.clean_word
parsing = language.parsing

model = Word2Vec.load(MODEL_DIR + MODEL_NAME)


def most_similar(positive=None, negative=None):
  """Return most similar words as described by positive and negative words.

  Return:
    most_similar_words -- list of tuples (word, similarity_score)
  """
  if positive is None:
    positive = []
  if negative is None:
    negative = []
  return model.wv.most_similar_cosmul(positive=positive, negative=negative)


def embed_word(word, default=None):
  """Return beer embedding for a word."""
  if default is None:
    default = np.zeros(EMB_DIM)

  word = clean_word(word)
  if word in model:
    return model.wv[word]
  else:
    return default


def embed_doc(doc_string, word_filter):
  """Given a doc string, parse it and calculate embeddings.

  Return:
    embeddings -- numpy array 2d, (number_of_token_embeddings X EMB_DIM)
  """
  embeddings = []
  # for each token in the doc string
  for token in parsing.tokenize(doc_string, clean=False):
    word_vector = embed_word(clean_word(token.text))
    # when the word vector is all zeros
    if not word_vector.any():
      continue

    # if there is no word_filter or the word filter is positive
    if not word_filter or word_filter(word_vector):
      embeddings.append(word_vector)
    else:
      continue
  # if no embedding was found for any of the tokens in the doc_string
  if len(embeddings) == 0:
    return np.zeros((1, EMB_DIM))
  return np.array(embeddings)


def get_model():
  """Return the beer embedding model instance."""
  return model
