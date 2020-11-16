import os
import json
import nltk
import string
import csv
import re
# nltk.download('stopwords')
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import collections
import gensim
from gensim import corpora
from gensim import models
from gensim.corpora import Dictionary, MmCorpus
import logging
from nltk.stem import WordNetLemmatizer
import pickle
import numpy
import pandas as pd
import numpy as np
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from tqdm import tqdm

en_stop = set(nltk.corpus.stopwords.words('english'))

def get_lemma(word):
	lemma = wn.morphy(word)
	if lemma is None:
		return word
	else:
		return lemma
	
def get_lemma2(word):
	return WordNetLemmatizer().lemmatize(word)

def nltk_stopwords():
    return set(nltk.corpus.stopwords.words('english'))

def prepare_text_for_lda(corpus):
	corpus = corpus.translate(str.maketrans('', '', string.punctuation)).lower()
	tokens = nltk.word_tokenize(corpus)
	tokens = [token for token in tokens if len(token) >= 4]
	tokens = [token for token in tokens if token not in en_stop]
	tokens = [get_lemma(token) for token in tokens]
	return tokens

def prep_corpus(docs, additional_stopwords=set(), no_below=2, no_above=0.4):
	print('Building dictionary...')
	dictionary = Dictionary(docs)
#     print(dictionary)
	stopwords = nltk_stopwords().union(additional_stopwords)
#     print(stopwords)
	stopword_ids = map(dictionary.token2id.get, stopwords)
#     print(stopword_ids)
	dictionary.filter_tokens(stopword_ids)
#     print(dictionary)
	dictionary.compactify()
#     print(dictionary)
	dictionary.filter_extremes(no_below=no_below, no_above=no_above, keep_n=None)
	print(dictionary)
	dictionary.compactify()
	
	print('Building corpus...')
	corpus = [dictionary.doc2bow(doc) for doc in docs]
	
	return dictionary, corpus

# # print(female_names)
logging.basicConfig(filename='gensim.log',
					format="%(asctime)s:%(levelname)s:%(message)s",
					level=logging.INFO)

wordnet_lemmatizer = WordNetLemmatizer()

########################################################################################################################################

df = pd.read_csv("/path_to_genderedness_csv")

print(df)
df = df.sort_values(by=['GRT_scaled'])
df["CleanTropeName"] = [tname.lower() for tname in df["Trope"].tolist()]
df = df.drop_duplicates(subset="CleanTropeName", keep="last")
print(df)

# Filtering
df["TotalMFTokens"] = df["FemaleTokens"] + df["MaleTokens"]
df["TokenRatio"] = df["TotalMFTokens"] / (df["Tokens"] + 0.0000001)
token_ratios = df["TokenRatio"].tolist()
df = df.loc[df['Tokens'] >= 1000]
df = df.loc[df['TokenRatio'] >= 0.01]

# print(np.average(token_ratios))

gender_ratios = np.sort(df["GRT_scaled"].tolist())

df_male = df.iloc[:3000]
print(df_male)
df_female= df.iloc[-3000:]
print(df_female)

df_all = pd.concat([df_male, df_female])
print(df_all)
print("compiling all text...")

all_corpus = [prepare_text_for_lda(trope_corpus) for trope_corpus in tqdm(df_all["Corpus"].tolist())]

########################################################################################################################################

def topic_model(corpus, name, topics=50, dictionary=None):
	print("evaluating", name, "model...")

	if dictionary == None:
		dictionary, corpus = prep_corpus(corpus)
		dictionary.save(name + '_tokens.dict')
		pickle.dump(corpus, open(name + "_tokens.corpus", "wb" ))

	lda_model = models.ldamodel.LdaModel(corpus=corpus,
	         id2word=dictionary,
	         num_topics=topics,
	         eval_every=10,
	         passes=topics,
	         iterations=5000,
	         random_state=numpy.random.RandomState(15))

	lda_model.save(name + str(topics) + '.model')

	return lda_model


all_lda_model = topic_model(all_corpus, "all", 50)
all_lda_model = topic_model(all_corpus, "all", 75)
all_lda_model = topic_model(all_corpus, "all", 100)
