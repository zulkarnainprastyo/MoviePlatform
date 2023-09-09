def main():
    user_ratings = load_user_ratings('C:\ProjectRecommendationSystems\MoviePlatform\data/user_ratings.csv')
    collaborative_filtering_model = train_collaborative_filtering_model(user_ratings)

    while True:
        user_id = input("Enter user ID (or 'q' to quit): ")
        if user_id.lower() == 'q':
            break
        
        recommendations = get_collaborative_filtering_recommendations(collaborative_filtering_model, user_id)
        print(f"Top Recommendations for User {user_id}:")
        for movie, score in recommendations:
            print(f"Movie ID: {movie}, Score: {score:.2f}")

if __name__ == "__main__":
    main()
