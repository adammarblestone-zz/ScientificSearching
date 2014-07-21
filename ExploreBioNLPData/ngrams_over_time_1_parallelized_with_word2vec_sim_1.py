'''Uses gensim and resources downloaded from bio.nlplab.org to take an input phrase from
the user, find similar words to that phrase, and plot their evolution over time.'''

import gzip
import matplotlib.pyplot as plt
import numpy as np
import gensim
import numpy as np
import dill

from multiprocessing import Process, Pipe
from itertools import izip

def spawn(f):
    def fun(pipe,x):
        pipe.send(f(x))
        pipe.close()
    return fun

def parmap(f,X):
    pipe=[Pipe() for x in X]
    proc=[Process(target=spawn(f),args=(c,x)) for x,(p,c) in izip(X,pipe)]
    [p.start() for p in proc]
    [p.join() for p in proc]
    return [p.recv() for (p,c) in pipe]


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
		# print "\tSearching in year %i" % year

		filename_base = self.ngrams_dir + str(self.n) + "-grams-"
		filename = filename_base + str(year) + ".tsv.gz"
	
		tsvfile = gzip.open(filename,'rb')
		lines = tsvfile.readlines()
    		for line in lines:
			elements = line.rstrip().split("\t")
			if elements[0] == self.input_string:
				# print "\t\tFinished searching in year %i" % year
				return [year, int(elements[2])]

		# otherwise
		# print "\t\tFinished searching in year %i" % year
		return [year,0.0]

	def set_input_string(self, input_str):
		self.input_string = input_str
		self.input_word_list = self.input_string.split()
		self.n = len(self.input_word_list)

		print "Set input string to %s" % self.input_string

		self.sims = [m[0] for m in self.model.most_similar(positive=self.input_string.split(), topn = 15)] 
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

		original_input_string = self.input_string
		
		if self.n == 1:
			original_query = self.input_string
		else:
			# if a long phrase... we could also do a direct n-gram search with n>1 but this is for efficiency
			original_query = self.model.most_similar(positive=self.sims)[0][0]
			print "Closest single word to the query (%s) is (%s)" % (original_input_string, original_query)
			self.input_string = original_query
			self.input_word_list = self.input_string.split()
			self.n = len(self.input_word_list)

		print "Searching for 1-gram %s..." % original_query

		# simple parallelization over the year-specific input files
		c = parmap(self.count_ngram, self.timerange)

		# getting the years back in the right order for plotting
		sorted_c = sorted(c, key = lambda tup: tup[0])
		self.counts = [k[1] for k in sorted_c]

		# plotting the ngram over time
		plots = []

		fig = plt.figure()
		p, = plt.plot(self.timerange, self.counts, linewidth = 2.0)
		plt.xlabel("Year")
		plt.ylabel("Count")
		plt.title("N-Grams for Words Similar to the Query String: %s" % original_input_string)
		plots.append(p)

		# searching for and plotting the 1-grams corresponding to similar words
		for w in self.sims:
			self.input_string = w
			self.input_word_list = self.input_string.split()
			self.n = len(self.input_word_list)

			print "Searching for %i-gram %s..." % (self.n, self.input_string)
			c = parmap(self.count_ngram, self.timerange)
			sorted_c = sorted(c, key = lambda tup: tup[0])
			self.counts = [k[1] for k in sorted_c]
			p, = plt.plot(self.timerange, self.counts, linewidth = 2.0)
			plots.append(p)


		plt.legend(plots, [original_query] + self.sims, loc = 'upper left')
		plt.show()
def main():
	
	# w = Word2VecPlusNgram("../../PubMed/BioNLP/ngrams/pubmed/","../../PubMed/BioNLP/wikipedia-pubmed-and-PMC-w2v.bin", range(1990,2013), binary = True)
	# w = Word2VecPlusNgram("../../PubMed/BioNLP/ngrams/pubmed/", "../../PubMed/derived_from_neuroscience_abstracts/word2vec_model_1", range(1990,2013), binary = False)
	w = Word2VecPlusNgram("../../PubMed/BioNLP/ngrams/pubmed/", "../../PubMed/derived_from_neuroscience_abstracts/word2vec_model_1_cleaned", range(1990,2013), binary = False) # use lowercase inputs with this model
	w.load_word2vec_model()
	w.query_input_from_prompt()
	w.search_for_ngrams()

	
if __name__ == '__main__':
	main()
