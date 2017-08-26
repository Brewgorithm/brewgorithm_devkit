* A fallback gate that uses the api.ai smalltalk module to give a response to the user in case we can't parse anything useful from the query

### Files overview:
__init__.py: imports functions from load.py
demo.py: quick demo
load.py: main code entry point
config.py: storing constants
access_ext.py: central import gateway for interacting with other modules in the project
