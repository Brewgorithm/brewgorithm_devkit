import unittest
import numpy as np
import brewgorithm

NATURAL_EMB_DIM = brewgorithm.language.config.NATURAL_EMB_DIM
get_max_similarity = brewgorithm.language.sense_emb.get_max_similarity
classify_word = brewgorithm.language.sense_emb.classify_word
concatenate_word_and_pos = brewgorithm.language.sense_emb.concatenate_word_and_pos
embed_word = brewgorithm.language.sense_emb.embed_word
embed_doc = brewgorithm.language.sense_emb.embed_doc


class TestSenseEmb(unittest.TestCase):
  """Test the sense embedding functions."""

  def test_get_max_similarity(self):
    """Test that the function returns the max cosine similarity."""
    vector1 = np.array([1., 1.])
    vector2 = np.array([1.1, 1.1])
    vector3 = np.array([2., 2.])
    similarity1 = get_max_similarity(vector1, [vector2, vector3])
    similarity2 = get_max_similarity(vector1, [vector2])
    self.assertTrue(np.allclose(similarity1, similarity2))

  def test_classify_word(self):
    """Test that the word gets classified as the one with the closest words."""
    word = 'good'
    class1 = ['decent', 'bad', 'awful', 'car']
    class2 = ['disgusting', 'salad', 'telephone']
    index = classify_word(word, [class1, class2])
    self.assertEqual(index, 0)

  def test_concatenate_word_and_pos(self):
    """Test that we get a sense2vec style word and pos concatenation."""
    word = 'dislike'
    pos = 'VERB'
    self.assertEqual(concatenate_word_and_pos(word, pos), 'dislike|VERB')

  def test_embed_word(self):
    """Test that we get a numpy array of correct size as return."""
    word = 'blue'
    pos = 'ADJ'
    # it works both when providing a pos tag and when not
    self.assertTrue(np.allclose(embed_word(word), embed_word(word, pos)))
    # we get a numpy array returned
    self.assertTrue(type(embed_word(pos)).__module__, np.__name__)
    # the numpy array is a vector with length NATURAL_EMB_DIM
    self.assertEqual(embed_word(word).shape[0], NATURAL_EMB_DIM)

  def test_embed_doc(self):
    """Test that we get a numpy array as return."""
    doc_string = 'this is a blue cow'
    # we get a numpy array returned
    self.assertTrue(type(embed_doc(doc_string)).__module__, np.__name__)
    # the numpy array is a matrix with second dimension NATURAL_EMB_DIM
    self.assertEqual(embed_doc(doc_string).shape[1], NATURAL_EMB_DIM)
    # ...and first dimension <= len(doc_string.split())
    self.assertTrue(embed_doc(doc_string).shape[0] <= len(doc_string.split()))


if __name__ == '__main__':
  unittest.main()
