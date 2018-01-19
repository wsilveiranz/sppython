import spacy
import json
import os

def jdefault(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__



postreqdata = json.loads(open(os.environ['req']).read())

#create the spaCy model
nlp = spacy.load('en_core_web_sm')

tokenList = nlp(postreqdata["sentence"])

for token in tokenList:
    print(token.text)

response = open(os.environ['res'], 'w')
response.write(json.dumps(tokenList, default=jdefault))
response.close()