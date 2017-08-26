import spacy
from . import cleaning

nlp = spacy.load('en')


def get_model():
  """Return the spacy nlp pipeline model."""
  return nlp


def parse_doc(doc_string):
  """Run a string through the spacy nlp pipeline, return spacy Doc object."""
  return nlp(str(doc_string))


def tokenize(input_text, clean=True, run_light=True):
  """Generate tokens from an input text and yield them.

  Arguments:
    input_text -- the text to tokenize
    clean -- remove uncommon characters from each token
    run_light -- don't run the complete nlp pipeline

  """
  # run a light nlp (only tokenizer and tagger)
  if run_light:
    parsed_doc = nlp.tokenizer(str(input_text))
    nlp.tagger(parsed_doc)
  # run the full nlp pipeline
  else:
    parsed_doc = parse_doc(str(input_text))

  for token in parsed_doc:
    if clean:
      if token.pos_ not in ['SPACE', 'PUNCT', 'X']:
        yield cleaning.clean_word(token.text)
    else:
      yield token
