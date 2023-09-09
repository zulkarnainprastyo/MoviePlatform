# Store configuration settings such as file paths, model hyperparameters, etc.
# File paths
MOVIE_DATA_PATH = 'C:\ProjectRecommendationSystems\MoviePlatform\data/movie_data.csv'
USER_RATINGS_PATH = 'C:\ProjectRecommendationSystems\MoviePlatform\data/user_ratings.csv'
USER_PROFILES_PATH = 'C:\ProjectRecommendationSystems\MoviePlatform\data/user_profiles.csv'

# Model hyperparameters
COLLABORATIVE_FILTERING_NUM_NEIGHBORS = 10
COLLABORATIVE_FILTERING_SIMILARITY_METRIC = 'cosine'
COLLABORATIVE_FILTERING_THRESHOLD = 4.0

CONTENT_BASED_FEATURES = ['genres', 'actors', 'directors']
CONTENT_BASED_VECTOR_SIZE = 100

# Web interface settings
WEB_SERVER_HOST = 'localhost'
WEB_SERVER_PORT = 5000

# Other configuration settings
DEBUG_MODE = True
