import pandas as pd

def load_user_ratings(file_path):
    try:
        # Load user ratings data from the CSV file
        user_ratings = pd.read_csv(file_path)

        # You can perform additional preprocessing or validation here if needed

        return user_ratings
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# I can use this function to load user ratings data in my user interface script as follows:
user_ratings = load_user_ratings('C:\ProjectRecommendationSystems\MoviePlatform\data/user_ratings.csv')