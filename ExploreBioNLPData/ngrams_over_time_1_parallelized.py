import gzip
import matplotlib.pyplot as plt
import numpy as np


input_string = "fMRI"
timerange = range(1990,2014)
counts = [0.0 for i in timerange]
input_word_list = input_string.split()
n = len(input_word_list)

def count_ngram(year):
	print "Searching in year %i ..." % year

	filename_base = "../../PubMed/BioNLP/ngrams/pubmed/" + str(n) + "-grams-"
	filename = filename_base + str(year) + ".tsv.gz"
	
	tsvfile = gzip.open(filename,'rb')
	lines = tsvfile.readlines()
    	for line in lines:
		elements = line.rstrip().split("\t")
		if elements[0] == input_string:
			return [year, int(elements[2])]

	# otherwise
	return [year,0.0]
	
def main():
	
	# simple parallelization over the year-specific input files
	from multiprocessing import Pool
	pool = Pool(processes = 6)
	c = pool.map(count_ngram, timerange)
	print c
	sorted_c = sorted(c, key = lambda tup: tup[0])
	counts = [k[1] for k in sorted_c]
	
	fig = plt.figure()
	plt.plot(timerange, counts)
	plt.title(input_string)
	plt.xlabel("Year")
	plt.ylabel("Count")
	plt.show()
	

if __name__ == '__main__':
	main()
