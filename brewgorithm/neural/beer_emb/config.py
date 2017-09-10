import os

MODEL_DIR = os.path.dirname(os.path.realpath(__file__)) + "/models/"

SMALL_NAME = "server64.model"
MID_NAME = "server128.model"
LARGE_NAME = "server256.model"
X_LARGE_NAME = "server512.model"
MODEL_NAME = X_LARGE_NAME

SMALL_URL = "https://brewgorithmdevkit.nyc3.digitaloceanspaces.com/server64.model"
MID_URL = "https://brewgorithmdevkit.nyc3.digitaloceanspaces.com/server128.model"
LARGE_URL = "https://brewgorithmdevkit.nyc3.digitaloceanspaces.com/server256.model"
X_LARGE_URL = "https://brewgorithmdevkit.nyc3.digitaloceanspaces.com/server512.model"

TEXT_CAP = False
EMB_DIM = 512
WINDOW_SIZE = 7
MIN_COUNT = 200
