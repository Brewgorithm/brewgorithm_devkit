import operator
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import sense2vec
from .config import NATURAL_EMB_DIM, SENSE2VEC_POS_TAGS
from .cleaning import clean_word
from .parsing import tokenize

model = sense2vec.load()


def get_max_similarity(wv, list_of_wvs):
  """Return the max cosine similarity between a wv and a list_of_wvs."""
  return max(cosine_similarity([wv], list_of_wvs).flatten())


def classify_word(word, classes):
  """Return the class index that the word is most similar to.

  Arguments:
    word -- string of a word
    classes -- list of list of words that constitute some class
  """
  wv = embed_word(clean_word(word))
  similarities = []
  # calculate the max similarity of word to any of the words in each class
  for words in classes:
    list_of_wvs = [embed_word(clean_word(word)) for word in words]
    similarities.append(get_max_similarity(wv, list_of_wvs))
  # return the class that contains the word that is most similar
  return similarities.index(max(similarities))


def concatenate_word_and_pos(word, pos):
  """Return sense2vec style string concatenation of word and pos tag."""
  return word + '|' + pos


def embed_word(word, pos=False):
  """Return sense2vec embedding for a word.

  Arguments:
    word -- string of a word
    pos -- part-of-speech tag of that word (string)
  """
  word = clean_word(word)
  pos_options = {}

  # If pos is given, first attempt a direct pos embed match
  if pos is not False:
    word_pos = concatenate_word_and_pos(word, pos)
    if word_pos in model:
      _, query_vector = model[word_pos]
      return query_vector

  # Explore possible POS
  for pos in SENSE2VEC_POS_TAGS:
    word_pos = concatenate_word_and_pos(word, pos)
    if word_pos in model:
      frequency, query_vector = model[word_pos]
      pos_options[word_pos] = frequency
  if word in model:
    frequency, query_vector = model[word]
    pos_options[word] = frequency

  # No pos matches
  if not pos_options:
    if word in model:
      _, query_vector = model[word]
      return query_vector
    else:
      return np.zeros(NATURAL_EMB_DIM)
  else:
    # If pos match, select the one with best frequency
    best_pos_word = max(pos_options.items(), key=operator.itemgetter(1))[0]
    _, query_vector = model[best_pos_word]
    return query_vector


def embed_doc(doc_string):
  """Given a doc string, parse it and calculate embeddings.

  Return:
    embeddings -- numpy array 2d, (number_of_token_embeddings X NATURAL_EMB_DIM)
  """
  embeddings = []
  for token in tokenize(doc_string, clean=False):
    word_vector = embed_word(clean_word(token.text), token.pos_)
    if np.all(word_vector == 0):
      continue
    embeddings.append(word_vector)
  if len(embeddings) == 0:
    return np.zeros((1, NATURAL_EMB_DIM))
  return np.array(embeddings)


def get_model():
  """Return the sense2vec word vector model."""
  return model

