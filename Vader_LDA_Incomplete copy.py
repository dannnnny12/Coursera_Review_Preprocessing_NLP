import csv
from itertools import count
from matplotlib.pyplot import polar
import pandas as pd
from email import header
import re
import nltk
nltk.download('omw-1.4')
import gensim
nltk.download("vader_lexicon")
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk_stopwords = nltk.corpus.stopwords.words('english')
newStpWord = [',','–','!','"','#','$','%','&',')','*','+','&',"i'm","I'm","I've","i've",'0','1','2','3','4','5','6','7','8','9','?','course.','course',"much",'more']
nltk_stopwords.extend(newStpWord)
from nltk.tokenize import word_tokenize
import gensim.corpora as corpora
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from pprint import pprint
import pandas as pd
from gensim.models.coherencemodel import CoherenceModel
#import pyLDAvis.gensim
from string import punctuation
from selenium import webdriver
from gensim.models.ldamodel import LdaModel
from gensim.models.coherencemodel import CoherenceModel
nltk.download('wordnet')
from nltk.corpus import wordnet 
nltk.download('averaged_perceptron_tagger')
lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()
pos = []
neg = []
sent_ls = [] #存欲分類正負情感之字串
path = 'E:\python\Sentiment&LDA\Import_Data_Incomplete.csv'
f = open(path, 'r',encoding="utf-8")
rows = csv.reader(f, delimiter=',')
for row in rows:
    sent_ls.append(row[1])

res = [idx for idx in sent_ls if not re.findall("[^\u0000-\u05C0\u2100-\u214F]+", idx)] #res = 20114筆

def lemma(text):
    
    lst_text = text.split()
    lem = nltk.stem.wordnet.WordNetLemmatizer()
    lst_text = [lem.lemmatize(word,'v') for word in lst_text]
    if lst_text == text:
        lst_text = lem.lemmatize(text, 'n')
        
    text = " ".join(lst_text)
    return text

clean_data = []
for i in res:
    p = re.sub(r'[^\w\s]', '', i)
    txt_lemma = lemma(p)
    clean_data.append(txt_lemma) 

sent_analyzer = SentimentIntensityAnalyzer()

test = pd.DataFrame(clean_data)
test.columns = ["reviews"]

def format_output(output_dict):
    polarity = "neutral"
    if (output_dict['compound']>=0.05):
        polarity = "positive"
    elif(output_dict['compound']<=-0.05):
        polarity = "negative"
    return polarity

def sentiment_calc(text):
     try:
         return sent_analyzer.polarity_scores(text)
     except:
         return None
test['sentiment_polarity'] = test['reviews'].apply(sentiment_calc)
test['pos_or_neg'] = test['sentiment_polarity'].apply(format_output)

for row in range (len(clean_data)):
    if test.loc[row][2]=="positive":
        pos.append(test.loc[row][0])       #positive review array list
    elif test.loc[row][2]=="negative":
        neg.append(test.loc[row][0])       #negative review array list

newStpWord_2 = ['game','Game', "i'm","I'm","I've",       #extend sentiment stopwords fo pos and neg
"i've",'0','1','2','3','4','5','6','7','8','9','?','sorry','course.','excellent','be','one','thank','yes','no','not','do','can','this','it','to','the','course','best','good','bad','great',"'great",",good",",great","'amazing",'``',"`",'nice','java',
'like','really','well','python','easy','programming','course,',"coursera",'could',"'good","''","'",'would','many','much','also','awesome','excellent']


def senti_word_rem(text):  #remove sentiment words function
    arr = []
    for i in text:
        x = i.split()
        filter = [k for k in x if not k in newStpWord_2] 
        filter = ' '.join(filter)
        arr.append(filter)
    return arr
clean_data_without_SentiWord = senti_word_rem(clean_data)

def gen_words(texts):
    final_pos = []
    for text in texts:
        new = gensim.utils.simple_preprocess(text, deacc=True)
        final_pos.append(new)
    return (final_pos)

data_words_overall = gen_words(clean_data_without_SentiWord)
data_words_pos = gen_words(senti_word_rem(pos))
data_words_neg = gen_words(senti_word_rem(neg))
#print("ovreall rev")
print(len(clean_data_without_SentiWord))
print("pos rev:")
print(len(pos))
print("neg rev:")
print(len(neg))


#--------------------------overall lda analysis--------------------------
id2word_ov = corpora.Dictionary(data_words_overall)
corpus_ov = []
for text in data_words_overall:
    new = id2word_ov.doc2bow(text)
    corpus_ov.append(new)
lda_model_ov = gensim.models.ldamodel.LdaModel(corpus=corpus_ov,
                                           id2word=id2word_ov,
                                           num_topics=10,
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha="auto")
pprint(lda_model_ov.print_topics(10))                                           
p_doc_term_matrix_ov = [id2word_ov.doc2bow(doc) for doc in data_words_overall]

# Compute Perplexity

print('\nOverall Review Perplexity: ', lda_model_ov.log_perplexity(p_doc_term_matrix_ov))   #Overall Review Perplexity:  -7.993474071673307

#--------------end of overall-----------------------
#cm = CoherenceModel(model=lda_model_ov, corpus=corpus_ov, coherence='u_mass')
#coherence = cm.get_coherence()
#print('\nOverall Review Cohernece: ',coherence)

#if __name__=='__main__':
#    coherence_model_lda = CoherenceModel(model=lda_model_ov, texts=clean_data_without_SentiWord, dictionary=id2word_ov, coherence='c_v')
#    coherence_lda = coherence_model_lda.get_coherence()
#    print('\nCoherence Score: ', coherence_lda)
#--------------------------positive lda analysis--------------------------
id2word_pos = corpora.Dictionary(data_words_pos)
corpus_pos = []
for text in data_words_pos:
    new = id2word_pos.doc2bow(text)
    corpus_pos.append(new)
lda_model_pos = gensim.models.ldamodel.LdaModel(corpus=corpus_pos,
                                           id2word=id2word_pos,
                                           num_topics=10,
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha="auto")
pprint(lda_model_pos.print_topics(10))     
p_doc_term_matrix_pos = [id2word_pos.doc2bow(doc) for doc in data_words_pos]

# Compute Perplexity
print('\nPositive Review Perplexity: ', lda_model_pos.log_perplexity(p_doc_term_matrix_pos))   #Positive Review Perplexity:  -7.7604093115426585
# a measure of how good the model is. lower the better.


#--------------------------negative lda analysis--------------------------
id2word_neg = corpora.Dictionary(data_words_neg)
corpus_neg = []
for text in data_words_pos:
    new = id2word_neg.doc2bow(text)
    corpus_neg.append(new)
lda_model_neg = gensim.models.ldamodel.LdaModel(corpus=corpus_neg,
                                           id2word=id2word_neg,
                                           num_topics=10,
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha="auto")
pprint(lda_model_neg.print_topics(10))   
p_doc_term_matrix_neg = [id2word_neg.doc2bow(doc) for doc in data_words_neg]
# Compute Perplexity
print('\nNegative Review Perplexity: ', lda_model_neg.log_perplexity(p_doc_term_matrix_neg))   #Negative Review Perplexity:  -9.519325542067824
# a measure of how good the model is. lower the better.

test.to_csv('E:\python\Sentiment&LDA\Vader_Sentiment_Result.csv') #將結果輸出至TextBlob_Sentiment_Result.CVS