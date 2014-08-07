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
    model = gensim.models.Word2Vec.load_word2vec_format("../../PubMed/NEURO-PHRASE-VECTOR", binary = True)
    model.init_sims(replace=True)
    vocab = model.index2word

    import readline
    readline.parse_and_bind("tab: complete")
    def complete(text,state):
        results = [x for x in vocab if x.startswith(text)] + [None]
        return results[state]

    readline.set_completer(complete)

    while True:
        line = raw_input('\nprompt> ')
        if line in vocab:
            print "\nSimilar words:"
            print "______________"
            sims = model.most_similar(positive=[line]) # this needs to be changed to allow phrases
            for p in sims:
                print p
        else:
            print "Sorry: not in vocabulary!"
            
if __name__ == '__main__':
    main()
