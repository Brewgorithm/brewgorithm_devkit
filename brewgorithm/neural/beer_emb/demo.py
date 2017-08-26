from .access_ext import language
from .load import most_similar

parsing = language.parsing
cleaning = language.cleaning


def run_demo():
  """Run the demo, returning you the most similar between pos and neg words."""
  print("Beer algebra demo: ")
  while True:
    pos_query = str(input("Enter positive words: "))
    neg_query = str(input("Enter negative words: "))
    pos_list = list(parsing.tokenize(pos_query))
    neg_list = list(parsing.tokenize(neg_query))
    print(most_similar(positive=pos_list, negative=neg_list))
    if pos_query == "STOP" or neg_query == "STOP":
      break


if __name__ == "__main__":
  run_demo()
