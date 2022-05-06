#Script to write BRNN results one word per line
output = open("output","a")
with open("input") as infile:
    for line in infile:
        lines = line.split()
        for word in lines:
            output.write(word)
            output.write("\n")
        output.write("\n")
output.close()