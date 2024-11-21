import os
import pandas as pd
import numpy as np


def find_invalid_values_in_directory(directory):
    # Find CSV files in the specified directory
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    csv_files = [f for f in os.listdir(directory) if f.endswith(".csv")]

    # If no CSV files are found
    if not csv_files:
        print(f"No CSV files found in the directory '{directory}'.")
        return

    # Check each CSV file for infinite and NaN values
    for csv_file in csv_files:
        print(f"Checking file: {csv_file}")
        file_path = os.path.join(directory, csv_file)

        try:
            # Read the CSV file
            df = pd.read_csv(file_path)

            # Check for infinite values
            infinite_mask = df.isin([np.inf, -np.inf])

            # Check for NaN values
            nan_mask = df.isna()

            # Find positions of infinite values
            invalid_positions = []
            for row_index, row in infinite_mask.iterrows():
                for col_index, is_infinite in row.items():
                    if is_infinite:
                        invalid_positions.append((row_index, col_index, "Infinity"))

            # Find positions of NaN values
            for row_index, row in nan_mask.iterrows():
                for col_index, is_nan in row.items():
                    if is_nan:
                        invalid_positions.append((row_index, col_index, "NaN"))

            # Output the results
            if invalid_positions:
                print(f"  Found invalid values in '{csv_file}':")
                for position in invalid_positions:
                    print(f"    Row: {position[0]}, Column: {position[1]}, Type: {position[2]}")
            else:
                print(f"  No invalid values found in '{csv_file}'.")

        except Exception as e:
            print(f"  Error reading '{csv_file}': {e}")

# Execution
directory_path = "../data"
find_invalid_values_in_directory(directory_path)