import gensim
import numpy as np
import matplotlib.pyplot as plt
import os
import io
import nltk
import logging

from matplotlib.mlab import PCA as PCA
from mpl_toolkits.mplot3d import Axes3D


#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

'''Outputs word+vector data for visualization using textSNE: https://github.com/turian/textSNE'''

def main():
    print "\nLoading Word2Vec model...\n"
    model = gensim.models.Word2Vec.load("word2vec_model_1")
    model.init_sims(replace=True)
    vocab = model.index2word
    
    print "\nWriting data to file..."
    outfile = open("saved_outputs/word_vector_mapping_1.txt", 'w')
    for v in vocab:
        fullVectorStr = "".join([" " + str(model[v][j]) for j in range(len(model[v]))])
        outfile.write(v + fullVectorStr + "\n")
    
    outfile.close()
            
if __name__ == '__main__':
    main()
    
    
