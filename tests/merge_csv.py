import pandas as pd


# Function to merge two CSV files based on 'date' and 'unit'
def merge_csv_files(file_path1, file_path2):
    # Load the two CSV files
    data1 = pd.read_csv(file_path1)
    data2 = pd.read_csv(file_path2)

    # Merge the two DataFrames on 'date' and 'unit'
    merged_data = pd.merge(data1, data2, on=['date', 'unit'])

    return merged_data


if __name__ == "__main__":
    # Define file paths for both CSV files
    file_path1 = '../data/test/BTC_active_address_test_data.csv'
    file_path2 = '../data/test/BTC_transactions_test_data.csv'

    # Merge the CSV files
    merged_data = merge_csv_files(file_path1, file_path2)

    # Save the merged data to a new CSV file
    merged_data.to_csv('../data/test/BTC_merged_data.csv', index=False)

    print("Merged data saved to '../data/test/BTC_merged_data.csv'")
