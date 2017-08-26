import re


def clean_word(word):
  """Lower-case and remove uncommon characters from a word."""
  return re.compile('[^a-zA-Z0-9_]').sub('', str(word.lower()))


def clean_doc(doc):
  """Lower-case and remove uncommon characters from a word."""
  cleaned_doc = []
  for word in doc.split(" "):
    cleaned_doc.append(clean_word(word))

  return " ".join(cleaned_doc)


def filter_nulls(field):
  """Filter out null field values, float conversion otherwise."""
  if field is None or field == "<null>":
    return 0
  else:
    try:
      return float(field)
    except ValueError:
      return str(field)
