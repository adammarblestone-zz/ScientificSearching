import gensim
import numpy as np
import matplotlib.pyplot as plt
import os
import io
import nltk
import logging

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

'''Displays similar terms to an input term.'''

def main():
    print "\nLoading Word2Vec model...\n"
    # 4 GB input file, uses about 20 GB of memory when loaded
    model = gensim.models.Word2Vec.load_word2vec_format("../../PubMed/BioNLP/wikipedia-pubmed-and-PMC-w2v.bin", binary = True)
    model.init_sims(replace=True)
    vocab = model.index2word

    while True:
        line = raw_input('\nprompt> ')
        if line in vocab:
            print "\nSimilar words:"
            print "______________"
            sims = model.most_similar(positive=[line.split()[0]])
            for p in sims:
                print p
        else:
            print "Sorry: not in vocabulary!"
            
if __name__ == '__main__':
    main()
