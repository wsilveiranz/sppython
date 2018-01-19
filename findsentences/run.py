import spacy
import json
import os
from array import *

def jdefault(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__



postreqdata = json.loads(open(os.environ['req']).read())

#create the spaCy model
nlp = spacy.load('en_core_web_sm')

tokenArray = nlp(postreqdata["sentence"])

tokenList = tokenArray.tolist()

response = open(os.environ['res'], 'w')
response.write(json.dumps(tokenList, default=jdefault))
response.close()