#Script for chunking the inputs for BRNN, based on https://github.com/mikahama/murre/blob/master/murre/generator.py
def _chunks(l, n):
	n = max(1, n)
	return [l[i:i+n] for i in range(0, len(l), n)]

with open("skn.synth.src","r") as f:
	with open("skn.synth.src.chunks","w") as g:
		for tokens in f:
			if isinstance(tokens, str):
				tokens = tokens.split(" ")

			chunks_l = _chunks([" ".join(x) for x in tokens],3)
			chunks = [" _ ".join(x) for x in chunks_l]
			for chunk in chunks:
				g.write(chunk)
				g.write("\n")