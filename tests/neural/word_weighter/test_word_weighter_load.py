import unittest
from brewgorithm import beer_emb, word_weighter

is_beer_related = word_weighter.is_beer_related


class TestWordWeighter(unittest.TestCase):
  """Test the word weighter functions."""

  def test_is_beer_related(self):
    """Test some no-brainer cases."""
    word1 = 'pilsener'
    word2 = 'car'
    self.assertTrue(is_beer_related(beer_emb.embed_word(word1)))
    self.assertFalse(is_beer_related(beer_emb.embed_word(word2)))


if __name__ == '__main__':
  unittest.main()
