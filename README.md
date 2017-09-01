# Brewgorithm Development Kit
This is the open source Brewgorithm development kit. This Python library allows any developer to leverage Brewgorithm's basic machine learning models. 

### Overview
Pre-trained Beer2vec model
* This module offers pretrained vector representations of beers.
* As with word embeddings, axises correspond to latent factors in the beer space, and the greater the cosine similarity of two beer vectors, the more similar those two beers are.

Beer-focused Word Embeddings
* This module offers pre-trained word embeddings specially designed to offer a deeper level of granularity for beer-specific vocabulary.
* Embeddings are offered at 64, 128, 256, and 512 dimensions.

Beer-relatedness word weighter
* This system offers a shallow, dense neural network defined in Keras that weights whether a given word vector represents a word that is beer-related.
* The word vectors the pre-trained model has been trained to handle come from `neural/beer_emb`.

Language module
* This module offers basic access to Sense2vec and Spacy utilities. It offers parsing as well as cleaning functions to help expedite development of natural language-related preprocessing.

### Redactions
Only basic models are provided through this development kit. Advanced models, such as food-beer pairing suggestion networks must be requested through conrad.barret@zx-ventures.com. In addition, some training scripts are likewise excluded from this open source release.

### Installation
To install this library, run:
* `pip install -r requirements.txt`
* `pip install -e .`

To run tests, please execute tests in Docker:
* `docker-compose up --build`
* `bash access_cluster.sh`
* `pip install -e .`
* `py.test tests`

### Contributors
Please find a list of contributors under `contributors.txt`.

### License
Copyright 2017 Brewgorithm and contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

