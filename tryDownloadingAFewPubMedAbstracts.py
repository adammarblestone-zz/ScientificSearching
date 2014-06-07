from Bio import Entrez
from Bio.Entrez import efetch
import re
import os

def main():
    Entrez.email = "amarbles@media.mit.edu"
    
    PMIDs = [s.strip() for s in open("pubmed_result_for_search_quote_neuroscience_unquote.txt").readlines()]
    
    IDsIHaveAlready = touchopen("IDs_I_have_already.txt", "w+")
    
    if IDsIHaveAlready.readlines():
        LastID = IDsIHaveAlready.readlines()[-1].strip()
        index = PMIDs.index(LastID)
    else:
        index = 0
    
    f = open("neuroscience_abstracts/abstracts_" + str(index/1000) + ".txt", 'w')
    for i in range(len(PMIDs[index:])):
        if i % 1000 == 0:
            f.close()
            f = open("neuroscience_abstracts/abstracts_" + str(i/1000) + ".txt", 'w')    
        pmid = PMIDs[i]
        abstract = fetch_abstract(pmid).decode('ascii', 'ignore').strip()
        print abstract
        print "\n"
        f.write(abstract)
        f.write("\n")
        IDsIHaveAlready.write(pmid + "\n")
            
def touchopen(filename, *args, **kwargs):
    open(filename, "a").close() # "touch" file
    return open(filename, *args, **kwargs)            

# From: http://stackoverflow.com/questions/17409107/obtaining-data-from-pubmed-using-python
def print_abstract(pmid):
    handle = efetch(db='pubmed', id=pmid, retmode='text', rettype='abstract')
    print handle.read()
    
def fetch_abstract(pmid):
    handle = efetch(db='pubmed', id=pmid, retmode='xml')
    xml_data = handle.read()
    r = re.compile('<AbstractText>(.*?)</AbstractText>')
    m = r.search(xml_data)
    if m:
        abstract = m.group(1)
        return abstract
    else:
        return ""

if __name__ == '__main__':
    main()