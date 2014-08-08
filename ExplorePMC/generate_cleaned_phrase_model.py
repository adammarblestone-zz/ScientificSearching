'''Purpose: generate Word2Vec model after cleaning the phrase file derived from running the original word2phrase C code'''

import gensim
import numpy as np
import matplotlib.pyplot as plt
import os
import io
import nltk
import logging
import nltk
from nltk.corpus import stopwords

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def cleanDoc(doc):
    stopset = set(stopwords.words('english'))
    #stemmer = nltk.PorterStemmer()
    tokens = nltk.tokenize.WordPunctTokenizer().tokenize(doc)
    clean = [token.lower() for token in tokens if token.lower() not in stopset and len(token) > 2]
    #final = [stemmer.stem(word) for word in clean]
    final = [word for word in clean]
    if final != []:
        final_str = "".join([final[i] + " " for i in range(len(final)-1)]) + final[len(final) - 1]
    else:
        final_str = ""
    return final_str

def main():
    infile = "../../PubMed/NEURO-PHRASE"
    print "Setting up access to all the sentences..."
    allTheSentences = SentenceList(infile)
    print "Making Word2Vec model..."
    model = gensim.models.Word2Vec(allTheSentences)
    print "Saving Word2Vec model..."
    model.save("../../PubMed/NEURO-PHRASE-VECTOR-CLEANED-NONBINARY")

def iter_document(infile):
    for line in open(infile).readlines():
    	if len(line) > 1:
        	yield line.decode('ascii', 'ignore').strip()

class SentenceList(object):
    def __init__(self, infile):
        self.infile = infile
        
    def __iter__(self):
        for line in iter_document(self.infile):
            sentences = sentence_tokenizer.tokenize(line)
            for s in sentences:
                q = str(cleanDoc(s)).split()
                #print q
                yield q

if __name__ == '__main__':
    main()
