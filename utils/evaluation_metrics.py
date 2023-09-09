import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt

def calculate_mae(predictions, actual_ratings):
    """
    Calculate Mean Absolute Error (MAE) between predicted and actual ratings.

    Parameters:
    predictions (list): Predicted ratings.
    actual_ratings (list): Actual ratings.

    Returns:
    float: MAE score.
    """
    return mean_absolute_error(actual_ratings, predictions)

def calculate_rmse(predictions, actual_ratings):
    """
    Calculate Root Mean Squared Error (RMSE) between predicted and actual ratings.

    Parameters:
    predictions (list): Predicted ratings.
    actual_ratings (list): Actual ratings.

    Returns:
    float: RMSE score.
    """
    return sqrt(mean_squared_error(actual_ratings, predictions))

def calculate_precision_at_k(predictions, k):
    """
    Calculate Precision at K for a set of predictions.

    Parameters:
    predictions (list): List of predicted item IDs for each user.
    k (int): Number of top recommendations to consider.

    Returns:
    float: Precision at K score.
    """
    precision_sum = 0
    total_users = len(predictions)

    for user_predictions in predictions:
        if not user_predictions:
            continue

        user_actual_items = set(user_predictions['actual'])
        user_top_k_predictions = set(user_predictions['predicted'][:k])

        # Calculate precision for this user
        precision = len(user_actual_items.intersection(user_top_k_predictions)) / k
        precision_sum += precision

    return precision_sum / total_users

def calculate_recall_at_k(predictions, k):
    """
    Calculate Recall at K for a set of predictions.

    Parameters:
    predictions (list): List of predicted item IDs for each user.
    k (int): Number of top recommendations to consider.

    Returns:
    float: Recall at K score.
    """
    recall_sum = 0
    total_users = len(predictions)

    for user_predictions in predictions:
        if not user_predictions:
            continue

        user_actual_items = set(user_predictions['actual'])
        user_top_k_predictions = set(user_predictions['predicted'][:k])

        # Calculate recall for this user
        recall = len(user_actual_items.intersection(user_top_k_predictions)) / len(user_actual_items)
        recall_sum += recall

    return recall_sum / total_users

def calculate_rmse(predictions, actual_ratings):
    # Calculate Root Mean Squared Error (RMSE) between predicted and actual ratings
    return mean_squared_error(actual_ratings, predictions, squared=False)