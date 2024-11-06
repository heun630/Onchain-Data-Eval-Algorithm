import pandas as pd
import numpy as np


# Function to calculate the importance score for 'active_address'
def evaluate_active_address_importance(data):
    # 1. Base weight for active_address (can be adjusted)
    base_weight = 0.5

    # 2. Volatility score: Calculating the standard deviation of the active_address data
    volatility_score = np.std(data['active_address'])

    # Normalizing volatility score (optional, can adjust the scale)
    normalized_volatility_score = volatility_score / np.max(data['active_address'])

    # 3. Correlation score: Placeholder for correlation with other metrics (if available)
    # Example: If you have other metrics like 'transaction_count', you can calculate correlation
    # Here we'll assume a dummy value for illustration
    correlation_score = 0.3  # This should be calculated based on real data

    # 4. Final importance score calculation
    final_score = (base_weight + normalized_volatility_score + correlation_score) / 3

    return final_score


if __name__ == "__main__":
    # Example: Load data from CSV
    file_path = './data/test/BTC_active_address_test_data.csv'
    data = pd.read_csv(file_path)

    # Evaluate the importance of the 'active_address' metric
    importance_score = evaluate_active_address_importance(data)

    # Output the importance score
    print(f"Importance Score for 'active_address': {importance_score}")
