import gensim
import numpy as np
import matplotlib.pyplot as plt
import os
import io
import nltk
import logging

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def main():
    print "\nLoading Word2Vec model...\n"
    model = gensim.models.Word2Vec.load("word2vec_model_1")
    # print model.vocab
    for s in ["neuron", "glia", "tetrode", "opsin", "GABA"]:
        print "Most similar words to: %s \n" % s
        print model.most_similar(positive=[s])
        print "\n"

if __name__ == '__main__':
    main()