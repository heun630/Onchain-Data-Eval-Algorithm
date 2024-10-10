import os
import pandas as pd
import random
from datetime import datetime, timedelta
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate random test data.")
    parser.add_argument('result_count', type=int, help='Number of data entries to generate')
    parser.add_argument('coin_name', type=str, help='Coin name (e.g., BTC, ETH)')
    parser.add_argument('data_name', type=str, help='Data name (e.g., active_address, transaction_count)')
    return parser.parse_args()

def generate_random_data(result_count, coin_name, data_name):
    start_date = datetime.now() - timedelta(days=result_count)

    data = {
        "date": [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(result_count)],
        "unit": [coin_name] * result_count,
        data_name: [random.randint(900, 100000) for _ in range(result_count)]
    }

    return pd.DataFrame(data)

def save_to_csv(df, coin_name, data_name):
    directory = '../data/test'
    os.makedirs(directory, exist_ok=True)

    file_name = f"{directory}/{coin_name}_{data_name}_test_data.csv"
    df.to_csv(file_name, index=False)
    print(f"Data saved to {file_name}")

if __name__ == "__main__":
    args = parse_arguments()

    df = generate_random_data(args.result_count, args.coin_name, args.data_name)

    save_to_csv(df, args.coin_name, args.data_name)
