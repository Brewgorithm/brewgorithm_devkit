import requests
from . import config


def download_file(url, filename):
  '''
  Generic function to stream-download a large file
  '''
  r = requests.get(url, stream=True)
  with open(filename, 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
      if chunk:
        f.write(chunk)
  return filename


if __name__ == "__main__":
  download_file(config.SMALL_URL, config.MODEL_DIR + config.SMALL_NAME)
  download_file(config.MID_URL, config.MODEL_DIR + config.MID_NAME)
  download_file(config.LARGE_URL, config.MODEL_DIR + config.LARGE_NAME)
  download_file(config.X_LARGE_URL, config.MODEL_DIR + config.X_LARGE_NAME)

