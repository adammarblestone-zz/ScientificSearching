import gensim
import numpy as np
import matplotlib.pyplot as plt
import os
import io
import nltk
import logging

from matplotlib.mlab import PCA as PCA

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

'''Visualize semantic relations using PCA, i.e., projecting a user-defined set of vectors onto an optimal 2D subspace.'''

def main():
    print "Loading Word2Vec model..."
    # 4 GB input file, uses about 20 GB of memory when loaded
    '''Uses the model from: http://bio.nlplab.org/'''
    model = gensim.models.Word2Vec.load_word2vec_format("../../PubMed/BioNLP/wikipedia-pubmed-and-PMC-w2v.bin", binary = True)
    #model = gensim.models.Word2Vec.load("../../PubMed/derived_from_neuroscience_abstracts/word2vec_model_1")
    model.init_sims(replace=True)
    vocab = model.index2word

    while True:
    	seed_string = raw_input('\nprompt> ')
    	seed_word_list = list(set(seed_string.split())) # set gets the unique elements here

    	print "Seed words:"
    	for word in seed_word_list:
		print word
        

	# choose how many words to find to allow numrows > numcols in PCA
	vector_length = len(model[vocab[0]])
	top_vecs = int(1 + float(vector_length) / float(len([s for s in seed_word_list if s in vocab])))
	if top_vecs < 15:
		top_vecs = 15

        print "Finding a bunch of similar words..."
    	derived_word_list = []
        for s in seed_word_list:
		if s in vocab:
			print "\tSearching for similarities for %s" % s
			l = [m[0] for m in model.most_similar(positive = [s], topn = top_vecs)]
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
	word_short_list = []
    	for word in seed_word_list:
		if word in vocab:
			f = model[word]
			projected_vectors.append(pca_results.project(f))
			word_short_list.append(word)

	
    
    	print "Plotting PCA results..."
    	fig = plt.figure()
    	plt.title("Principal Components of Word Vectors")

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

        	p, = plt.plot([projected_vectors[i][0]], [projected_vectors[i][1]], marker = m, markersize = 21, color = col, linestyle = "none")
		plots.append(p)
        
        plt.legend(plots, word_short_list, loc = "upper left", numpoints = 1)
        plt.show()
            
if __name__ == '__main__':
    main()
    
    
