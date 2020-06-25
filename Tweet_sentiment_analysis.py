
"""
Created on Wed Jun 24 14:42:25 2020

@author: HP
"""

# Clean text
# 1. Create a text file and get text from it
# 2. Convert all the letters into lowercase('Apple' is not hte same 'apple)
# 3. Remove punctuations

import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
import GetOldTweets3 as got
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Donald trump')\
                                           .setSince("2019-05-01")\
                                           .setUntil("2020-05-30")\
                                           .setMaxTweets(1000)
    #List of objects gets stored in tweets variable
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    #Iterating through tweets, and storing the strings as a list in a list
    text_tweets = [[tweet.text] for tweet in tweets]
    
    return text_tweets

tweets=get_tweets()

num_of_tweets=len(tweets)
text=""
for i in range(0,num_of_tweets):
    text = tweets[i][0] + " " + text

print(text)

#Converting to lowercase.
lower_case = text.lower()

#translate and maketrans are used to replace or remove characters in a string
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
#1st parameter are characters that need to be replaced
#2nd parameter specifies list of characters which replace the characters in first parameter
#3rd parameter specifies the characters that you want to delete

tokenized_words = word_tokenize(cleaned_text,"english") #Why not just juse split? When text gets very big, split takes a lot of time. This is optimised

#stop words are words that do not add any meaning to the sentence. These stop words are already included in the NLTK library



final_words=[]
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)



#NLP emotion algorithm
# 1. Check if the word in the final_words list is also present in emotions.txt
# -open the emotion file
# -loop through each line and clear it
# -Extract the word and emotion using split

# 2. If word is present -> Add the emotion to emotion_list
# 3. Finally count each emotion in the emotion list

#opening file in read-only mode

emotion_list = []
with open(r"C:\Users\HP\Documents\emotions.txt","r") as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'","").strip()
        word, emotion = clear_line.split(':') 
        
        if word in final_words:
            emotion_list.append(emotion)


w = Counter(emotion_list)
print(w)

def sentiment_analyse()

#One or more graphs can be created in figures.
#The Axes is what we think of a 'a plot'. A given figure can contain many Axes, but a given Axes object can only be in one Figure. 
fig, axl = plt.subplots()
axl.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
            