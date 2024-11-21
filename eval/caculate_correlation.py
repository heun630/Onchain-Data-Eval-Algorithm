import os
import pandas as pd
from scipy.stats import pearsonr, spearmanr

# Set the data directory
DATA_DIR = "../data"
BASE_FILE = "BTC_price.csv"

# Function to calculate correlation coefficients
def calculate_correlation(base_df, target_df, base_col, target_col):
    # Remove rows with missing or infinite values from the two columns
    valid_data = pd.concat([base_df[base_col], target_df[target_col]], axis=1).dropna()
    valid_data = valid_data[~valid_data.isin([float("inf"), float("-inf")]).any(axis=1)]

    # Pearson correlation coefficient
    pearson_corr, _ = pearsonr(valid_data[base_col], valid_data[target_col])
    # Spearman correlation coefficient
    spearman_corr, _ = spearmanr(valid_data[base_col], valid_data[target_col])
    return pearson_corr, spearman_corr

# Main logic
def main():
    # Load the base CSV file
    base_path = os.path.join(DATA_DIR, BASE_FILE)
    base_df = pd.read_csv(base_path, parse_dates=["Date"])  # Parse dates
    base_df.set_index("Date", inplace=True)

    # Set the base column (Data column)
    base_col = "Data"

    # Initialize a list to store the results
    results = []

    # Iterate through the files in the data directory
    for file_name in os.listdir(DATA_DIR):
        # Skip the base file and non-CSV files
        if file_name == BASE_FILE or not file_name.endswith(".csv"):
            continue

        file_path = os.path.join(DATA_DIR, file_name)
        target_df = pd.read_csv(file_path, parse_dates=["Date"])
        target_df.set_index("Date", inplace=True)

        # Merge the dataframes using common dates
        merged_df = pd.merge(base_df, target_df, left_index=True, right_index=True, how="inner")

        # Calculate correlation coefficients
        pearson_corr, spearman_corr = calculate_correlation(
            merged_df, merged_df, base_col + "_x", base_col + "_y"
        )

        # Store the results
        results.append({
            "File": file_name,
            "Pearson Correlation": pearson_corr,
            "Spearman Correlation": spearman_corr
        })

    # Create a DataFrame for the results and save it
    results_df = pd.DataFrame(results)
    print(results_df)
    results_df.to_csv("../data/eval/correlation_results.csv", index=False)

if __name__ == "__main__":
    main()