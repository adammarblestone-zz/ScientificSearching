'''Uses gensim and resources downloaded from bio.nlplab.org to take an input phrase from
the user, find similar words to that phrase, and plot their evolution over time.'''

import gzip
import matplotlib.pyplot as plt
import numpy as np
import gensim
import numpy as np
import dill
import pathos.multiprocessing as mp
'''http://stackoverflow.com/questions/22418816/python-pickling-and-multiprocessing'''

class Word2VecPlusNgram:

	def __init__(self, ngrams_dir, word2vec_file, timerange, binary = False):

		self.ngrams_dir = ngrams_dir
		self.word2vec_file = word2vec_file
		self.input_string = None
		self.timerange = timerange
		self.counts = [0.0 for i in self.timerange]
		self.n = None
		self.model = None
		self.vocab = None
		self.sims = None
		self.binary = binary

	def count_ngram(self, year):
		print "\tSearching in year %i" % year

		filename_base = self.ngrams_dir + str(self.n) + "-grams-"
		filename = filename_base + str(year) + ".tsv.gz"
	
		tsvfile = gzip.open(filename,'rb')
		lines = tsvfile.readlines()
    		for line in lines:
			elements = line.rstrip().split("\t")
			if elements[0] == self.input_string:
				print elements
				return [year, int(elements[2])]

		# otherwise
		return [year,0.0]

	def set_input_string(self, input_str):
		self.input_string = input_str
		self.input_word_list = self.input_string.split()
		self.n = len(self.input_word_list)

		print "Set word to %s" % self.input_string

		self.sims = [m[0] for m in self.model.most_similar(positive=self.input_string.split())] 
		# you could also put negative here, in addition to positive, to get difference vectors: see gensim word2vec docs
		
		print "Most similar words:"
		print self.sims

	def query_input_from_prompt(self):
		print "Look for words similar to..."
        	
		line = raw_input('\nprompt> ')
		self.set_input_string(line)

	def load_word2vec_model(self):

		if self.model == None:
			print "\nLoading Word2Vec model...\n"
			if self.binary:
				self.model = gensim.models.Word2Vec.load_word2vec_format(self.word2vec_file, binary = self.binary)
			else:
				self.model = gensim.models.Word2Vec.load(self.word2vec_file)
	    		self.model.init_sims(replace=True)
    			self.vocab = self.model.index2word
		else:
			print "Word2Vec model %s already loaded." % self.word2vec_file

	def search_for_ngrams(self):
		print "Searching for %i-gram %s..." % (self.n, self.input_string)

		# simple parallelization over the year-specific input files
		pool = mp.ProcessingPool(8)
		print "\tCreated ProcessingPool to search through the files..."
		c = pool.map(self.count_ngram, self.timerange)
		print c

		# getting the years back in the right order for plotting
		sorted_c = sorted(c, key = lambda tup: tup[0])
		self.counts = [k[1] for k in sorted_c]

		# plotting the ngram over time
		plots = []

		fig = plt.figure()
		p = plt.plot(self.timerange, self.counts)
		plt.xlabel("Year")
		plt.ylabel("Count")
		plots.append(p)
		plt.show()

		# searching for and plotting the 1-grams corresponding to similar words
		for w in self.sims:
			self.input_string = w
			self.input_word_list = self.input_string.split()
			self.n = len(self.input_word_list)

			print "Searching for %i-gram %s..." % (self.n, self.input_string)
			c = pool.map(self.count_ngram, self.timerange)
			print c
			sorted_c = sorted(c, key = lambda tup: tup[0])
			self.counts = [k[1] for k in sorted_c]
			p = plt.plot(self.timerange, self.counts)
			plots.append(p)


		plt.legend(plots, [self.input_string] + self.sims)
		plt.show()
def main():
	
	# w = Word2VecPlusNgram("../../PubMed/BioNLP/ngrams/pubmed/","../../PubMed/BioNLP/wikipedia-pubmed-and-PMC-w2v.bin", range(1990,2013), binary = True)
	w = Word2VecPlusNgram("../../PubMed/BioNLP/ngrams/pubmed/",\
		"../../PubMed/derived_from_neuroscience_abstracts/word2vec_model_1",\
		 range(1990,2013),\
	 	binary = False)
	w.load_word2vec_model()
	w.set_input_string("fMRI")
	w.search_for_ngrams()

	
if __name__ == '__main__':
	main()
