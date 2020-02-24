### pip install spacy 
### py -m spacy download en

import spacy 

#nlp= spacy.load ('en')

nlp= spacy.load('en_core_web_sm')

document = nlp('In 1994, Tim Bernes-Lee founded the World Wide' +
'Web Consortium (W3C), devoted to developing web technologies')

for entity in document.ents: 
    print(entity.text, ":", entity.label_)

### after pip install of spacy 

### do the py install above 

from pathlib import Path

document1= nlp(Path('RomeoAndJuliet.txt').read_text())
document2= nlp(Path('EdwardTheSecond.txt').read_text())

###helps us figure out similar words

print(document1.similarity(document2))