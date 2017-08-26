from .. import config
from ..model import build_model
from .preprocessing import get_training_data


def train(model_name):
  inputs, labels = get_training_data()
  model = build_model()
  model.fit(inputs, labels, epochs=config.EPOCHS,
            batch_size=config.BATCH_SIZE, verbose=2)
  model.save(config.MODEL_DIR + model_name)


if __name__ == "__main__":
  print("Starting word weighter training")
  train(config.MODEL_NAME)
  print("Word weighter training complete\nTerminating.")
