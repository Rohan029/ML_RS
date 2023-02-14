#steps Data nedo--> Data pre processing --> Feature extention --> user input--> cosine Similarity --> List of movie
import numpy as np
import pandas as pd
import difflib #user search er somoy judi movie name er spelling vhull lekhe tale o jeno searching e oshubidha na hoy
from sklearn.feature_extraction.text import TfidfVectorizer #string value  numerical kore debe also called features vectors
from sklearn.metrics.pairwise import cosine_similarity #compare korbo j kon movie ta highest similar score korche user jeta input koreche



Data collection & Pre processing

#loading the data from csv file to a pandas dataframe
#amra pandas dataframe ta k pd nicci
movies_data = pd.read_csv('/content/movies.csv')

#amra ektu dekhbo j thikk kkore convert hoche naki csv to pandas e tai 1st 5 khana tuple dekhbo
movies_data.head()

#number of rows & columns in the data frame
movies_data.shape #4803 ta row ache mane tuple ache & 24 khana column ache

#selecting the important columns for recommandation feature
selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)

#replacting the null values wit null string
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

movies_data.head

#combining all the 5 selected features
combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

print(combined_features)

#convert this text data into feature vectors
vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(combined_features)

print(feature_vectors)

Cosine Similarity 

#amra ebar similarity ta dekhbo with the help of cosine_similarity
similarity = cosine_similarity(feature_vectors)

print(similarity)

print(similarity.shape)

print(similarity.shape)

#getting the movie name from the user/ audiance
movie_name = input('Enter your Favourit Movie name :')

#creating list with all the movie names given in the dataset 

list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)
#amra ayta alada kore ekta list banachi becos user judi vhul spelling lekhe tale o jano amr code ta ay list theke kom time e nearest name ta show kroe

#finding the close match for the movie name given by the user

find_close_match = difflib.get_close_matches(movie_name,list_of_all_titles)
print(find_close_match)

#since in the above line of code printing the find_close_match e amader k amader matching ta to show korche tar sathe aro duto dekhache but amra baki duto chai na becos amader search kore movie ta amra ekbar e peye gechi
#so amra akhn ekta e close match dekhabp
close_match = find_close_match[0]
print(close_match)

#find the index of the movie with title
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)

#mane amader iron man movie the 68 no. e ache 
#getting a lis of similar movies, elumerate ta hocce list the por por ekta manner e print korte help kore
similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)

#1st of all amra each and every movie index and similarity score pacci but amader seta chai na
#amader j list ta ache seta csv file e jerom manner e sort kora chilo sei hiseb e bar bar print hocce seta amra chai na
#amra csv list ta k erom vhabe short korbo jeno similar movie gulo sobar agge thake and last er dik e dissimilar jinis gulo thake


sorting the movie on the similarity score list manner

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
print(sorted_similar_movies)

#print the name of similar movies based on the index
#below is the code for find the index of the movie with title

#index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
#print(index_of_the_movie)

print('Movies Suggested for you :\n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i,'.',title_from_index)
    i+=1


movie Recommendation system

movie_name = input('Enter your Favourit Movie name :')

list_of_all_titles = movies_data['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name,list_of_all_titles)

close_match = find_close_match[0]

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

similarity_score = list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)


print('Movies Suggested for you :\n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i,'.',title_from_index)
    i+=1
