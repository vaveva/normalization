#Script for finding the amounts of error types in Ylilauta and Suomi24 data
import re
n = []
r = []
e =[]
ii = []
low =[]
lower = []
up = []
en = []
isi = []
o = []
iiii = []
with open("source.txt","r") as f:
	for line in f:
		line = line.strip("\n")
		if line.endswith("n"):
			n.append(line)
		for i in range(len(line)):
			if i > 0:
				if line[i] == line[i-1]:
					r.append(line)
					break
		if line.endswith("e"):
			e.append(line)
		if line.endswith("i"):
			ii.append(line)
		if line.islower():
			low.append(line)
		if len(line) > 0 and line[0].isupper() and line[1:].islower():
			lower.append(line)
		if line.isupper():
			up.append(line)
		if line.endswith("en"):
			en.append(line)
		if line.endswith("is"):
			isi.append(line)
		if line.endswith("t"):
			o.append(line)
		if "s" in line:
			iiii.append(line)

for line in iiii:
	print(line)
print(len(iiii))