# addition load_data if how we can create this function to load CSV files into DataFrames
import pandas as pd

def load_data():
    try:
        # Load the movie dataset (movie_data.csv)
        movie_data = pd.read_csv('C:\ProjectRecommendationSystems\MoviePlatform\data/movie_data.csv')

        # Load the user ratings dataset (user_ratings.csv)
        user_ratings = pd.read_csv('C:\ProjectRecommendationSystems\MoviePlatform\data/user_ratings.csv')

        return movie_data, user_ratings
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None, None

# Example usage:
if __name__ == "__main__":
    movie_data, user_ratings = load_data()
    if movie_data is not None and user_ratings is not None:
        print("Data loaded successfully!")
    else:
        print("Failed to load data.")