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
