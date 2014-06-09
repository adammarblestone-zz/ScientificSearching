import gensim
import numpy as np
import matplotlib.pyplot as plt
import os
import io

def main():
    indir = "neuroscience_abstracts"
    
    # Construct the corpus
    c = abstractsCorpus(indir)
    
    # Save the corpus
    print "Saving the corpus."
    gensim.corpora.MmCorpus.serialize('abstracts_corpus_1.mm', c)

def iter_documents(indir):
    print "Loading tokens into dictionary..."
    for filename in os.listdir(indir):
        if filename[:9] == "abstracts":
            print "Filename: %s" % filename
            for line in open(indir + "/" + filename).readlines():
                if len(line) > 1:
                    yield gensim.utils.tokenize(line.decode('ascii', 'ignore').strip(), lower=True)
    
class abstractsCorpus(object):
    def __init__(self, indir):
        self.indir = indir
        self.dictionary = gensim.corpora.Dictionary(iter_documents(indir))
        self.dictionary.filter_extremes(no_below = 1, keep_n = 30000) # check API docs for pruning params    
        
    def __iter__(self):
        print "Creating vector corpus from tokens..."
        for tokens in iter_documents(self.indir):
            yield self.dictionary.doc2bow(tokens)
    
if __name__ == '__main__':
    main()