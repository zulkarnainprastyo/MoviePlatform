# content_based.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the movie dataset (movie_data.csv)
movie_data = pd.read_csv('C:\ProjectRecommendationSystems\MoviePlatform\data/movie_data.csv')

# Create a TF-IDF vectorizer to convert movie genres into numerical features
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
movie_genres_matrix = tfidf_vectorizer.fit_transform(movie_data['genres'])

# Calculate the cosine similarity between movies based on their genres
cosine_sim = linear_kernel(movie_genres_matrix, movie_genres_matrix)

# Create a function to recommend movies based on user preferences
def content_based_recommendations(movie_title, cosine_sim=cosine_sim, movie_data=movie_data, top_n=10):
    # Find the index of the movie with the given title
    movie_idx = movie_data.index[movie_data['title'] == movie_title].tolist()[0]

    # Calculate the cosine similarity scores for all movies
    sim_scores = list(enumerate(cosine_sim[movie_idx]))

    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top N most similar movies
    sim_scores = sim_scores[1:top_n+1]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top N similar movies
    return movie_data['title'].iloc[movie_indices]


# Content-based filtering model (if used)
# Implement our content-based filtering model here if needed
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the movie dataset (movie_data.csv)
movie_data = pd.read_csv('C:\ProjectRecommendationSystems\MoviePlatform\data/movie_data.csv')

# Create a TF-IDF vectorizer to convert movie genres into numerical features
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
movie_genres_matrix = tfidf_vectorizer.fit_transform(movie_data['genres'])

# Calculate the cosine similarity between movies based on their genres
cosine_sim = linear_kernel(movie_genres_matrix, movie_genres_matrix)

# Create a function to recommend movies based on user preferences
def content_based_recommendations(movie_title, cosine_sim=cosine_sim, movie_data=movie_data, top_n=10):
    # Find the index of the movie with the given title
    movie_idx = movie_data.index[movie_data['title'] == movie_title].tolist()[0]

    # Calculate the cosine similarity scores for all movies
    sim_scores = list(enumerate(cosine_sim[movie_idx]))

    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top N most similar movies
    sim_scores = sim_scores[1:top_n+1]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top N similar movies
    return movie_data['title'].iloc[movie_indices]

# Example usage: Get recommendations for a specific movie
recommendations = content_based_recommendations("Toy Story (1995)")
print(recommendations)
