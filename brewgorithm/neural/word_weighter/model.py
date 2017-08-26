from .access_ext import beer_emb
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.core import Dropout


def build_model():
  """Build and return a keras model for classifying beer related words."""
  model = Sequential()
  model.add(Dense(beer_emb.EMB_DIM, activation="relu",
                  input_dim=beer_emb.EMB_DIM))
  model.add(Dropout(0.5))
  model.add(Dense(64, activation="relu"))
  model.add(Dropout(0.5))
  model.add(Dense(32, activation="relu"))
  model.add(Dense(1, activation='sigmoid'))
  model.compile(loss='binary_crossentropy',
                metrics=['accuracy'], optimizer='adam')

  return model
