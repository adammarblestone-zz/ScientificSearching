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
    final_str = "".join([f[i] + " " for i in range(len(final)-1)]) + final[len(final) - 1]
    #print final_str
    return final_str

def main():
    indir = "neuroscience_abstracts"
    print "Setting up access to all the sentences..."
    allTheSentences = SentenceList(indir)
    print "Making Word2Vec model..."
    model = gensim.models.Word2Vec(allTheSentences)
    print "Saving Word2Vec model..."
    model.save("word2vec_model_1_cleaned")

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
                q = str(cleanDoc(s)).split()
                print q
                yield q

if __name__ == '__main__':
    main()