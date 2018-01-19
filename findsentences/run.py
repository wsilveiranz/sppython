import spacy
import json
import os

postreqdata = json.loads(open(os.environ['req']).read())

#create the spaCy model
nlp = spacy.load('en_core_web_sm')

document = nlp(postrequest)

for token in document:
    print(token.text)

response = open(os.environ['res'], 'w')
response.write(len(doucment.tokens))
response.close()