import pandas as pd
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import nltk

tokenizer = RegexpTokenizer(r'\w+')
nltk.download('stopwords')

classifier = pipeline("sentiment-analysis")
stop_words = set(stopwords.words('english'))

def sentiment(val):
    
    res = classifier(val)
    
    return res

def read_csv(fil):
    df = pd.read_csv(fil)
    
    for idx,row in df.iterrows():
        text_val = row['Tweet']
        #print(text_val)
       
        new_text = tokenizer.tokenize(text_val)
        new_text = ' '.join(new_text)
        #invoke the sentiment funciton
        sen_ouput = sentiment(new_text)
        
        df.loc[idx,'Updated_Tweet']=new_text
        df.loc[idx,'Sentiment'] = sen_ouput[0]['label']
        df.loc[idx,'Score'] = sen_ouput[0]['score']
    return df

        
data = read_csv('tweets.csv')
data.to_csv('test.csv')
