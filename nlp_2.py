from pathlib import Path
from textblob import TextBlob 
from textblob import Word


blob= TextBlob(Path('RomeoAndJuliet.txt').read_text())

###tokenization 
print(blob.words.count('joy'))

happy= Word('happy')

#print(happy.definitions) ##it will search through wordnet19 (database created by  Princeton)and gives definitions of words

#print(happy.synsets)

###lets create sets which like lists but wont include duplicates 

synonyms= set()

for synset in happy.synsets: 
    #lemma object represets all synonyms , lemma is a method 
    for lemma in synset.lemmas():
        synonyms.add(lemma.name) ###lemma name method adds specific synonyms from earlier 
print(synonyms)

blob= TextBlob('Today is a beautiful day')
