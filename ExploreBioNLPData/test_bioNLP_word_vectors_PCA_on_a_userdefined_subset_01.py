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

'''Visualize semantic relations using PCA, i.e., projecting a user-defined set of vectors onto an optimal 2D subspace.'''

def main():
    print "Loading Word2Vec model..."
    # 4 GB input file, uses about 20 GB of memory when loaded
    '''Uses the model from: http://bio.nlplab.org/'''
    model = gensim.models.Word2Vec.load_word2vec_format("../../PubMed/BioNLP/wikipedia-pubmed-and-PMC-w2v.bin", binary = True)
    model.init_sims(replace=True)
    vocab = model.index2word

    while True:
    	seed_string = raw_input('\nprompt> ')
    	seed_word_list = list(set(seed_string.split())) # set gets the unique elements here

    	print "Seed words:"
    	for word in seed_word_list:
		print word
        
        print "Finding a bunch of similar words..."
    	derived_word_list = []
        for s in seed_word_list:
		if s in vocab:
			print "\tSearching for similarities for %s" % s
			l = [m[0] for m in model.most_similar(positive = [s])]
			derived_word_list += l

	if len(derived_word_list) == 0:
		continue

	derived_word_list = list(set(derived_word_list))

    	print "Derived words:"
    	for word in derived_word_list:
        	print word

    	data_matrix = np.array([model[s] for s in derived_word_list])
    
    	print "Running PCA..."
    	pca_results = PCA(data_matrix)
    	projected_vectors = []
    	for word in seed_word_list:
		if word in vocab:
			f = model[word]
			projected_vectors.append(pca_results.project(f))
    
    	print "Plotting PCA results..."
    	fig = plt.figure()
    	ax = fig.add_subplot(111, projection = '3d')
    	ax.set_title("Principal Components of Word Vectors")

	plots = []
    
    	import itertools
    	marker = itertools.cycle(['o', '^', '*', "s", "h", "8"])
    	colorList = ["r", "b", "g", "y", "k", "c", "m", "w"]
    	colors = itertools.cycle(colorList)
        
    	m = marker.next()
    	for i in range(len(projected_vectors)):
        	col = colors.next()
        	if i % len(colorList) == 0:
            	    m = marker.next()

        	p = ax.plot([projected_vectors[i][0]], [projected_vectors[i][1]], [projected_vectors[i][2]], marker = m, markersize = 21, color = col, label = seed_word_list[i], linestyle = "none")
		plot.append(p)
        
        ax.legend(plots, seed_word_list, loc = "upper left")
        plt.show()
            
if __name__ == '__main__':
    main()
    
    
