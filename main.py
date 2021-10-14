import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
from colored import fg

with open("intents.json") as file:
  data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
  for pattern in intent["patterns"]:
    wrds = nltk.tokenize(pattern)
    words.extend(wrds)
    docs_x.append(pattern)
    docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
      labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(classes))]