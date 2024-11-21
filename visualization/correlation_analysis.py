import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the correlation results
results_file = "../data/eval/correlation_results.csv"
results_df = pd.read_csv(results_file)

# Map file names to readable English labels
file_name_mapping = {
    "BTC_price.csv": "Bitcoin Price",
    "exchange_reserves.csv": "Exchange Reserves",
    "exchange_inflow_CDD.csv": "Exchange Inflow CDD",
    "exchange_stablecoin_ratio.csv": "Exchange Stablecoin Ratio",
    "fund_reserves.csv": "Fund Reserves",
    "total_miner_to_exchange_coin_transfers.csv": "Total Miner-to-Exchange Transfers",
    "miner_reserves.csv": "Miner Reserves",
    "miner_position_index.csv": "Miner Position Index (MPI)",
    "hashrate.csv": "Hashrate",
    "SOPR_ratio.csv": "SOPR Ratio",
    "MVRV_ratio.csv": "MVRV Ratio",
    "net_unrealized_profit_loss.csv": "Net Unrealized Profit/Loss (NUPL)",
    "UTXO_in_profit_ratio.csv": "UTXO in Profit Ratio",
    "UTXO_in_loss_ratio.csv": "UTXO in Loss Ratio",
    "funding_fee.csv": "Funding Rate",
    "federal_funds_effective_rate.csv": "Interest Rate (Federal Funds)",
    "real_broad_dollar_index.csv": "Dollar Index (Real Broad)",
    "open_interest.csv": "Open Interest",
    "BTC_dominance.csv": "Bitcoin Dominance",
    "UTXO_age_distribution_0d_to_1d.csv": "UTXO Age Distribution (0d-1d)",
    "UTXO_age_distribution_1d_to_1w.csv": "UTXO Age Distribution (1d-1w)",
    "UTXO_age_distribution_1w_to_1m.csv": "UTXO Age Distribution (1w-1m)",
    "UTXO_age_distribution_1m_to_3m.csv": "UTXO Age Distribution (1m-3m)",
    "UTXO_age_distribution_3m_to_6m.csv": "UTXO Age Distribution (3m-6m)",
    "UTXO_age_distribution_6m_to_12m.csv": "UTXO Age Distribution (6m-12m)",
    "UTXO_age_distribution_12m_to_18m.csv": "UTXO Age Distribution (12m-18m)",
    "UTXO_age_distribution_18m_to_2y.csv": "UTXO Age Distribution (18m-2y)",
    "UTXO_age_distribution_2y_to_3y.csv": "UTXO Age Distribution (2y-3y)",
    "UTXO_age_distribution_3y_to_5y.csv": "UTXO Age Distribution (3y-5y)",
    "UTXO_age_distribution_5y_to_7y.csv": "UTXO Age Distribution (5y-7y)",
    "UTXO_age_distribution_7y_to_10y.csv": "UTXO Age Distribution (7y-10y)",
    "UTXO_age_distribution_after_10y.csv": "UTXO Age Distribution (after 10y)"
}

# Map file names to English labels
results_df["File"] = results_df["File"].map(file_name_mapping)

# Set the sort order (reverse order)
sort_order = list(file_name_mapping.values())[::-1]
results_df["File"] = pd.Categorical(results_df["File"], categories=sort_order, ordered=True)
results_df = results_df.sort_values("File")

# Visualization - 1 (Overlapping bars version)
plt.figure(figsize=(14, 8))
plt.barh(results_df["File"], results_df["Pearson Correlation"], alpha=0.7, label="Pearson Correlation")
plt.barh(results_df["File"], results_df["Spearman Correlation"], alpha=0.5, label="Spearman Correlation")
plt.xlabel("Correlation Coefficient")
plt.title("Correlation Analysis")
plt.legend()
plt.tight_layout()
plt.savefig("correlation_analysis_overlapping.png")
plt.show()

# Visualization - 2 (Separated bars version)
plt.figure(figsize=(14, 8))
y_positions = np.arange(len(results_df))
plt.barh(y_positions - 0.2, results_df["Pearson Correlation"], height=0.4, alpha=0.7, label="Pearson Correlation", color="skyblue")
plt.barh(y_positions + 0.2, results_df["Spearman Correlation"], height=0.4, alpha=0.7, label="Spearman Correlation", color="orange")
plt.yticks(y_positions, results_df["File"])
plt.xlabel("Correlation Coefficient")
plt.title("Correlation Analysis")
plt.legend()
plt.tight_layout()
plt.savefig("correlation_analysis_separated.png")
plt.show()