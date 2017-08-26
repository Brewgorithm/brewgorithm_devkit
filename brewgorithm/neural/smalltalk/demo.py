from . import load as process_query


def run_demo():
  """Run the demo, print demo outputs."""
  demo_query = "Hey. How are you?"
  response = process_query.process(demo_query)
  print(demo_query)
  print(response)


if __name__ == "__main__":
  run_demo()
