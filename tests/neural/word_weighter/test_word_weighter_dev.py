import unittest
from brewgorithm import word_weighter
from brewgorithm import beer_emb


class TestWordWeighterDev(unittest.TestCase):
  """Test the word weighter functions."""

  def test_is_beer_related(self):
    """Test some no-brainer cases."""
    word1 = 'pilsener'
    word2 = 'car'
    self.assertTrue(word_weighter.is_beer_related(beer_emb.embed_word(word1)))
    self.assertFalse(word_weighter.is_beer_related(beer_emb.embed_word(word2)))

  def test_data(self):
    self.assertTrue("amber" in word_weighter.dev.data.get_data()[0])
    self.assertTrue("rich" in word_weighter.dev.data.get_data()[0])
    self.assertFalse("it" in word_weighter.dev.data.get_data()[0])
    self.assertFalse("!" in word_weighter.dev.data.get_data()[0])

    self.assertFalse("amber" in word_weighter.dev.data.get_data()[1])
    self.assertFalse("rich" in word_weighter.dev.data.get_data()[1])
    self.assertTrue("it" in word_weighter.dev.data.get_data()[1])
    self.assertTrue("!" in word_weighter.dev.data.get_data()[1])

    backup_sentiment = word_weighter.config.SENTIMENT_IS_DESCRIPTOR

    word_weighter.config.SENTIMENT_IS_DESCRIPTOR = True
    self.assertIn("gross", word_weighter.dev.data.get_data()[0])
    self.assertFalse("gross" in word_weighter.dev.data.get_data()[1])

    word_weighter.config.SENTIMENT_IS_DESCRIPTOR = False
    self.assertFalse("gross" in word_weighter.dev.data.get_data()[0])
    self.assertTrue("gross" in word_weighter.dev.data.get_data()[1])

    word_weighter.config.SENTIMENT_IS_DESCRIPTOR = backup_sentiment

  def test_preprocessing(self):
    # Filters redundancys
    self.assertIsNone(word_weighter.dev.preprocessing.get_word_vector("chocolate", ["chocolate", "apple"]))
    # Filters zeroes
    self.assertIsNone(word_weighter.dev.preprocessing.get_word_vector("oaiwjefoiawjfoij", ["chocolate", "apple"]))
    # Works normally
    self.assertIsNotNone(word_weighter.dev.preprocessing.get_word_vector("chocolate", ["fruity", "apple"]))

  def test_training_with_sentiment(self):
    """Test some no-brainer cases."""
    backup_sentiment = word_weighter.config.SENTIMENT_IS_DESCRIPTOR
    word_weighter.config.SENTIMENT_IS_DESCRIPTOR = True

    word_weighter.dev.train.train("test_sentiment.model")
    self.test_is_beer_related()

    word_weighter.config.SENTIMENT_IS_DESCRIPTOR = backup_sentiment

  def test_training_without_sentiment(self):
    """Test some no-brainer cases."""
    backup_sentiment = word_weighter.config.SENTIMENT_IS_DESCRIPTOR
    word_weighter.config.SENTIMENT_IS_DESCRIPTOR = False

    word_weighter.dev.train.train("test_no_sentiment.model")
    self.test_is_beer_related()

    word_weighter.config.SENTIMENT_IS_DESCRIPTOR = backup_sentiment


if __name__ == '__main__':
  unittest.main()
