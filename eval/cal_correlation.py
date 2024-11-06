import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
from tabulate import tabulate
import matplotlib.pyplot as plt
import seaborn as sns


# Function to load merged CSV data
def load_merged_data(file_path):
    data = pd.read_csv(file_path)
    # Rename columns to shorter names
    data.rename(columns={
        'active_address': 'act_addr',
        'transactions': 'txs',
        'price': 'price',
        'volume': 'vol'
    }, inplace=True)
    return data


# Function to calculate Pearson and Spearman correlation matrices
def calculate_correlation_matrix(data):
    # Use the renamed columns
    cols = ['act_addr', 'txs', 'price', 'vol']
    data_selected = data[cols]

    # Calculate Pearson correlation matrix
    pearson_corr_matrix = data_selected.corr(method='pearson')

    # Calculate Spearman correlation matrix
    spearman_corr_matrix = data_selected.corr(method='spearman')

    return pearson_corr_matrix, spearman_corr_matrix


if __name__ == "__main__":
    # Define the file path for the merged CSV file
    merged_file_path = '../data/test/BTC_merged_data.csv'

    # Load the merged data
    merged_data = load_merged_data(merged_file_path)

    # Calculate the correlation matrices
    pearson_corr_matrix, spearman_corr_matrix = calculate_correlation_matrix(merged_data)

    # Print the correlation matrices
    print("Pearson Correlation Matrix:")
    print(tabulate(pearson_corr_matrix, headers='keys', tablefmt='fancy_grid'))

    print("\nSpearman Correlation Matrix:")
    print(tabulate(spearman_corr_matrix, headers='keys', tablefmt='fancy_grid'))

    # Visualize the correlation matrices using heatmaps
    plt.figure(figsize=(10, 4))

    # Pearson correlation heatmap
    plt.subplot(1, 2, 1)
    sns.heatmap(pearson_corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Pearson Correlation Matrix')

    # Spearman correlation heatmap
    plt.subplot(1, 2, 2)
    sns.heatmap(spearman_corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Spearman Correlation Matrix')

    plt.tight_layout()
    plt.show()