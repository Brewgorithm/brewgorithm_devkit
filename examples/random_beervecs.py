from brewgorithm import beer2vec

for beer in beer2vec.get_beer2vec()[:4]:
   beer_vector = beer['vector']
   beer_name = beer['BeerNamePlain']
   print(beer_name)