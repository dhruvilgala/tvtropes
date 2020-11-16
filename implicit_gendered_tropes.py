import pandas as pd
import numpy as np
import string
import re
# nltk.download('wordnet')
from nltk.corpus import wordnet as wn

# This file creates a CSV of tropes that are highly-gendered but do not contain any gendered tokens in their names. 
# The idea is that they may contain a large number of implicitly gendered tropes

def get_lemma(word):
	lemma = wn.morphy(word)
	if lemma is None:
		return word
	else:
		return lemma
 
def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return [m.group(0) for m in matches]

male_words_file = open('/path_to_male_lexicon', 'r')
male_words = male_words_file.read().splitlines()
male_words_file.close()

# print(male_words)

female_words_file = open('/path_to_female_lexicon', 'r')
female_words = female_words_file.read().splitlines()
female_words_file.close()

male_words = [get_lemma(tok.translate(str.maketrans('', '', string.punctuation)).lower()) for tok in male_words]
female_words = [get_lemma(tok.translate(str.maketrans('', '', string.punctuation)).lower()) for tok in female_words]

male_set = set(male_words)
female_set = set(female_words)

print(len(male_set))

mf_set = male_set | female_set

print(len(mf_set))

df = pd.read_csv("/path_to_genderedness_csv")

print(df)

df["CleanTropeName"] = [tname.lower() for tname in df["Trope"].tolist()]

df = df.drop_duplicates(subset="CleanTropeName", keep="last")

print(df)

gender_ratios = np.sort(df["GRT_scaled"].tolist())

m_threshold = -1
f_threshold = 1

df_male = df.loc[df['GRT_scaled'] <= m_threshold]
print(df_male)
df_female = df.loc[df['GRT_scaled'] >= f_threshold]
print(df_female)

df_all = df.loc[(df['GRT_scaled'] <= m_threshold) | (df['GRT_scaled'] >= f_threshold)]

print(df_all)

implicit_titles = []

trope_list = df_all['Trope'].tolist()
gender_ratio_list = df_all['GRT_scaled'].tolist()

for i in range(len(trope_list)):
	title = trope_list[i]
	gender_ratio = gender_ratio_list[i]
	title_tokens = camel_case_split(title)
	title_tokens = [get_lemma(tok.translate(str.maketrans('', '', string.punctuation)).lower()) for tok in title_tokens]
	
	contains_gender = False

	for tok in title_tokens:
		if tok in mf_set:
			contains_gender = True
			break
		for s in mf_set:
			if tok.startswith(s) or tok.endswith(s):
				contains_gender = True
				break

	if not contains_gender:
		implicit_titles.append([title, gender_ratio])

df_implicit = pd.DataFrame(implicit_titles)

print(df_implicit)
df_implicit.to_csv("/path_to_implicit_gendered_tropes_csv", index=False)

