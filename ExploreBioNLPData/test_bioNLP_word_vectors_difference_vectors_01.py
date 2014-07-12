import gensim
import numpy as np
import matplotlib.pyplot as plt
import os
import io
import nltk
import logging

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

'''Words similar to the difference of two words, at the command line.'''

def main():
    print "\nLoading Word2Vec model...\n"
    # 4 GB input file, uses about 20 GB of memory when loaded
    '''Uses the model from: http://bio.nlplab.org/'''
    model = gensim.models.Word2Vec.load_word2vec_format("../../PubMed/BioNLP/wikipedia-pubmed-and-PMC-w2v.bin", binary = True)
    model.init_sims(replace=True)
    vocab = model.index2word

    while True:
    	line1 = raw_input('\nFirst word:> ')
    	line2 = raw_input('\nSecond word:> ')

    	if line1 and line2 in vocab:
             print "\nWords similar to the difference:"
             print "______________"
	     m = model.most_similar(positive = [line1], negative = [line2])
             for k in m:
                  print k[0]        

             print "\nWords similar to `minus' the difference:"
             print "______________"
      	     m = model.most_similar(positive = [line2], negative = [line1])
             for k in m:
                  print k[0] 
             print "\n"

    	else:
        	print "\nSorry: not in vocabulary!\n"
            
if __name__ == '__main__':
    main()
    
    
'''
Behavior:

First word:> excitatory

Second word:> inhibitory

Words similar to the difference:
______________
Excitatory
EPSPs
synaptically
cEPSPs
IPSPs
corticostriatal
MNTB
EPSCs
single-shock
axo-spinous

Words similar to `minus' the difference:
______________
growth-inhibitory
inhibitive
stimulatory
suppressive
anti-proliferative
antiproliferative
synergistic
growth-inhibiting
growth-stimulatory
Growth-inhibitory



First word:> dopamine

Second word:> serotonin

Words similar to the difference:
______________
nigra-ventral
SNPR
substancia
SNpr
DAergic
nigra/ventral
pVTA
nigro-striatal
SNPC
nigral

Words similar to `minus' the difference:
______________
serotonin-norepinephrine
SSRIs
SNRIs
SNRI
serotonin-reuptake
serotonin/norepinephrine
serotonin-noradrenaline
SSRI
serotonin-selective
cyclo-oxygenase-2

'''
