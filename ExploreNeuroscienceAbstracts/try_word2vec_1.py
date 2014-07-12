import gensim
import numpy as np
import matplotlib.pyplot as plt
import os
import io
import nltk
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def main():
    indir = "neuroscience_abstracts"
    print "Setting up access to all the sentences..."
    allTheSentences = SentenceList(indir)
    print "Making Word2Vec model..."
    model = gensim.models.Word2Vec(allTheSentences)
    print "Saving Word2Vec model..."
    model.save("word2vec_model_1")

def iter_documents(indir):
    print "Reading documents..."
    for filename in os.listdir(indir):
        if filename[:9] == "abstracts":
            print "Filename: %s" % filename
            for line in open(indir + "/" + filename).readlines():
                if len(line) > 1:
                    yield line.decode('ascii', 'ignore').strip()

class SentenceList(object):
    def __init__(self, indir):
        self.indir = indir
        
    def __iter__(self):
        for line in iter_documents(self.indir):
            sentences = sentence_tokenizer.tokenize(line)
            for s in sentences:
                print str(s).split()
                yield str(s).split()

if __name__ == '__main__':
    main()