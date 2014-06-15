import gensim
import numpy as np
import matplotlib.pyplot as plt
import os
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def main():
    dictionary = gensim.corpora.Dictionary.load("dict_abstracts_corpus_1_cleaned.dict")
    corpus = gensim.corpora.MmCorpus("abstracts_corpus_1_cleaned.mm")
    print corpus
    
    print "Running TF-IDF..."
    tfidf = gensim.models.TfidfModel(corpus) # generate TF-IDF model
    corpus_tfidf = tfidf[corpus] # transform the corpus into TF-IDF real-valued weights
    corpus_tfidf.save("abstracts_corpus_1_cleaned.tfidf")
    
    # LDA topic modeling
    print "Running LDA..."
    lda = gensim.models.LdaModel(corpus, id2word=dictionary)
    corpus_lda = lda[corpus]
    lda.print_topics(100)
    lda.save("abstracts_corpus_1_cleaned.lda")
    
if __name__ == '__main__':
    main()