import sys
import bibtexparser as bp

def read_file(filename):
	with open(filename, errors='replace') as bibtex_file:
		bibtex_str = bibtex_file.read()
		bib = bp.loads(bibtex_str)
	return bib

def write_file(lib, filename):
	with open(filename, 'w') as out_file:
		out_file.write(bp.dumps(lib))

if __name__ == '__main__':
	if len(sys.argv) == 2:
		in_file = sys.argv[1]
		out_file = in_file.replace(".bib", "-out.bib")
	elif len(sys.argv) == 3:
		in_file = sys.argv[1]
		out_file = sys.argv[2]
	else:
		print("Usage: python main.py in_file [out_file]")
		sys.exit()

	bib = read_file(in_file)

	# add/remove fields depending on what you want
	strip = ['file', 'abstract', 'keyword', 'keywords', 'eprint', 'archiveprefix', 'pmid', 'link', 'issn', 'isbn', 'mendeley-groups']
	
	# replace doi field with note for JBO-style reference processing
	DO_DOI = True

	for k, v in bib.entries_dict.items():
	
		if DO_DOI:
			if 'doi' in v:
				old_value = v.pop('doi')
				new_value = "[doi:%s]" % old_value

				v['note'] = new_value

		for kk in strip:
			
			if kk in v:
				v.pop(kk)


	write_file(bib, out_file)
