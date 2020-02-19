from textblob import TextBlob
import nltk

#nltk.download("stopwords") ##3 downloadsa file of common stop words
# only do this once

from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd

stops = stopwords.words("english")

blob= TextBlob("Today is a beautiful day") ### we are going to use a list comprehension to generate words that are not stop words

#print([word for word in blob.words if word not in stops])
### it is going to cycle in our blob each word, and if it is not one of the stop words, it will print it out. 

#we are about to create a word cloud of top words frequently used in the text of "romeo and juliet"
# we will get a list of tuples

blob= TextBlob(Path('RomeoAndJuliet.txt').read_text())

items = blob.word_counts.items()
#this above will create every word with every count  
#print(items)

#### we want to get rid of all the tuples that have item 0 is the actual word not the number, if it is not in the stop list
### then it goes into the new list we are creating. It is iterating through each words and it searches the stop list then doing what
### i just described above. 
items_no_stops= [item for item in items if item [0] not in stops]
#print(items_no_stops)

###3 here we want to grab the top 20 words, you don't have to install the library 

from operator import itemgetter
### helps us sort this list we made above

sorted_items = sorted (items_no_stops, key=itemgetter(1),reverse=True) ### reverse is getting us descending order, true is case sensitive
### the itemgetter is getting the second object in the list, the numbers pretty much and giving us the words with the highest number
top20= sorted_items[:21] ### this is slicing because we only want the top 20 
print(top20)

##3after this we activated the virtual environment nlp_venv/scripts/activate 
#### then installed pandas pip install pandas 
### then install imageio pip install imageio

df= pd.DataFrame(top20, columns=['word', 'count'])

print(df)

import matplotlib.pyplot as plt 
from wordcloud import WordCloud
import imageio

###pip install wordcloud



df.plot.bar(x='word', y= 'count', rot=0, legend= False,
color = ["y","c","m","b", "g", "r"])

plt.gcf().tight_layout()

plt.show 



###it has to be a white background, so we use imageio because it allows us to specify 

text= Path("RomeoAndJuliet.txt"). read_text()

mask_image = imageio.imread('mask_heart.png')

wordcloud = WordCloud(colormap= 'prism', mask=mask_image, background_color='w')

wordcloud = wordcloud.generate(text)

wordcloud= wordcloud.to_file("RomeoandJulietHeart.png")

plt.imshow(wordcloud)

print("done")