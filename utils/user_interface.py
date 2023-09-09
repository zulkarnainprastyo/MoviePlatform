import sys
sys.path.append(r"C:\ProjectRecommendationSystems\MoviePlatform\utils")

import pandas as pd
from models.collaborative_filtering import train_collaborative_filtering_model, get_collaborative_filtering_recommendations
from utils.data_preprocessing import preprocess_user_input

def create_user_interface(collaborative_model):
    while True:
        print("\nMovie Recommendation System")
        print("1. Get Movie Recommendations")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = input("Enter your user ID: ")

            # Ensure user ID is valid and preprocess it if needed
            user_id = preprocess_user_input(user_id)

            if user_id is None:
                print("Invalid user ID. Please try again.")
                continue

            # Get collaborative filtering recommendations
            recommendations = get_collaborative_filtering_recommendations(collaborative_model, user_id, top_n=10)

            # Display recommendations
            print("\nTop Recommendations:")
            for i, movie in enumerate(recommendations, start=1):
                print(f"{i}. {movie}")

        elif choice == '0':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    # Initialize your collaborative filtering model here
    user_ratings = pd.read_csv('user_ratings.csv')  # Load your user ratings data
    collaborative_model = train_collaborative_filtering_model(user_ratings)

    # Start the user interface
    create_user_interface(collaborative_model)
