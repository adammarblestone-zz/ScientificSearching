import gensim
import numpy as np
import matplotlib.pyplot as plt
import os
import nltk
from nltk.corpus import stopwords
import wordcloud # https://github.com/amueller/word_cloud

def cleanDoc(doc):
    stopset = set(stopwords.words('english'))
    #stemmer = nltk.PorterStemmer()
    tokens = nltk.tokenize.WordPunctTokenizer().tokenize(doc)
    clean = [token.lower() for token in tokens if token.lower() not in stopset and len(token) > 2]
    #final = [stemmer.stem(word) for word in clean]
    final = [word for word in clean]
    final_str = "".join([f + " " for f in final])
    #print final_str
    return final_str

def main():

    dictionary = gensim.corpora.Dictionary.load("dict_abstracts_corpus_1_cleaned.dict")
    corpus = gensim.corpora.MmCorpus("abstracts_corpus_1_cleaned.mm")
    lda = gensim.models.LdaModel.load("abstracts_corpus_1_cleaned.lda")
    
    list_of_topics = lda.show_topics(100, formatted = False)
    
    for i in range(len(list_of_topics)):
        # Compute the position of the words.
        elements = wordcloud.fit_words( [(str(l[1]), l[0]) for l in list_of_topics[i]], font_path = "/Library/Fonts/Tahoma.ttf")
        # Draw the positioned words to a PNG file.
        wordcloud.draw(elements, "../topic_%i.png" % i, font_path = "/Library/Fonts/Tahoma.ttf")
        
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