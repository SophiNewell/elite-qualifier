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
docs = []

for intent in data["intents"]:
  for pattern in intent["patterns"]:
    wrds = nltk.tokenize(pattern)
    words.extend(wrds)
    docs.append(pattern)

    if intent["tag"] not in labels:
      labels.append(intent["tag"])
