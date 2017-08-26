from .. import config


def get_data():
  """Return beer_words and non_beer_words as lists."""
  sentiment_words = ["good", "bad", "ok", "disgusting", "amazing",
                     "fantastic", "terrible", "barf", "garbage", "medium", "gross"]
  colors = ["amber", "blond", "brown", "cloudy", "dark", "hazy", "white"]
  descriptor = ["apple", "balsamic", "bitter", "bitterish", "burnt",
                "chocolate", "cinnamon", "cocoa", "coffee", "creamy",
                "dry", "floral", "foam", "fruit", "fruity", "grape", "hop",
                "lavender", "musty", "peach", "pear", "caramel", "coriander",
                "rich", "rotten", "smooth", "sour", "spices", "spicy", "sweet",
                "tart", "sugar", "bitters", "fragrant", "balanced",
                "unbalanced", "sweet", "grainy", "malty", "smoky"]
  abv = ["light", "strong", "heavy"]
  types = ["ipa", "stout", "lambic", "trappist", "sours",
           "ale", "pilsner", "lager"]
  eth = ["german", "british", "american", "belgian", "belgium", "czech"]
  random = ["a", "after", "again", "and", "anything", "at", "beer", "ben",
            "body", "bottle", "but", "competition", "eve", "everyone",
            "festival", "finish", "from", "fuck", "handpump", "here",
            "his", "home", "i", "interesting", "is", "just", "kind", "lots",
            "many", "mouth", "my", "nevertheless", "no", "nose", "not", "of",
            "one", "opening", "quite", "rome", "second", "shared", "so",
            "station", "taste", "thanks", "there", "together", "very", "where",
            "who", "why", "with", "yet", "can", "a", "has", "with", "thanks",
            "pours", "no", "drink", "it", "at", "the", "moment", "!", "2", ",", ".",
            "which", "products", "brands"]

  beer_words = colors + descriptor + abv + types + eth
  non_beer_words = random

  if config.SENTIMENT_IS_DESCRIPTOR:
    beer_words += sentiment_words
    beer_words.append("DESCRIPTOR")
  else:
    non_beer_words += sentiment_words
    beer_words.append("NOT_DESCRIPTOR")

  return beer_words, non_beer_words
