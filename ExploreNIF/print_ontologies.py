from bs4 import BeautifulSoup
import os

def main():
    
    named_entities = []
    
    indir = "../NIF_OWL_files"
    for filename in os.listdir(indir):
        f = open(indir + "/" + filename, 'r')
        soup = BeautifulSoup(f)
        for link in soup.find_all("rdfs:label"):
            named_entities.append(link.contents[0])
        f.close()
    
    outfile = open("../../named_entities.txt", 'w')
    for n in sorted(list(set(named_entities))):
        print str(n)
        outfile.write(n + "\n")
    outfile.close()
        
        
if __name__ == '__main__':
    main()