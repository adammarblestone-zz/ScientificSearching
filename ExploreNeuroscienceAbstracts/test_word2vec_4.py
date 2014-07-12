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
    model = gensim.models.Word2Vec.load("word2vec_model_1_cleaned")
    model.init_sims(replace=True)
    
    import readline
    readline.parse_and_bind("tab: complete")

    vocab = model.index2word
    def complete(text,state):
        results = [x for x in vocab if x.startswith(text)] + [None]
        return results[state]

    readline.set_completer(complete)

    print "\nPress <tab> twice to see all your autocomplete options."
    print "_______________________________________________________"
    line1 = raw_input('\nFirst word:> ')
    line2 = raw_input('\nSecond word:> ')
    if line1 and line2 in vocab:
        print "\nWords similar to the difference:"
        print "______________"
        diff = model[line1] - model[line2]
        diff = diff
        dot_products = [np.dot(model[model.index2word[i]], diff) for i in range(len(model.index2word))]
        closest_word = model.index2word[dot_products.index(max(dot_products))]
        print closest_word
        for s in model.most_similar(closest_word):
            print s[0]
        
        print "\nWords similar to `minus' the difference:"
        print "______________"
        diff = -1*diff
        dot_products = [np.dot(model[model.index2word[i]], diff) for i in range(len(model.index2word))]
        closest_word = model.index2word[dot_products.index(max(dot_products))]
        print closest_word
        for s in model.most_similar(closest_word):
            print s[0]        
        print "\n"
    else:
        print "\nSorry: not in vocabulary!\n"
            
if __name__ == '__main__':
    main()
    
    
'''
Behavior:

Adam-Marblestones-MacBook-Pro:ScientificSearching adammarblestone$ python test_word2vec_4.py 

Loading Word2Vec model...


Press <tab> twice to see all your autocomplete options.
_______________________________________________________

First word:> dopamine

Second word:> serotonin

Words similar to the difference:
______________
6-OHDA
6-hydroxydopamine
MPTP
6-hydroxydopamine-induced
6-hydroxydopamine.
quinolinate
(6-OHDA)
6-OHDA-induced
(6-OHDA)-induced
(6-OHDA),
intrastriatal

Words similar to `minus' the difference:
______________
serotonin-norepinephrine
(SSRI),
serotonin/noradrenaline
(SSRI)
sertraline.
DA+NE
Prozac
(SSRI).
(SSRIs),
(SSRIs).
(SRIs)


Adam-Marblestones-MacBook-Pro:ScientificSearching adammarblestone$ python test_word2vec_4.py 

Loading Word2Vec model...


Press <tab> twice to see all your autocomplete options.
_______________________________________________________

First word:> optical

Second word:> electrical

Words similar to the difference:
______________
computer-aided
computer-assisted
software.
semiautomated
cryo-electron
STED
deconvolution
semi-automated
Computer-assisted
high-speed,
intravital

Words similar to `minus' the difference:
______________
electrical
Electrical
Repetitive
(NMES)
High-frequency
high-frequency
Tetanic
(rTMS).
Low-frequency
single-pulse
(GVS)


Adam-Marblestones-MacBook-Pro:ScientificSearching adammarblestone$ python test_word2vec_4.py 

Loading Word2Vec model...


Press <tab> twice to see all your autocomplete options.
_______________________________________________________

First word:> cognitive

Second word:> behavioral

Words similar to the difference:
______________
language
linguistic
comprehension
phonological
ToM
language,
semantic
visuospatial
speech
reading
metacognitive

Words similar to `minus' the difference:
______________
fear-induced
fear-conditioned
shock-induced
LiCl-induced
pre-CS
(open-field
cocaine-seeking
nocifensive
novelty-induced
defeat-induced
morphine-induced

Adam-Marblestones-MacBook-Pro:ScientificSearching adammarblestone$ python test_word2vec_4.py 

Loading Word2Vec model...


Press <tab> twice to see all your autocomplete options.
_______________________________________________________

First word:> dopaminergic

Second word:> monoaminergic

Words similar to the difference:
______________
NSC34
(pcd)
MN9D
(SH-SY5Y)
SN4741
NSC-34
NTera2
&quot;Purkinje
C17.2
B35
N2a

Words similar to `minus' the difference:
______________
neurotransmitters,
neurotransmitters
substances,
transmitters,
neurotransmitters.
neuropeptides,
monoamines,
neuropeptides.
xenobiotics
monoamine,
neurohormones
'''