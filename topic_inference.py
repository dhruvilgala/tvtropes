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
# nltk.download('wordnet')
from nltk.corpus import wordnet as wn
import operator

df = pd.read_csv("/path_to_genderedness_csv")

# Filter the tropes to only contain tropes with more than 1k tokens, where 1% are gendered
df["TotalMFTokens"] = df["FemaleTokens"] + df["MaleTokens"]
df["TokenRatio"] = df["TotalMFTokens"] / (df["Tokens"] + 0.0000001)
token_ratios = df["TokenRatio"].tolist()
df = df.loc[df['Tokens'] >= 1000]
df = df.loc[df['TokenRatio'] >= 0.01]

m_threshold = 0
f_threshold = 0

df = df.sort_values(by=['GRT_scaled'])
print(df)

df["CleanTropeName"] = [tname.lower() for tname in df["Trope"].tolist()]

df = df.drop_duplicates(subset="CleanTropeName", keep="last")

# take the top n most gendered tropes for each gender
balance_count = 3000
print(df)
df_male = df.iloc[:balance_count]
print(df_male)
df_female= df.iloc[-balance_count:]
print(df_female)

# df_all = df.loc[(df['GRT_scaled'] <= m_threshold) | (df['GRT_scaled'] >= f_threshold)]
df_all = pd.concat([df_male, df_female])

print(df_all)

num_topics_vals = [75]

for num_topics in num_topics_vals:
	# print(male_corpus[:5])
	# all_corpus = [prepare_text_for_lda(trope_corpus) for trope_corpus in df_all["Corpus"].tolist()]

	trope_corpus = df_all["Trope"].tolist()
	genderedness_corpus = df_all["GRT_scaled"].tolist()

	# for i in range(len(trope_corpus)):
	# 	print(trope_corpus[i], genderedness_corpus[i])

	dictionary = Dictionary.load('all_tokens.dict')
	corpus = pickle.load(open("all_tokens.corpus", "rb"))
	model = models.ldamodel.LdaModel.load('all'+str(num_topics)+'.model')

	doc_scores = model[corpus]

	male_topics = {}
	fem_topics = {}

	# male_num_topics = []
	# female_num_topics = []

	for i in range(num_topics):
		male_topics[i] = 0
		fem_topics[i] = 0

	# get_topic_terms(topicid, topn=10)

	for i in range(len(genderedness_corpus)):
		doc_topics = sorted(doc_scores[i], key = lambda x: x[1])
		# print(len(doc_topics))

		# if genderedness_corpus[i] <= m_threshold:
		# 	male_num_topics.append(len(doc_topics))
		# else:
		# 	female_num_topics.append(len(doc_topics))

		# update male/female topic counts for topics the trope is assigned
		for topic in doc_topics:
			topic_num = topic[0]
			if genderedness_corpus[i] <= m_threshold:
				male_topics[topic_num] += 1
			else:
				fem_topics[topic_num] += 1

	# print(np.mean(np.array(male_num_topics)))
	# print(np.mean(np.array(female_num_topics)))

	with open(str(num_topics)+'topic_inference.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(["Topic", "Male Tropes", "Female Tropes", "Terms"])
		for i in range(num_topics):
			term_list = [t[0] for t in model.show_topic(i, topn=15)]
			writer.writerow([i+1, male_topics[i], fem_topics[i], " ".join(term_list)])

