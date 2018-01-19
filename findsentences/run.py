import spacy
import json
import os


postreqdata = json.loads(open(os.environ['req']).read())

#create the spaCy model
nlp = spacy.load('en_core_web_sm')

tokenList = nlp(postreqdata["sentence"])

for token in tokenList:
    print(token.text)

response = open(os.environ['res'], 'w')
response.write(json.dumps(c,default=lambda,o: o)
response.close()