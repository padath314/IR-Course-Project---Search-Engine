import re
import string
import json
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from string import punctuation

class preprocessing:
    def __init__(self):
        json_data=5

    def make(self):
        final=list()
        for i in final:
            data=i.keys()
    
    def decontracted(self,phrase):
        # specific
        phrase = re.sub(r"won\'t", "will not", phrase)
        phrase = re.sub(r"can\'t", "can not", phrase)

        # general
        phrase = re.sub(r"n\'t", " not", phrase)
        phrase = re.sub(r"\'re", " are", phrase)
        phrase = re.sub(r"\'s", " is", phrase)
        phrase = re.sub(r"\'d", " would", phrase)
        phrase = re.sub(r"\'ll", " will", phrase)
        phrase = re.sub(r"\'t", " not", phrase)
        phrase = re.sub(r"\'ve", " have", phrase)
        phrase = re.sub(r"\'m", " am", phrase)
        return phrase

    def lemmatise(self,text):
        stopword = stopwords.words('english')
        wordnet_lemmatizer = WordNetLemmatizer()
        word_tokens = nltk.word_tokenize(text)
        lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in word_tokens]
        return (" ".join(lemmatized_word))

    def remove_punct(self,text):
        return ''.join(c for c in text if c not in punctuation)

    def stemming(self,text):
        stopword = stopwords.words('english')
        snowball_stemmer = SnowballStemmer('english')
        word_tokens = nltk.word_tokenize(text)
        stemmed_word = [snowball_stemmer.stem(word) for word in word_tokens]
        return " ".join(stemmed_word)

    def remove_stopwords(self,string):
        stop_words = set(stopwords.words('english'))
        return ' '.join([w for w in nltk.word_tokenize(string) if not w in stop_words])
