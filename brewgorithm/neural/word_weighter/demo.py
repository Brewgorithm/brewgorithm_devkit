from .access_ext import beer_emb
from .load import is_beer_related


def run_demo():
  """Run demo, testing whether input words are beer related."""
  while True:
    embeddings = beer_emb.embed_doc(input("Test if words are beer-related: "),
                                    word_filter=False)
    for word_vec in embeddings:
      print(is_beer_related(word_vec))


if __name__ == "__main__":
  run_demo()
