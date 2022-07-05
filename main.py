import re
import requests
import nltk
import gensim
nltk.download('punkt')
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk_stopwords = nltk.corpus.stopwords.words('english')
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import gensim.corpora as corpora
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from gensim import models
from pprint import pprint
result_list = []
for page in range(1,4): #hetch page1 to 3
    response = requests.get("https://www.coursera.org/learn/python/reviews?page="+str(page))

    soup = BeautifulSoup(response.text, "html.parser")

    results = soup.find_all("div", class_="rc-CML font-lg show-soft-breaks cml-cui")
    #print(results)
    

#stpwd_arr = []

    for result in results: #extraction
        #result = str(result)
        #word_tokenize(result)
        result_list.append(result.getText())
    #print(result_list)
arr = []
pos = []
neg = []
for ite in range(len(result_list)): #tokenization
    arr.append(word_tokenize(result_list[ite]))
#print(arr)

for n in range(len(arr)): #stop words removal
    for element in arr[n]:
        if element in nltk_stopwords:
            pass
        else:
            if TextBlob(element).sentiment.polarity>0.15:
                pos.append(element)
            elif TextBlob(element).sentiment.polarity<-0.15:
                neg.append(element)

            #stpwd_arr.append(element)
#print(stpwd_arr)
print("positive words:"+str(pos))
print("negative words:"+str(neg))

