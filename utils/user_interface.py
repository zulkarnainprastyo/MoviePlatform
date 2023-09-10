# utils/user_interface.py

class UserInterface:
    def __init__(self, collaborative_filtering_model, content_based_model, deep_learning_model):
        self.cf_model = collaborative_filtering_model
        self.cb_model = content_based_model
        self.dl_model = deep_learning_model

    def get_user_input(self):
        print("Welcome to Movie Recommendation System!")
        while True:
            try:
                user_id = int(input("Enter your user ID: "))
                if user_id > 0:
                    return user_id
                else:
                    print("Invalid user ID. Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid user ID (a positive integer).")

    def display_recommendations(self, user_id):
        print("\nRecommendations for User", user_id)
        
        # Get recommendations from different models
        recommendation_models = {
            'Collaborative Filtering': self.cf_model,
            'Content-Based': self.cb_model,
            'Deep Learning': self.dl_model
        }
        
        print("\nChoose a recommendation model:")
        for i, model_name in enumerate(recommendation_models.keys(), start=1):
            print(f"{i}. {model_name}")
        
        while True:
            try:
                model_choice = int(input("Enter the number of your preferred model: "))
                if 1 <= model_choice <= len(recommendation_models):
                    chosen_model = list(recommendation_models.values())[model_choice - 1]
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        recommendations = chosen_model.get_recommendations(user_id)
        
        print(f"\n{chosen_model.__class__.__name__} Recommendations:")
        for i, movie in enumerate(recommendations, start=1):
            print(f"{i}. {movie}")

    def run(self):
        user_id = self.get_user_input()
        self.display_recommendations(user_id)

# Example Usage:
# if __name__ == '__main__':
#     collaborative_filtering_model = CollaborativeFilteringModel()
#     content_based_model = ContentBasedModel()
#     deep_learning_model = DeepLearningModel()
#
#     ui = UserInterface(collaborative_filtering_model, content_based_model, deep_learning_model)
#     ui.run()
