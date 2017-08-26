From tensorflow/tensorflow:latest-py3

# Install apk packages
RUN apt update \
  && apt install gcc make libc-dev g++ bzip2 git libssl-dev openssl freetds-dev build-essential -y

# Establish working directory
WORKDIR /service 

# Copying pip requirement files 
COPY ./requirements.txt ./requirements.txt
COPY ./sense2vec_requirements.txt ./sense2vec_requirements.txt

# Install python dependencies
RUN export C_INCLUDE_PATH=/usr/include
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt
RUN pip3 install -r ./sense2vec_requirements.txt
RUN pip3 install git+git://github.com/explosion/sense2vec.git@e3e871d46101dfe51b2eff0f9ac4a6e15f951ef7 

# Download natural language models
RUN python3 -m spacy.en.download 
RUN sputnik --name sense2vec --repository-url http://index.spacy.io install reddit_vectors
