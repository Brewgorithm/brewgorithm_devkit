import unittest
import brewgorithm

clean_word = brewgorithm.language.cleaning.clean_word
filter_nulls = brewgorithm.language.cleaning.filter_nulls


class TestCleaning(unittest.TestCase):
  """Test the cleaning functions."""

  def test_clean_word(self):
    """Test that a word gets cleaned."""
    word1, clean1 = 'abc', 'abc'
    word2, clean2 = '--def_-gh13', 'def_gh13'
    self.assertEqual(clean_word(word1), clean1)
    self.assertEqual(clean_word(word2), clean2)

  def test_filter_nulls(self):
    """Test that nulls are filtered out."""
    test1 = None
    test2 = '<null>'
    test3 = '13'
    self.assertEqual(filter_nulls(test1), 0)
    self.assertEqual(filter_nulls(test2), 0)
    self.assertEqual(filter_nulls(test3), float(test3))


if __name__ == '__main__':
  unittest.main()
