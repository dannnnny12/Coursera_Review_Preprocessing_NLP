import csv
from itertools import count
import pandas as pd
from email import header
import re
import requests
import nltk
import gensim
nltk.download('punkt')
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk_stopwords = nltk.corpus.stopwords.words('english')
newStpWord = ['game','Game', ',','–','!','"','#','$','%','&',')','*','+','&',"i'm","I'm","I've","i've",'0','1','2','3','4','5','6','7','8','9','?','course.','course',"much",'more']
nltk_stopwords.extend(newStpWord)
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import gensim.corpora as corpora
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from gensim import models
from pprint import pprint
from gensim.models import TfidfModel
import pandas as pd
from nltk.probability import FreqDist
from gensim.models.ldamulticore import LdaMulticore
from gensim.models.coherencemodel import CoherenceModel
#import pyLDAvis.gensim
from string import punctuation
import json
from selenium import webdriver
import time
from nltk.stem import PorterStemmer
from gensim.models import CoherenceModel

pos = []
neg = []
sent_ls = [] #存欲分類正負情感之字串
path = 'E:\python\Sentiment&LDA\Import_Data.csv'
f = open(path, 'r',encoding="utf-8")
rows = csv.reader(f, delimiter=',')
for row in rows:
    sent_ls.append(row[2])
    #print(sent_ls)

res = [idx for idx in sent_ls if not re.findall("[^\u0000-\u05C0\u2100-\u214F]+", idx)] 

def sentiment_calc(text):
     try:
         return TextBlob(text).sentiment.polarity
     except:
         return None
test = pd.DataFrame(res)
test.columns = ["reviews"]
test['sentiment_polarity'] = test['reviews'].apply(sentiment_calc)

neg_or_pos = []

def pos_or_neg(score):
    if score>0:
        return "positive"
    elif score==0:
        return "neutral"
    else:
        return "negative"

test['pos_or_neg'] = test['sentiment_polarity'].apply(pos_or_neg)




for row in range (len(res)):
    if test.loc[row][1]>0:
        pos.append(test.loc[row][0])       #positive review array list
    elif test.loc[row][1]<0:
        neg.append(test.loc[row][0])       #negative review array list

#print(pos)

def stemming(text):
    porter = PorterStemmer()
    
    result=[]
    for word in text:
        result.append(porter.stem(word))
    return result

pos_stem = stemming(pos)
print(pos_stem)
neg_stem = stemming(neg)

newStpWord_2 = ['game','Game', ',','–','!','"','""','" "','#','$','%','&',')','.','*','+','&',"i'm","I'm","I've",       #extend sentiment stopwords fo pos and neg
"i've",'0','1','2','3','4','5','6','7','8','9','?','sorry','course.','course','good','bad','great',"'great",",good",",great","'amazing",'``',"`",'nice','java',
'like','really','well','python','easy','programming','course,',"coursera",'could',"'good","''","'",'would','many','much','also','awesome','excellent']
nltk_stopwords.extend(newStpWord_2)


pos_tokens = word_tokenize(str(pos_stem)) 
neg_tokens = word_tokenize(str(neg_stem)) 
filter_pos = [k for k in pos_tokens if not k in nltk_stopwords] 
filter_neg = [k for k in neg_tokens if not k in nltk_stopwords]

def remove_punc(content):
    train_data = []
    for word in content:
        word = re.sub(r'[{}]+'.format(punctuation),' ',word)
        train_data.append(word)
    return train_data

pos_list_without_punc = remove_punc(filter_pos)
neg_list_without_punc = remove_punc(filter_neg)

print(pos_list_without_punc)
print(len(neg_list_without_punc))



#--------------------------positive lda analysis--------------------------
plwp = [x.split(' ')for x in pos_list_without_punc]
p_dictionary = corpora.Dictionary(plwp)
p_doc_term_matrix = [p_dictionary.doc2bow(doc) for doc in plwp]
ldamodel = gensim.models.ldamodel.LdaModel(p_doc_term_matrix, num_topics=10, id2word = p_dictionary, passes=10, alpha=0.1, per_word_topics=True)
pprint(ldamodel.print_topics(10))

# Compute Perplexity
print('\nPositive Review Perplexity: ', ldamodel.log_perplexity(p_doc_term_matrix))   #Positive Review Perplexity:  -11.167232015783327
# a measure of how good the model is. lower the better.


#--------------------------negative lda analysis--------------------------
nlwp = [x.split(' ')for x in neg_list_without_punc]
n_dictionary = corpora.Dictionary(nlwp)
n_doc_term_matrix = [n_dictionary.doc2bow(doc) for doc in nlwp]
ldamodel = gensim.models.ldamodel.LdaModel(n_doc_term_matrix, num_topics=10, id2word = n_dictionary, passes=10, alpha=0.1, per_word_topics=True)
pprint(ldamodel.print_topics(10))

# Compute Perplexity
print('\nPositive Review Perplexity: ', ldamodel.log_perplexity(n_doc_term_matrix))   #Positive Review Perplexity:  -11.533226563029533
# a measure of how good the model is. lower the better.





test.to_csv('E:\python\Sentiment&LDA\TextBlob_Sentiment_Result.csv') #將結果輸出至TextBlob_Sentiment_Result.CVS 