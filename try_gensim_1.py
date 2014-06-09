from gensim import corpora, models, similarities
import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    indir = "neuroscience_abstracts"
    c = abstractsCorpus(indir)
    for vector in c:
        print vector
    
    
class abstractsCorpus(object):
    def __init__(self, indir):
        self.indir = indir
    
    def __iter__(self):
        for filename in os.listdir(self.indir):
            for line in open(filename):
                yield dictionary.doc2bow(line.lower().split())
    
if __name__ == '__main__':
    main()