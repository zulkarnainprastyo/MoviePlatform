from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

def train_collaborative_filtering_model(user_ratings):
    try:
        # Define the rating scale (e.g., from 1 to 5)
        reader = Reader(rating_scale=(1, 5))

        # Load the user ratings data into a Surprise dataset
        data = Dataset.load_from_df(user_ratings[['userId', 'movieId', 'rating']], reader)

        # Split the data into training and testing sets
        trainset, testset = train_test_split(data, test_size=0.2)

        # Initialize and train the SVD algorithm (or another collaborative filtering model)
        algo = SVD()
        algo.fit(trainset)

        return algo
    except Exception as e:
        print(f"An error occurred during model training: {str(e)}")
        return None

def get_collaborative_filtering_recommendations(model, user_id, top_n=10):
    try:
        # Get the list of all movie IDs
        all_movie_ids = set(model.trainset.all_items())

        # Create a list of movie IDs that the user has not rated
        unrated_movie_ids = [movie_id for movie_id in all_movie_ids if not model.trainset.knows_user(user_id) or not model.trainset.knows_item(movie_id)]

        # Predict ratings for unrated movies
        predictions = [model.predict(user_id, movie_id) for movie_id in unrated_movie_ids]

        # Sort predictions by predicted rating in descending order
        predictions.sort(key=lambda x: x.est, reverse=True)

        # Get the top N recommended movie IDs
        top_movie_ids = [prediction.iid for prediction in predictions[:top_n]]

        return top_movie_ids
    except Exception as e:
        print(f"An error occurred during recommendation: {str(e)}")
        return []
