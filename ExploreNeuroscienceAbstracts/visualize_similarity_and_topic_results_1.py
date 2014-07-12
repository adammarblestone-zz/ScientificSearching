import gensim
import numpy as np
import matplotlib.pyplot as plt
import os

def main():

    dictionary = gensim.corpora.Dictionary.load("dict_abstracts_corpus_1.dict")
    corpus = gensim.corpora.MmCorpus("abstracts_corpus_1.mm")
    lda = gensim.models.LdaModel.load("abstracts_corpus_1.lda")
    
    print "\nTopics:\n"
    for l in lda.show_topics(100,formatted=True):
        print l
    
    index = gensim.similarities.MatrixSimilarity.load("abstracts_corpus_1.index")
    
    indir = "neuroscience_abstracts"
    
    # test a query string
    query_strings = ["It has been proposed that memories are encoded by modification of synaptic strengths through cellular mechanisms such as long-term potentiation (LTP) and long-term depression (LTD). However, the causal link between these synaptic processes and memory has been difficult to demonstrate. Here we show that fear conditioning a type of associative memory, can be inactivated and reactivated by LTD and LTP, respectively. We began by conditioning an animal to associate a foot shock with optogenetic stimulation of auditory inputs targeting the amygdala, a brain region known to be essential for fear conditioning. Subsequent optogenetic delivery of LTD conditioning to the auditory input inactivates memory of the shock. Then subsequent optogenetic delivery of LTP conditioning to the auditory input reactivates memory of the shock. Thus, we have engineered inactivation and reactivation of a memory using LTD and LTP, supporting a causal link between these synaptic processes and memory.", "Neural precursor cells (NPCs) offer a promising approach for treating demyelinating diseases. However, the cellular dynamics that underlie transplanted NPC-mediated remyelination have not been described. Using two-photon imaging of a newly developed ventral spinal cord preparation and a viral model of demyelination, we describe the motility and intercellular interactions of transplanted mouse NPCs expressing green fluorescent protein (GFP) with damaged axons expressing yellow fluorescent protein (YFP). Our findings reveal focal axonal degeneration that occurs in the ventral side of the spinal cord within 1 wk following intracranial instillation with the neurotropic JHM strain of mouse hepatitis virus (JHMV). Axonal damage precedes extensive demyelination and is characterized by swelling along the length of the axon, loss of YFP signal, and transected appearance. NPCs engrafted into spinal cords of JHMV-infected mice exhibited diminished migration velocities and increased proliferation compared with transplanted cells in noninfected mice. NPCs preferentially accumulated within areas of axonal damage, initiated direct contact with axons, and subsequently expressed the myelin proteolipid protein gene, initiating remyelination. These findings indicate that NPCs transplanted into an inflammatory demyelinating microenvironment participate directly in therapeutic outcome through the wrapping of myelin around damaged neurons.", "Face perception in both humans and monkeys is thought to depend on neurons clustered in discrete, specialized brain regions. Because primates are frequently called upon to recognize and remember new individuals, the neuronal representation of faces in the brain might be expected to change over time. The functional properties of neurons in behaving animals are typically assessed over time periods ranging from minutes to hours, which amounts to a snapshot compared to a lifespan of a neuron. It therefore remains unclear how neuronal properties observed on a given day predict that same neuron's activity months or years later. Here we show that the macaque inferotemporal cortex contains face-selective cells that show virtually no change in their patterns of visual responses over time periods as long as one year. Using chronically implanted microwire electrodes guided by functional MRI targeting, we obtained distinct profiles of selectivity for face and nonface stimuli that served as fingerprints for individual neurons in the anterior fundus (AF) face patch within the superior temporal sulcus. Longitudinal tracking over a series of daily recording sessions revealed that face-selective neurons maintain consistent visual response profiles across months-long time spans despite the influence of ongoing daily experience. We propose that neurons in the AF face patch are specialized for aspects of face perception that demand stability as opposed to plasticity."]
    
    for doc in query_strings:
        print "\nQuery string: " + doc
        
        vec_bow = dictionary.doc2bow(doc.lower().split()) # bag of words (bow) form
        vec_lda = lda[vec_bow] # convert the query to LDA space
        sims = index[vec_lda] # get the similarities for this query vector
        sims = sorted(enumerate(sims), key=lambda item: -item[1])
        print "\nDocument indices with top similarity scores:\n"
        print sims[:5]
        indices = [int(k[0]) for k in sims[:5]]
        top_docs = [get_document(indir, i) for i in indices]
        print "\nMost similar abstracts:\n"
        for d in top_docs:
            print d
            print "\n"
        
def get_document(indir, index):
    q = 0 # note the 1-indexing!
    for filename in os.listdir(indir):
        if filename[:9] == "abstracts":
            for line in open(indir + "/" + filename).readlines():
                if len(line) > 1:
                    q += 1
                    if q == index+1:
                        return line.decode('ascii', 'ignore').strip()
                        

if __name__ == '__main__':
    main()