# Collaborative filtering model
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

def train_collaborative_filtering_model(user_ratings):
    # Load data and create a Surprise dataset
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(user_ratings[['userId', 'movieId', 'rating']], reader)

    # Split data into training and testing sets
    trainset, testset = train_test_split(data, test_size=0.2)

    # Initialize and train the SVD algorithm (or another collaborative filtering model)
    algo = SVD()
    algo.fit(trainset)

    return algo

def get_collaborative_filtering_recommendations(model, user_id, top_n=10):
    # Generate recommendations using the trained model
    # We can use the model to predict ratings for items not rated by the user
    # and recommend items with the highest predicted ratings.
    # Here's a simplified example using Surprise's built-in functions:

    # Create a list of movie IDs that the user has not rated
    unrated_movie_ids = [movie_id for movie_id in range(num_movies) if not user_has_rated_movie(user_id, movie_id, user_ratings)]

    # Predict ratings for unrated movies
    predictions = [model.predict(user_id, movie_id) for movie_id in unrated_movie_ids]

    # Sort predictions by predicted rating in descending order
    predictions.sort(key=lambda x: x.est, reverse=True)

    # Get the top N recommended movie IDs
    top_movie_ids = [prediction.iid for prediction in predictions[:top_n]]

    return top_movie_ids

def user_has_rated_movie(user_id, movie_id, user_ratings):
    # Helper function to check if a user has rated a specific movie
    return not user_ratings[(user_ratings['userId'] == user_id) & (user_ratings['movieId'] == movie_id)].empty
