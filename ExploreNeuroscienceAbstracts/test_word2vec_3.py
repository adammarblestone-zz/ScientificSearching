import gensim
import numpy as np
import matplotlib.pyplot as plt
import os
import io
import nltk
import logging

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

'''Visualizes the available vocabulary at the prompt and displays similar terms.'''

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

    while True:
        print "\nPress <tab> twice to see all your autocomplete options."
        print "_______________________________________________________"
        line = raw_input('\nprompt> ')
        if line in vocab:
            print "\nSimilar words:"
            print "______________"
            sims = model.most_similar(positive=[line.split()[0]])
            all_similar = []
            for k in sims[:3]:
                all_similar.append(k[0].lower())
                second_order_sim = model.most_similar(positive=[k[0]])
                for l in second_order_sim:
                    all_similar.append(l[0].lower())
            for p in set(all_similar):
                print p
        else:
            print "Sorry: not in vocabulary!"
            
if __name__ == '__main__':
    main()
    
    
'''
Behavior:

Adam-Marblestones-MacBook-Pro:ScientificSearching adammarblestone$ python test_word2vec_3.py 

Loading Word2Vec model...


Press <tab> twice to see all your autocomplete options.
_______________________________________________________

prompt> dopamin
dopamine                                  dopamine-containing                       dopamine-related
dopamine's                                dopamine-deficient                        dopamine-releasing
dopamine(D1)                              dopamine-denervated                       dopamine-replacement
dopamine)                                 dopamine-dependent                        dopamine-replacing
dopamine).                                dopamine-depleted                         dopamine-rich
dopamine,                                 dopamine-depleting                        dopamine-sensitive
dopamine-                                 dopamine-enhancing                        dopamine-serotonin
dopamine-,                                dopamine-glutamate                        dopamine-stimulated
dopamine--hydroxylase                     dopamine-immunoreactive                   dopamine-synthesizing
dopamine-2                                dopamine-independent                      dopamine.
dopamine-D1                               dopamine-induced                          dopamine;
dopamine-D2                               dopamine-innervated                       dopaminergic
dopamine-D2S                              dopamine-intact                           dopaminergic)
dopamine-activating                       dopamine-lesioned                         dopaminergic,
dopamine-beta-hydroxylase                 dopamine-like                             dopaminergic-like
dopamine-beta-hydroxylase,                dopamine-mediated                         dopaminergic.
dopamine-beta-hydroxylase-immunoreactive  dopamine-producing                        dopaminergically
dopamine-beta-hydroxylase-positive        dopamine-receptor                         dopaminoceptive
dopamine-beta-hydroxylase.                dopamine-regulated                        dopaminomimetic

prompt> dopaminergic

Similar words:
______________
serotonergic
catecholaminergic
non-da
jcbnst
(tida)
midbrain
(nsda)
histaminergic
dopaminergic
mesostriatal
cholinergic
mesocorticolimbic
non-dopaminergic
orexinergic
nigrostriatal
mesocortical
nigral
noradrenergic
mesotelencephalic
serotoninergic
nigro-striatal
daergic
mesolimbic
(da)
(da)-containing
(daergic)
monoaminergic
'''