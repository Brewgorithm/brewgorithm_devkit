From tensorflow/tensorflow:latest-py3

# Install apk packages
RUN apt update \
  && apt install gcc make libc-dev g++ bzip2 git libssl-dev openssl build-essential -y

# Establish working directory
WORKDIR /service 

# Copying pip requirement files 
COPY ./requirements.txt ./requirements.txt

# Install python dependencies
RUN export C_INCLUDE_PATH=/usr/include
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt

# Download natural language models
RUN python3 -m spacy.en.download 

# Install dev-only dependencies
RUN pip3 install pytest

# install brewgorithm stuff
RUN pip3 install brewgorithm

RUN python3 -m brewgorithm.neural.beer_emb.download