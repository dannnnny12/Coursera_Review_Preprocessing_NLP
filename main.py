import re
import requests
import nltk
nltk.download('punkt')
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk_stopwords = nltk.corpus.stopwords.words('english')
from nltk.tokenize import word_tokenize
from textblob import TextBlob
response = requests.get("https://www.coursera.org/learn/python/reviews")
soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all("div", class_="rc-CML font-lg show-soft-breaks cml-cui")

result_list = []
arr = []
stpwd_arr = []
pos = []
neg = []
for result in results:
    #result = str(result)
    #word_tokenize(result)
    result_list.append(result.getText())

for ite in range(len(result_list)):
    arr.append(word_tokenize(result_list[ite]))
#print(arr)

for n in range(len(arr)):
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
