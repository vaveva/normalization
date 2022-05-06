#Script for processing the SFF corpus data
import json
import re
from sklearn.model_selection import train_test_split
import pandas as pd

file = open("skn_simple_corpus.json")

data = json.load(file)
training = open('training.txt', 'a')
testing = open('test.txt', 'a')

s = pd.Series(data)
train, test = [i.to_dict() for i in train_test_split(s, test_size = 0.2, random_state=42)]

for i in test:
    for index,word in enumerate(data[i]['src']):
        try:
            testing.write(word + "\t" + data[i]['tgt'][index] +"\n")
        except TypeError:
            pass
    testing.write("\n")

for i in train:
    for index,word in enumerate(data[i]['src']):
        try:
            training.write(word + "\t" + data[i]['tgt'][index] +"\n")
        except TypeError:
            pass
    training.write("\n")