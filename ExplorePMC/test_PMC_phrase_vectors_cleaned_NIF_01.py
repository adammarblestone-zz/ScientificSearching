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
    model = gensim.models.Word2Vec.load("../../PubMed/NEURO-PHRASE-VECTOR-CLEANED-NONBINARY")
    model.init_sims(replace = True)
    vocab = model.index2word

    print "\nLoading NIF phrases...\n"
    common = open("../ExploreNIF/named_entities.txt").readlines()

    outfile = open("../../nif-sims-1.txt", 'w')

    for c in common:
        line = c.replace(" ", "_").lower()[:-1]
        if line in vocab:
            print line
	    outfile.write("\n" + line)
            print "-------
            outfile.write("\n______________")
            sims = model.most_similar(positive=[line]) # this needs to be changed to allow phrases
            for p in sims:
                outfile.write("\n" + p[0])
                print p
            
if __name__ == '__main__':
    main()
