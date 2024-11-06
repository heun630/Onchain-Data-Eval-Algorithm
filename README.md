## On-chain and Off-chain Data Correlation Analyzer

This script acts as a tool to extract correlation coefficients between on-chain and off-chain data by generating random test data for specified coin names and data types. The generated data is saved as a CSV file in the `data/test` directory.

## Usage

You can generate random test data using the following command:

```bash
python3 make_test_results.py <result_count> <coin_name> <data_name>
```

## Argument Description

- `<result_count>`: Number of data rows to generate.
- `<coin_name>`: Name of the cryptocurrency (e.g., BTC, ETH).
- `<data_name>`: Type of data (e.g., `active_address`, `transaction_count`).

## Purpose

The primary purpose of this script is to generate synthetic test data to analyze and extract correlation coefficients between on-chain and off-chain data. By simulating various datasets, you can evaluate how different on-chain metrics correlate with off-chain factors, aiding in the development of analytical models and algorithms for cryptocurrency data evaluation.
