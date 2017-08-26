import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from .load import get_beer2vec
from .access_ext import beer_emb, word_weighter


def run_demo():
  beer_labels = get_beer2vec()
  beer_vectors = [beer['vector'] for beer in beer_labels]

  while True:
    text = input("Positive sentence: ")
    embeddings = beer_emb.embed_doc(text, word_weighter.is_beer_related)
    text = input("Negative sentence: ")
    if True:
      embeddings = np.concatenate((embeddings, (beer_emb.embed_doc(text, word_weighter.is_beer_related) * -0.7)), axis=0)
      emb = np.average(embeddings, axis=0)
    elif False:
      emb = np.average(embeddings, axis=0)
      embeddings = beer_emb.embed_doc(text, word_weighter.is_beer_related) * -1.5
      emb2 = np.average(embeddings, axis=0)
      emb = np.average(emb, emb2)
    if np.all(emb == 0):
      print("Non-significant")
      continue

    sims = cosine_similarity([emb], beer_vectors).reshape(-1)
    candidates = []
    for i, sim in enumerate(sims):
      candidates.append((sim, i))
    result = [x for x in sorted(candidates, key=lambda i: i[0], reverse=True)[:3]]
    for i, x in enumerate(result):
      desc = [a[0] for a in beer_emb.most_similar(positive=[beer_vectors[x[1]]], negative=[])]
      print("Res", i, "called: ", beer_labels[x[1]]['BeerNamePlain'], "\nwith description:", desc)
      print("Alcohol:", beer_labels[x[1]]['Alcohol'])
      print("AverageRating:", beer_labels[x[1]]['AverageRating'])


if __name__ == "__main__":
  run_demo()

