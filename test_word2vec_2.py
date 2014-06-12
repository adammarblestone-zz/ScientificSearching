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
    model.init_sims(replace=True)
    
    # example of finding similar words to a given vector
    for s in ["glia", "tetrode", "neuron", "cognitive", "animal", "GABA", "stimulation", "auditory", "binding"]:
        print "\nMost similar words to: %s \n" % s
        print model.most_similar(positive=[s])
        print "\n"
        
        # get difference vectors, and find the word most similar to each difference vector: this did not give "meaningful" results
        sims = model.most_similar(positive=[s])
        for k in sims:
            print "\nrelated word:"
            print k[0]
            diff = model[s] - model[k[0]]
            print "most similar vector to difference vector:"
            dot_products = [np.dot(model[model.index2word[i]], diff) for i in range(len(model.index2word))]
            closest_word = model.index2word[dot_products.index(max(dot_products))]
            print closest_word
            print "most similar vector to 'minus' the difference vector:"
            diff = -1 * diff
            dot_products = [np.dot(model[model.index2word[i]], diff) for i in range(len(model.index2word))]
            closest_word = model.index2word[dot_products.index(max(dot_products))]
            print closest_word

if __name__ == '__main__':
    main()