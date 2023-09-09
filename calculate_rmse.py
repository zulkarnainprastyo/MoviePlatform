# calculate_rmse
from sklearn.metrics import mean_squared_error
import numpy as np
from math import sqrt

def calculate_rmse(predictions, actual_ratings):
    """
    Calculate Root Mean Squared Error (RMSE) between predicted and actual ratings.

    Parameters:
    predictions (list or numpy array): Predicted ratings.
    actual_ratings (list or numpy array): Actual ratings.

    Returns:
    float: RMSE score.
    """
    mse = mean_squared_error(actual_ratings, predictions)
    rmse = sqrt(mse)
    return rmse

# Example usage:
if __name__ == "__main__":
    # Example predicted and actual ratings
    predicted_ratings = [4.0, 3.5, 2.0, 4.5, 5.0]
    actual_ratings = [3.5, 4.0, 1.5, 4.0, 4.5]

    rmse = calculate_rmse(predicted_ratings, actual_ratings)
    print(f"RMSE: {rmse:.2f}")
