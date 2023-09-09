import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the movie dataset (movie_data.csv) and user ratings dataset (user_ratings.csv)
movie_data = pd.read_csv('C:\ProjectRecommendationSystems\MoviePlatform\data/movie_data.csv')
user_ratings = pd.read_csv('C:\ProjectRecommendationSystems\MoviePlatform\data/user_ratings.csv')

# Preprocess the data
user_encoder = LabelEncoder()
movie_encoder = LabelEncoder()

user_ids = user_encoder.fit_transform(user_ratings['userId'])
movie_ids = movie_encoder.fit_transform(user_ratings['movieId'])
ratings = user_ratings['rating'].values

num_users = len(user_encoder.classes_)
num_movies = len(movie_encoder.classes_)

# Split the data into training and testing sets
X_train_user, X_test_user, X_train_movie, X_test_movie, y_train, y_test = train_test_split(
    user_ids, movie_ids, user_ids, test_size=0.2, random_state=42
)

# Define the embedding size for users and movies
embedding_size = 32

# Create the neural collaborative filtering model (NeuMF)
user_input = keras.layers.Input(shape=(1,))
movie_input = keras.layers.Input(shape=(1,))

user_embedding_mlp = keras.layers.Embedding(
    num_users, embedding_size, input_length=1, name="user_embedding_mlp"
)(user_input)
movie_embedding_mlp = keras.layers.Embedding(
    num_movies, embedding_size, input_length=1, name="movie_embedding_mlp"
)(movie_input)

user_embedding_mf = keras.layers.Embedding(
    num_users, embedding_size, input_length=1, name="user_embedding_mf"
)(user_input)
movie_embedding_mf = keras.layers.Embedding(
    num_movies, embedding_size, input_length=1, name="movie_embedding_mf"
)(movie_input)

mlp_vector = keras.layers.concatenate([user_embedding_mlp, movie_embedding_mlp])
mf_vector = keras.layers.multiply([user_embedding_mf, movie_embedding_mf])

mlp_vector = keras.layers.Flatten()(mlp_vector)
mf_vector = keras.layers.Flatten()(mf_vector)

concat_vector = keras.layers.concatenate([mlp_vector, mf_vector])
output = keras.layers.Dense(1, activation="relu")(concat_vector)

model = keras.models.Model(inputs=[user_input, movie_input], outputs=output)
model.compile(optimizer="adam", loss="mean_squared_error")

# Train the model
model.fit(
    x=[X_train_user, X_train_movie],  # Use the correct variables
    y=y_train,
    batch_size=64,
    epochs=10,
    validation_data=([X_test_user, X_test_movie], y_test),  # Use the correct variables
)

# Make recommendations using the trained model
user_id = 1  # Replace with the desired user ID
user_indices = np.full(num_movies, user_id)

movie_scores = model.predict([user_indices, np.arange(num_movies)])
top_movie_indices = np.argsort(movie_scores.flatten())[::-1]

# Get the top N recommended movies
top_n = 10
top_movie_ids = movie_encoder.inverse_transform(top_movie_indices[:top_n])

# Print the top recommended movies
recommended_movies = movie_data[movie_data['movieId'].isin(top_movie_ids)]['title']
print(recommended_movies)
