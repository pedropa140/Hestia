import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.cross_decomposition import CCA


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cross_decomposition import CCA

# Read the DataFrame and drop unnecessary columns
df = pd.read_csv('./full_combined_quarterly_reports.csv')
df.dropna(inplace=True)
df = df[['market_cap_category', 'indicator', 'book_value','book_to_share_value','earnings_per_share','debt_ratio','current_ratio','dividend_yield_ratio']]
grouped = df.groupby('market_cap_category')

# Perform CCA and plot heatmap for each market cap category
for name, group in grouped:
    Y = group[['indicator']]
    X = group[['book_value','book_to_share_value','earnings_per_share','debt_ratio','current_ratio','dividend_yield_ratio']]

    # Perform CCA
    cca = CCA(n_components=1)
    cca.fit(X, Y)
    X_c, Y_c = cca.transform(X, Y)

    # Plot and save heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(cca.x_weights_, cmap='coolwarm', annot=True, fmt=".2f", annot_kws={"size": 10},yticklabels=X.columns)
    plt.title(f'CCA Weights Heatmap for {name} Market Cap Category')
    plt.xlabel("Variables in Set X")
    plt.ylabel("Variables in Set Y")
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'./heatmaps/market_cap/{name}-cca_weights_heatmap.png')
    plt.close()

df = pd.read_csv('./full_combined_quarterly_reports.csv')
df.dropna(inplace=True)
df = df[['sic_code', 'indicator', 'book_value','book_to_share_value','earnings_per_share','debt_ratio','current_ratio','dividend_yield_ratio']]
grouped2 = df.groupby('sic_code')
for name, group in grouped2:
    Y = group[['indicator']]
    X = group[['book_value','book_to_share_value','earnings_per_share','debt_ratio','current_ratio','dividend_yield_ratio']]
    name = name.strip().replace("/","")
    # Perform CCA
    cca = CCA(n_components=1)
    cca.fit(X, Y)
    X_c, Y_c = cca.transform(X, Y)

    # Plot and save heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(cca.x_weights_, cmap='coolwarm', annot=True, fmt=".2f", annot_kws={"size": 10},yticklabels=X.columns)
    plt.title(f'CCA Weights Heatmap for {name} Market Cap Category')
    plt.xlabel("Variables in Set X")
    plt.ylabel("Variables in Set Y")
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'./heatmaps/sic_code/{name}-cca_weights_heatmap.png')
    plt.close()


# df = pd.read_csv('./full_combined_quarterly_reports.csv')
# df.dropna(inplace = True)
# df = df.drop(['company_name', 'ticker', 'start_date', 'end_date','market_cap','sic_code','start_open','start_close','start_high','end_open','end_close','end_high','price_movement_percent'], axis=1)
# df = df[['market_cap_category','indicator','earnings_per_share']]
# grouped = df.groupby('market_cap_category')
# for name, group in grouped:
# 	print(group)
# 	corr = group.corr(method='spearman',numeric_only=True)
# 	corr.to_csv('styled_correlation_matrix.csv')
# 	mask = np.zeros_like(corr, dtype=bool)
# 	mask[np.triu_indices_from(mask)] = True
# 	corr[mask] = np.nan
# 	(corr
# 	 .style
# 	 .background_gradient(cmap='coolwarm', axis=None, vmin=-1, vmax=1)
# 	 .highlight_null(color='#f1f1f1') 
# 	 .format(precision=2))


# 	plt.figure(figsize=(10, 8))
# 	sns.heatmap(corr, cmap='coolwarm', annot=True, fmt=".2f", annot_kws={"size": 10})
# 	plt.title('Correlation Heatmap')
# 	plt.xticks(rotation=45)
# 	plt.yticks(rotation=45)
# 	plt.tight_layout()
# 	plt.savefig(f'./heatmaps/market_cap/{name}-correlation_heatmap.png')


