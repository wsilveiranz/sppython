import spacy
import json
import os
import numpy

def jdefault(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__



postreqdata = json.loads(open(os.environ['req']).read())

#create the spaCy model
nlp = spacy.load('en_core_web_sm')

docs = nlp(postreqdata["sentence"])

tokenList = docs.to_array()

response = open(os.environ['res'], 'w')
response.write(json.dumps(tokenList, default=jdefault))
response.close()