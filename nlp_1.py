#take notes from Madeleine 

from textblob import TextBlob

""" text = 'Today is a beautiful day, Tomorrow looks like a bad weather.'

blob=TextBlob(text)

#print(blob)

#print(blob.sentences) ### creates sentences object

#print(blob.words)

#print(blob.tags) ### breaks down every word with its tag. For example : Today (NN --- noun), beautiful (JJ --- adjective)

#print (blob.noun_phrases)

print(blob.sentiment.polarity, 3)

print(round(blob.sentiment.subjectivity,3))



#for sentence in sentences: 
#    print(round(sentence.sentiment.polarity,3))
#   print(round(sentence.sentiment.subjectivity,3))

from textblob.sentiments import NaiveBayesAnalyzer

blob= TextBlob(text, analyzer= NaiveBayesAnalyzer()) ### we used the default analyzer above 

#print(blob.sentiment)  ### whichever number is higher shows its polarity 

sentences = blob.sentences

for sentence in sentences:
    print(sentence.sentiment)

##3textbob uses Google Translate 

## New topic: 

print(blob.detect_language())

spanish =blob.translate(to='es')

print(spanish)

german = blob.translate(to='de')

#print(german)

print(spanish.translate()) """

#### below we are doing spelling check 

from textblob import Word

word = Word('theyr')

print(word.spellcheck())

new_word= word.correct() ##3 here it looks at the code above and takes the highest value 

print(new_word)

sentence= TextBlob("Ths sentence has missplled wrds.")

new_sentence = sentence.correct()

print(new_sentence)