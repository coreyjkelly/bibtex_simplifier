import sys
import bibtexparser as bp

def readFile(filename):
    with open(filename) as bibtex_file:
        bibtex_str = bibtex_file.read()
        bib = bp.loads(bibtex_str)
    return bib

def writeFile(lib, filename):
    with open(filename, 'w') as outFile:
        outFile.write(bp.dumps(lib))

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: python main.py filename.bib")
	else:
		inFile = sys.argv[1]
		bib = readFile(inFile)

		# add/remove fields depending on what you want
		strip = ['file', 'abstract', 'keyword', 'eprint', 'archiveprefix', 'pmid', 'link', 'issn', 'isbn']

		for k, v in bib.entries_dict.items():
			for kk in strip:
				if kk in v:
					v.pop(kk)


		writeFile(bib, inFile.replace(".bib", "-out.bib"))
