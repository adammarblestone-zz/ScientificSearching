import arpalm

def main():

	lm = arpalm.ArpaLM("../../PubMed/derived_from_BioNLP/model_populated.arpa.gz")
	lm.read()
	
	for strk in ["Chr2 induced", "electron microscopic", "stimulus driven", "C.elegans connectome", "reversible terminator"]:

		print "successors of" + strk
		print successors(strk)

if __name__ == '__main__':
	main()
