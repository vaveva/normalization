#Script for postprocessing BRNN outputs, parts from https://github.com/mikahama/murre/blob/master/murre/generator.py
def dummy_picker(list, current_index, original_tokens):
	if len(list) == 0:
		return ""
	else:
		return list[0]

def _dechunk(l,n_best=1, best_picker=dummy_picker, orig=[]):
	c = [best_picker([y.replace(" ", "") for y in x], i, orig) for i, x in enumerate(l)]
	c = "_".join(c)
	c = c.replace("_"," ")
	c = c.replace("     ","\t")
	c = c.replace(" ","")
	c = c.replace("\t"," ")
	c = c.replace("\n"," ")
	c = c.replace("<BLANK>","\n")
	return c

with open("test.norm","r") as o:
	with open("output_skn_best","r") as f:
		with open("output_skn_processed","w") as g:
			for tokens in o:
				if isinstance(tokens, str):
					tokens = tokens.split(" ")
				for res in f:
					r = _dechunk(res, n_best=1, best_picker=dummy_picker, orig=tokens)
					g.write(r)
