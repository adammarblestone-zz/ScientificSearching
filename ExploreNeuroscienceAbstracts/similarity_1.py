import gensim
import numpy as np
import matplotlib.pyplot as plt
import os
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def main():

    dictionary = gensim.corpora.Dictionary.load("dict_abstracts_corpus_1.dict")
    corpus = gensim.corpora.MmCorpus("abstracts_corpus_1.mm")
    
    # load LDA representation
    lda = gensim.models.LdaModel.load("abstracts_corpus_1.lda")

    # similarity matrix
    print "Indexing similarities..."
    # index = gensim.similarities.Similarity(lda[corpus], corpus, num_features = len(dictionary)) # not sure if num_features should be the dict size...
    index = gensim.similarities.MatrixSimilarity(lda[corpus]) # this is very memory-intensive: see the note on the gensim tutorial...
    index.save("abstracts_corpus_1.index")
    
    # test a query string
    print "Testing query string..."
    doc = "loss of striatal dopamine neurons in parkinson's"
    print "Query string: " + doc
   
    vec_bow = dictionary.doc2bow(doc.lower().split()) # bag of words (bow) form
    vec_lda = lda[vec_bow] # convert the query to LDA space
    sims = index[vec_lda] # get the similarities for this query vector
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
   
    print "Printing query results..."
    print sims
   
    print "Printing texts corresponding to query results"
    for s in sims: # not sure if this will work
        print corpus[int(s[0])]

if __name__ == '__main__':
    main()
