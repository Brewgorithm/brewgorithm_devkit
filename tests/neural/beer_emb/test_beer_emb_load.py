from brewgorithm import beer_emb, word_weighter
import numpy as np
import unittest
from sklearn.metrics.pairwise import cosine_similarity


class TestBeerEmb(unittest.TestCase):
  def test_most_similar_test(self):
    self.assertIn("cocoa", [option[0] for option in beer_emb.most_similar("chocolate")])
    self.assertIn("pale", [option[0] for option in beer_emb.most_similar(["sweet"], negative=["chocolate"])])

  def test_embed_word_test(self):
    self.assertEqual(beer_emb.embed_word("aweofawoeif").shape[0], beer_emb.config.EMB_DIM)
    self.assertTrue(np.all(beer_emb.embed_word("aweofawoeif") == np.zeros(beer_emb.config.EMB_DIM)))
    self.assertEqual(beer_emb.embed_word("aweofawoeif", None).shape[0], beer_emb.config.EMB_DIM)
    self.assertTrue(np.all(beer_emb.embed_word("aweofawoeif", None) == np.zeros(beer_emb.config.EMB_DIM)))

    self.assertTrue(cosine_similarity([beer_emb.embed_word("chocolate")], [beer_emb.embed_word("caramel")])[0][0] > cosine_similarity([beer_emb.embed_word("chocolate")], [beer_emb.embed_word("strawberry")])[0][0])

  def test_embed_doc_test(self):
    self.assertTrue(len(beer_emb.embed_doc("i want chocolate fruits", None)) == 4)
    self.assertTrue(len(beer_emb.embed_doc("i want chocolate fruits awoefijawoiefjeawo", None)) == 4)
    self.assertTrue(len(beer_emb.embed_doc("i want chocolate fruits awoefijawoiefjeawo", word_weighter.is_beer_related)) == 2)

    self.assertGreater(cosine_similarity([np.mean(beer_emb.embed_doc("chocolate caramel", None), axis=0)], [np.mean(beer_emb.embed_doc("dark rich", None), axis=0)])[0][0], cosine_similarity([np.mean(beer_emb.embed_doc("chocolate", None), axis=0)], [np.mean(beer_emb.embed_doc("fruity sour", None), axis=0)])[0][0])

  def test_get_model_test(self):
    self.assertIn("chocolate", beer_emb.get_model())
    self.assertNotIn("awoefijwaoijfa", beer_emb.get_model())


if __name__ == '__main__':
  unittest.main()
