# Script to print ByT5 results sentence per line
outfile = open("output","a")
with open("input","r") as infile:
    for line in infile:
        words = line.split("\t")
        new_words = []
        for word in words:
            word = word.replace("\n","")
            new_words.append(word)
        if line == "\n":
            outfile.write("\n")
        else:
            outfile.write(new_words[1])
            outfile.write(" ")

outfile.close()