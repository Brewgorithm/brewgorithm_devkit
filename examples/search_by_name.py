from brewgorithm import beer2vec

map = {}
for beer in beer2vec.get_beer2vec():
   map[beer['BeerNamePlain'].lower().strip()] = beer['vector']

# Getting goose island or something
beer_vec = map["orval".lower()]
beer_vec2 = map["alesmith speedway stout".lower()]

# Find similarity between goose island and something
from sklearn.metrics.pairwise import cosine_similarity
print(cosine_similarity([beer_vec], [beer_vec2])[0][0])