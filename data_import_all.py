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
newStpWord = ['game','Game', ',','–','!','"','#','$','%','&',')','*','+','&',"i'm","I'm","I've","i've",'0','1','2','3','4','5','6','7','8','9','?','course.','course']
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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
result_list=[]
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"
driver = webdriver.Chrome('E:\python\chromedriver.exe')
for page in range(1,35):
    driver.get("https://www.coursera.org/learn/machine-learning/reviews?page="+str(page))                       #machine learning @stanford
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
    #time.sleep(3)
for page in range(1,25): 
    driver.get("https://www.coursera.org/learn/introduction-programming-unity/reviews?page="+str(page))         #C_SHARP_COURSE @colorado
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,400):
    driver.get("https://www.coursera.org/learn/python/reviews?page="+str(page))                                 #python @michegan
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)

for page in range(1,400):
    driver.get("https://www.coursera.org/learn/python-data/reviews?page="+str(page))                                 #python-data @michegan
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text) 

for page in range(1,310):
    driver.get("https://www.coursera.org/learn/python-network-data/reviews?page="+str(page))                                 #python-network @michegan
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text) 

for page in range(1,125):
    driver.get("https://www.coursera.org/learn/python-databases/reviews?page="+str(page))                                 #python-data-develop @michegan
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)       

for page in range(1,67):
    driver.get("hhttps://www.coursera.org/learn/python-data-visualization/reviews?page="+str(page))                                 #python-visual @michegan
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)     

for page in range(1,144):
    driver.get("https://www.coursera.org/learn/sql-for-data-science/reviews?page="+str(page))                    #SQL for Data Science @UC Devis
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,61):
    driver.get("https://www.coursera.org/learn/java-programming/reviews?page="+str(page))                        #JAVA-programming @DUKE
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,123):
    driver.get("https://www.coursera.org/learn/duke-programming-web/reviews?page="+str(page))                        #JAVA-programming-web @DUKE
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,22):
    driver.get("https://www.coursera.org/learn/java-programming-arrays-lists-data/reviews?page="+str(page))                        #JAVA-programming-arrays-lists-data @DUKE
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)

for page in range(1,62):
    driver.get("https://www.coursera.org/learn/c-for-everyone/reviews?page="+str(page))                          #C for Everyone: Programming Fundamentals  @Saint Cruz
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,279):
    driver.get("https://www.coursera.org/learn/html/reviews?page="+str(page))                                   #HTML5 入门  @michegan
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,74):
    driver.get("https://www.coursera.org/learn/introcss/reviews?page="+str(page))                               #CSS3 入门  @michegan
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,185):
    driver.get("https://www.coursera.org/learn/r-programming/reviews?page="+str(page))                          #R programming  @johns hopkins
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,11):
    driver.get("https://www.coursera.org/learn/cloud-computing/reviews?page="+str(page))                        # Cloud Computing  @Illenois Champine
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,36):
    driver.get("https://www.coursera.org/learn/web-applications-php/reviews?page="+str(page))                   #Building Web Applications in PHP  @michegan
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,307):
    driver.get("https://www.coursera.org/learn/python-network-data/reviews?page="+str(page))                    #Python Web  @michegan
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,29):
    driver.get("https://www.coursera.org/learn/python-text-mining/reviews?page="+str(page))                    #Applied Text Mining in Python  @michegan
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,99):
    driver.get("https://www.coursera.org/learn/algorithmic-toolbox/reviews?page="+str(page))                    #Algorithmic Toolbox  @UC san diego
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,56):
    driver.get("https://www.coursera.org/learn/object-oriented-java/reviews?page="+str(page))                    #Java oriented  @UC san diego
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,18):
    driver.get("https://www.coursera.org/learn/data-structures-optimizing-performance/reviews?page="+str(page))                    #Java data-structures-optimizing-performance  @UC san diego
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,12):
    driver.get("https://www.coursera.org/learn/advanced-data-structures/reviews?page="+str(page))                    #Java advanced-data-structures  @UC san diego
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,56):
    driver.get("https://www.coursera.org/learn/cs-fundamentals-1/reviews?page="+str(page))                      #Object-Oriented Data Structures in C++   @Illenois Champine
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)  
for page in range(1,31):
    driver.get("https://www.coursera.org/learn/python-statistics-financial-analysis/reviews?page="+str(page))   #Python and Statistics for Financial Analysis   @HK tech uni
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,9):
    driver.get("https://www.coursera.org/learn/python-programming-intro/reviews?page="+str(page))                 #P Introduction to Python Programming   @Penn uni
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)    
for page in range(1,25):
    driver.get("https://www.coursera.org/learn/c-plus-plus-a/reviews?page="+str(page))                             #C++   @Saint Cruz
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)      
for page in range(1,30):
    driver.get("https://www.coursera.org/learn/machine-learning-duke/reviews?page="+str(page))                             #ML   @Duke
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text) 
for page in range(1,68):
    driver.get("https://www.coursera.org/learn/learn-to-program/reviews?page="+str(page))                             #programming fundamental   @toranto
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,10):
    driver.get("https://www.coursera.org/learn/introduction-to-computer-programming/reviews?page="+str(page))        #intro to comp programming   @London uni
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,127):
    driver.get("https://www.coursera.org/learn/iot/reviews?page="+str(page))        #iot   @Calif Erwin
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,11):
    driver.get("https://www.coursera.org/learn/introduction-to-computer-programming/reviews?page="+str(page))        #Introduction to Computer Programming   @Uni of London
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,6):
    driver.get("https://www.coursera.org/learn/how-computers-work/reviews?page="+str(page))        #how computer works   @Uni of London
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)
for page in range(1,5):
    driver.get("https://www.coursera.org/learn/more-programming-unity/reviews?page="+str(page))        #C# Programming and Unity  @Uni of Colorado
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text) 
for page in range(1,62):
    driver.get("https://www.coursera.org/learn/arduino-platform/reviews?page="+str(page))        #Arduino  @UC Irvine
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text) 
for page in range(1,10):
    driver.get("https://www.coursera.org/learn/parallel-programming-in-java/reviews?page="+str(page))        #Parallel Programming in Java @Rice Uni
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text) 
for page in range(1,11):
    driver.get("https://www.coursera.org/learn/scala-parallel-programming/reviews?page="+str(page))        #scala-parallel-programming @EPFL洛桑
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)   
for page in range(1,16):
    driver.get("https://www.coursera.org/learn/swift-programming/reviews?page="+str(page))        #swift programming @Toranto
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text)   
for page in range(1,12):
    driver.get("https://www.coursera.org/learn/interactive-python-2/reviews?page="+str(page))        #python interactive @Rice
    datas = driver.find_elements("xpath",'//*[@class="reviewText"]')
    for result in datas: #extraction
        result_list.append(result.text) 
driver.quit()
#print(result_list)
#---------------------資料讀取---------------------------

test = pd.DataFrame(result_list)
#print(len(test.columns))
test.columns = ["reviews"]
test["reviews"] = test["reviews"].str.lower()
test['review_withoutSTPWD'] = test['reviews'].apply(lambda x: ' '.join([word for word in x.split() if word not in (nltk_stopwords)]))


test.to_csv('E:\python\Sentiment&LDA\Import_Data.csv') #將結果輸出至Import_Data.CVS




