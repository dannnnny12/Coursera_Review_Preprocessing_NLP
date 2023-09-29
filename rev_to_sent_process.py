import csv
import pandas as pd
import nltk
nltk.download('stopwords')
nltk_stopwords = nltk.corpus.stopwords.words('english')
sent_ls_all = [] #存欲分類正負情感之字串

path_all = 'E:\python\Sentiment&LDA\Import_Data.csv'
f = open(path_all, 'r',encoding="utf-8")
rows_all = csv.reader(f, delimiter=',')
for row in rows_all:
    sent_ls_all.append(row[1])  

token_list_all=[]
for i in range(1,len(sent_ls_all)):
    nltk_tokens = nltk.sent_tokenize(sent_ls_all[i])
    for ele in nltk_tokens:
        token_list_all.append(ele)

test = pd.DataFrame(token_list_all)
#print(len(test.columns))
test.columns = ["reviews"]
test['review_withoutSTPWD'] = test['reviews'].apply(lambda x: ' '.join([word for word in x.split() if word not in (nltk_stopwords)]))
test.to_csv('E:\python\Sentiment&LDA\Import_Data_all_final_sentenized.csv') #將結果輸出至Import_Data.CVS

sent_ls_complete = []
path_complete = 'E:\python\Sentiment&LDA\Import_Data_Complete.csv'
f = open(path_complete, 'r',encoding="utf-8")
rows_complete = csv.reader(f, delimiter=',')
for row in rows_complete:
    sent_ls_complete.append(row[1])
token_list_complete=[]
for i in range(1,len(sent_ls_complete)):
    nltk_tokens = nltk.sent_tokenize(sent_ls_complete[i])
    for ele in nltk_tokens:
        token_list_complete.append(ele)

test = pd.DataFrame(token_list_complete)
#print(len(test.columns))
test.columns = ["reviews"]
test['review_withoutSTPWD'] = test['reviews'].apply(lambda x: ' '.join([word for word in x.split() if word not in (nltk_stopwords)]))
test.to_csv('E:\python\Sentiment&LDA\Import_Data_complete_final_sentenized.csv') #將結果輸出至Import_Data.CVS