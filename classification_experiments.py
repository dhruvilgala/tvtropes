import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score,cross_val_predict
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.utils import resample
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import sklearn
from sklearn.preprocessing import StandardScaler

tropes_df = pd.read_csv('tvtropes_data/tropes.csv')

tv_tropes = pd.read_csv('tvtropes_data/tv_tropes.csv')
lit_tropes = pd.read_csv('tvtropes_data/lit_tropes.csv')
film_tropes = pd.read_csv('tvtropes_data/film_tropes.csv')

#setup code
trope_dict = pd.Series(tropes_df.TropeID.values,index=tropes_df.Trope).to_dict()
lit_tropes['trope_id'] = lit_tropes['Trope'].map(trope_dict)
lit_tropes =lit_tropes.dropna(subset=['trope_id'])
tv_tropes['trope_id'] = tv_tropes['Trope'].map(trope_dict)
tv_tropes =tv_tropes.dropna(subset=['trope_id'])
film_tropes['trope_id'] = film_tropes['Trope'].map(trope_dict)  
film_tropes =film_tropes.dropna(subset=['trope_id'])

film_df = pd.DataFrame()
film_df['film_title'] = film_tropes.Title.unique()
film_df['count'] = np.arange(len(film_df))
film_df['title_id'] = 'f' + film_df['count'].astype(str)
film_df = film_df.drop('count',1)

tv_df = pd.DataFrame()
tv_df['series_title'] = tv_tropes.Title.unique()
tv_df['count'] = np.arange(len(tv_df))
tv_df['title_id'] = 'tv' + tv_df['count'].astype(str)
tv_df = tv_df.drop('count',1)

lit_df = pd.DataFrame()
lit_df['lit_title'] = lit_tropes.Title.unique()
lit_df['count'] = np.arange(len(lit_df))
lit_df['title_id'] = 'lit' + lit_df['count'].astype(str)
lit_df = lit_df.drop('count',1)

lit_dict = pd.Series(lit_df.title_id.values,lit_df.lit_title).to_dict()
lit_tropes['title_id'] = lit_tropes['Title'].map(lit_dict)

tv_dict = pd.Series(tv_df.title_id.values,tv_df.series_title).to_dict()
tv_tropes['title_id'] = tv_tropes['Title'].map(tv_dict)

film_dict = pd.Series(film_df.title_id.values,film_df.film_title).to_dict()
film_tropes['title_id'] = film_tropes['Title'].map(film_dict)

trope_examples = pd.concat([lit_tropes,tv_tropes,film_tropes])

# get IMDb data from https://www.imdb.com/interfaces/
name_df = pd.read_csv("IMDb/name_basics.tsv", error_bad_lines=False, header=0, sep='\t')
title_df = pd.read_csv("IMDb/title_basics.tsv", error_bad_lines=False, header=0, sep='\t')
crew_df = pd.read_csv("IMDb/title_crew.tsv", error_bad_lines=False, header=0, sep='\t')
principals_df = pd.read_csv("IMDb/title_principals.tsv", error_bad_lines=False, header=0, sep='\t')
ratings_df = pd.read_csv("IMDb/title_ratings.tsv", error_bad_lines=False, header=0, sep='\t')

tv_imdb_match = pd.read_csv('tvtropes_data/tv_imdb_match.csv')
tv_imdb_match = tv_imdb_match.dropna(subset=['tconst'])
tv_imdb_match['trope_id'] = tv_imdb_match['Trope'].map(trope_dict)
tv_imdb_match =tv_imdb_match.dropna(subset=['trope_id'])
tv_dict = pd.Series(tv_df.title_id.values,tv_df.series_title).to_dict()
tv_imdb_match['title_id'] = tv_imdb_match['Title'].map(tv_dict)

film_imdb_match = pd.read_csv('tvtropes_data/film_imdb_match.csv')
film_imdb_match = film_imdb_match.dropna(subset=['tconst'])
film_imdb_match['trope_id'] = film_imdb_match['Trope'].map(trope_dict)
film_imdb_match =film_imdb_match.dropna(subset=['trope_id'])
film_dict = pd.Series(film_df.title_id.values,film_df.film_title).to_dict()
film_imdb_match['title_id'] = film_imdb_match['Title'].map(film_dict)

media_imdb_match = pd.concat([film_imdb_match,tv_imdb_match])

genderedness_df = pd.read_csv('tvtropes_data/genderedness.csv')


r = genderedness_df['FemaleTokens'].sum()/(genderedness_df['FemaleTokens']+genderedness_df['MaleTokens']).sum()
scaler = StandardScaler()
genderedness_df['GRT']=genderedness_df['Gender Ratio']/r
genderedness_df['GRT_scaled'] = scaler.fit_transform(genderedness_df[['GRT']])
genderedness_df['GRT_scaled'].hist()
genderedness_df['trope_id'] = genderedness_df['Trope'].map(trope_dict)

#genderedness for genre experiment
#GRT_scaled is our genderedness

genderedness_imdb_df = pd.merge(genderedness_df[['Trope','GRT_scaled','trope_id']],film_imdb_match[['title_id','trope_id','tconst']],on='trope_id')
x = genderedness_imdb_df[['title_id','tconst','GRT_scaled']].groupby(['tconst']).mean().reset_index()
gendered_genre = pd.merge(x,title_df[['tconst','genres']])
gendered_genre[['genreP', 'genreRest']] = gendered_genre['genres'].str.split(",", n = 1, expand = True)
gendered_genre_film = gendered_genre[['GRT_scaled','genreP']].groupby('genreP').mean().reset_index()
gendered_genre_film = gendered_genre_film[gendered_genre_film['genreP'] != '\\N'].sort_values('GRT_scaled')

genderedness_imdb_df = pd.merge(genderedness_df[['Trope','GRT_scaled','trope_id']],tv_imdb_match[['title_id','trope_id','tconst']],on='trope_id')
x = genderedness_imdb_df[['title_id','tconst','GRT_scaled']].groupby(['tconst']).mean().reset_index()
gendered_genre = pd.merge(x,title_df[['tconst','genres']])
gendered_genre[['genreP', 'genreRest']] = gendered_genre['genres'].str.split(",", n = 1, expand = True)
gendered_genre_tv = gendered_genre[['GRT_scaled','genreP']].groupby('genreP').mean().reset_index()
gendered_genre_tv = gendered_genre_tv[gendered_genre_tv['genreP'] != '\\N'].sort_values('GRT_scaled')

width = 0.5
plt.barh((np.arange(21))*2.5-width/2, np.asarray(a2['GRT_scaled'].to_list()),width,tick_label=a2['genreP'],label='TV', align='edge',)
plt.barh((np.arange(21))*2.5+width/2, np.asarray(a1['GRT_scaled'].to_list()),width,tick_label=a1['genreP'],label='Movies', align='edge',)
plt.legend()

plt.xticks([-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7])

plt.ylabel('Genre',fontweight='bold')
plt.xlabel('Genderedness',fontweight='bold')
plt.tight_layout()
plt.grid(axis='x')
plt.savefig('genre_ft_bars_legend_fin')


#ratings classifier experiment
matched_ratings = pd.merge(media_imdb_match,ratings_df,on='tconst')
x = media_imdb_match.groupby('trope_id').size().reset_index(name='counts')
filter_tropes = x[x.counts > 10]['trope_id'].tolist()
y = media_imdb_match[media_imdb_match.trope_id.isin(filter_tropes)]


x = y.groupby('title_id').size().reset_index(name='counts')
filter_titles = x[x.counts > 10]['title_id'].tolist()
y = y[y.title_id.isin(filter_titles)]

y_ = y[['title_id','trope_id']]
feature_matrix = pd.get_dummies(data=y_, columns = ['trope_id']).groupby('title_id').max()
feature_matrix.columns = ('t') + feature_matrix.columns.str.lstrip('trope_id') 
matched_ratings['RatingBucket'] = pd.qcut(matched_ratings.averageRating,3,labels=['Low','Medium','High'])

X = data_df_ratings.loc[:, data_df_ratings.columns !='RatingBucket']
y = data_df_ratings['RatingBucket']
X_train, X_test,y_train,y_test = train_test_split(X,y, test_size=0.2,shuffle=True)
print(y_test.value_counts())
clf = LogisticRegression()
clf.fit(X_train,y_train)
print(sklearn.metrics.accuracy_score(y_test, clf.predict(X_test)))


#author gender classifier experiment
lit_match_gr = pd.read_csv('tvtropes_data/lit_goodreads_match.csv')
lit_match_gr['title_id'] = lit_match_gr['Title'].map(lit_dict)
lit_match_gr['trope_id'] = lit_match_gr['Trope'].map(trope_dict)
X = lit_match_gr[['title_id','trope_id']]
y = lit_match_gr[['title_id','verified_gender']]
X_ = pd.get_dummies(data=X, columns = ['trope_id']).groupby('title_id').max()
X_train, X_test,y_train,y_test = train_test_split(X,y, test_size=0.2,shuffle=True)
clf2 = LogisticRegression()
clf2.fit(X_train,y_train)
print(sklearn.metrics.accuracy_score(y_test, clf2.predict(X_test)))


