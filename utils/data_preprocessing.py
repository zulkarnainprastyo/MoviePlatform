import pandas as pd
import os  # Import the os module

def load_movie_data(movie_data_path):
    return pd.read_csv(movie_data_path)

def load_user_ratings(user_ratings_path):
    return pd.read_csv(user_ratings_path)

# More preprocessing functions as needed

# Load movie data, user ratings, and user profiles if applicable
movie_data = pd.read_csv('C:\ProjectRecommendationSystems\MoviePlatform\data/movie_data.csv')
user_ratings = pd.read_csv('C:\ProjectRecommendationSystems\MoviePlatform\data/user_ratings.csv')
user_profiles = pd.read_csv('C:\ProjectRecommendationSystems\MoviePlatform\data/user_profiles.csv') if 'user_profiles.csv' in os.listdir('C:\ProjectRecommendationSystems\MoviePlatform\data') else None

# Perform necessary data cleaning and preprocessing
# Merge datasets, handle missing values, encode categorical features, etc.