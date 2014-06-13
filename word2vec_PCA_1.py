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

'''Visualize semantic relations using PCA, i.e., projecting the vectors onto an optimal 2D subspace.'''

def main():
    print "\nLoading Word2Vec model...\n"
    model = gensim.models.Word2Vec.load("word2vec_model_1")
    model.init_sims(replace=True)

    vocab = model.index2word

    data_matrix = np.array([model[vocab[i]] for i in range(len(vocab))])
    
    print "Running PCA..."
    pca_results = PCA(data_matrix)
    
    seed_word_list = ["dopamine", "GABA", "serotonin", "5-HT", "acetylcholine" , "glutamate","electrode", "stimulator", "cognitive", "behavioral", "ethological", "genetic", "biochemical", "channel", "concentration", "dynamics", "receptor", "antibody", "fMRI", "calcium", "nucleus", "axon", "soma", "dendrite", "synapse", "fNIRS", "EEG"]
    
    classes = [[] for s in seed_word_list]
    for i in range(len(seed_word_list)):
        classes[i].append(model[seed_word_list[i]])
        for s in model.most_similar(seed_word_list[i]):
            classes[i].append(model[s[0]])
            
    classes_projected = [[] for s in seed_word_list]
    for i in range(len(seed_word_list)):
        for f in classes[i]:
            classes_projected[i].append(pca_results.project(f))
    
    print "Plotting PCA results..."
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.set_title("Principle Components of Word Vectors")
    
    import itertools
    marker = itertools.cycle(['o', '^', '*', "s", "h", "8"])
    colorList = ["r", "b", "g", "y", "k", "c", "m", "w"]
    colors = itertools.cycle(colorList)
        
    m = marker.next()
    for i in range(len(seed_word_list)):
        col = colors.next()
        if i % len(colorList) == 0:
            m = marker.next()
        
        '''
        # plot the individual words
        ax.scatter([f[0] for f in classes_projected[i]], [f[1] for f in classes_projected[i]], [f[2] for f in classes_projected[i]], marker = m, s = 20, c = col)
        '''
        
        # plot the cluster means
        ax.plot([np.mean([f[0] for f in classes_projected[i]])], [np.mean([f[1] for f in classes_projected[i]])], [np.mean([f[2] for f in classes_projected[i]])], marker = m, markersize = 21, color = col, label = seed_word_list[i], linestyle = "none")
        
    
    ax.legend(numpoints = 1)
    plt.show()
            
if __name__ == '__main__':
    main()
    
    
