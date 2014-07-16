def main():

	'''Following instructions on http://bio.nlplab.org/, we inject the n-gram model contents into the appropriate places in the ARPA file.'''
	onegrams = open("PubMed/BioNLP/ngrams/smoothed_model/1-grams.txt.bz2")
	twograms = open("PubMed/BioNLP/ngrams/smoothed_model/2-grams.txt.bz2")
	threegrams = open("PubMed/BioNLP/ngrams/smoothed_model/3-grams.txt.bz2")
	fourgrams = open("PubMed/BioNLP/ngrams/smoothed_model/4-grams.txt.bz2")
	fivegrams = open("PubMed/BioNLP/ngrams/smoothed_model/5-grams.txt.bz2")

	with open("PubMed/BioNLP/ngrams/smoothed_model/model.arpa") as f_old, open("PubMed/BioNLP/ngrams/smoothed_model/model_populated.arpa", "w") as f_new:
    		for line in f_old:
        		if '<<contents of 1-grams.txt.bz2 here>>' in line:
				onegramtext = onegrams.read()
            			f_new.write(onegramtext)
			else:
        			f_new.write(line)

        		if '<<contents of 2-grams.txt.bz2 here>>' in line:
				twogramtext = twograms.read()
            			f_new.write(twogramtext)
			else:
        			f_new.write(line)

        		if '<<contents of 3-grams.txt.bz2 here>>' in line:
				threegramtext = threegrams.read()
            			f_new.write(threegramtext)
			else:
        			f_new.write(line)

        		if '<<contents of 4-grams.txt.bz2 here>>' in line:
				fourgramtext = fourgrams.read()
            			f_new.write(fourgramtext)
			else:
        			f_new.write(line)

        		if '<<contents of 5-grams.txt.bz2 here>>' in line:
				fivegramtext = fivegrams.read()
            			f_new.write(fivegramtext)
			else:
        			f_new.write(line)


if __name__ == '__main__':
	main()
