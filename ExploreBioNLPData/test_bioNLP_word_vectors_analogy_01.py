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
        print "A is to B as C is to ?"
    	line1 = raw_input('\nA:> ')
    	line2 = raw_input('\nB:> ')
    	line3 = raw_input('\nC:> ')
    	if line1 and line2 in vocab:
             print "\n? = :"
             print "______________"
	     m = model.most_similar(positive = [line2, line3], negative = [line1])
             for k in m:
                  print k[0]        
             print "\n"

    	else:
        	print "\nSorry: not in vocabulary!\n"
            
if __name__ == '__main__':
    main()
    
    
'''
Behavior:

A is to B as C is to ?

A:> ATP

B:> ATPase

C:> GTP

? = :
______________
GTPase
NTPase
ribosome-stimulated
GEF
5'-triphosphatase
Mg-ATPase
Mg2+-dependent
Mg2+-ATPase
microtubule-activated
MgATPase


A is to B as C is to ?

A:> RNAP

B:> transcription

C:> ribosome

? = :
______________
translation
cap-independent
transcriptional
trans-acting
cap-mediated
splicing
non-transcription
OsABI5
co-transcription
STRE-dependent


A is to B as C is to ?

A:> RNAP

B:> transcription

C:> DNAP 

? = :
______________
trancription
transciption
transcriptor
transcritption
promoter-specific
Promoter-dependent
HERV-Ec1
transcriptive
A2L-like
promoter-dependent


A is to B as C is to ?

A:> mitochondria

B:> animal

C:> chloroplast

? = :
______________
plant
experimental
husbandry
somacloning
Cenpcs
Arabidopsis
models4
experimentation
primate
rodent


A is to B as C is to ?

A:> CRISPR

B:> TALEN

C:> TALEN

? = :
______________
ZFN
TALENs
IL2RG-specific
GFP1/2
ZFN1
ZFNs
HOXB13-specific
hTERT6
CoDA
CompoZr


A is to B as C is to ?

A:> channelrhodopsin

B:> activation

C:> halorhodopsin

? = :
______________
hyperactivation
dephosphorylation
MAPK/MSK1
phosphorylation/activation
MAPK-dependent
cascade
MAPK-mediated
MKK4-dependent
phosphorylation
PC-PLC-driven


A is to B as C is to ?

A:> Chr2            

B:> excitation

C:> halorhodopsin

? = :
______________
Excitation
one-photon
photoexcitation
wavelength
flash-induced
long-wavelength
dual-wavelength
2c2p
wave-length
excited


A is to B as C is to ?

A:> deep-learning

B:> neural-networks

C:> ngrams

? = :
______________
unigrams
M-estimators
rSQP
MFCCs
orthonormalized
covariance-structuring
rank-1
M-Step
ROMQG
top-N


A is to B as C is to ?

A:> photosynthesis

B:> plants

C:> metabolism

? = :
______________
metabolisms
accumulation
metabolites
biosynthesis
plant
transgenic
homeostasis
[41,56,57]
trigonelline
G5G8-/-

'''
