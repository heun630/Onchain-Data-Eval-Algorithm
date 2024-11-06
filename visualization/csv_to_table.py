import pandas as pd
from tabulate import tabulate
import argparse
import os

def load_active_addresses_data(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist.")
        return None
    data = pd.read_csv(file_path)
    return data

def display_table(data):
    data.index = data.index + 1
    print(tabulate(data, headers='keys', tablefmt='pretty'))

def parse_arguments():
    parser = argparse.ArgumentParser(description="Load and visualize CSV data.")
    parser.add_argument('csv_name', type=str, help='CSV file name without extension')
    parser.add_argument('--test', action='store_true', help='Indicate if the file is in the test directory')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    if args.test:
        file_path = f'./data/test/{args.csv_name}.csv'
    else:
        file_path = f'./data/{args.csv_name}.csv'

    active_addresses_data = load_active_addresses_data(file_path)

    if active_addresses_data is not None:
        display_table(active_addresses_data)
