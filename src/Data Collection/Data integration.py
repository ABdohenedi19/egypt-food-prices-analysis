import pandas as pd

df_prices = pd.read_csv('prices.csv')

df_markets = pd.read_csv('markets_lookup.csv')

merged_df = pd.merge(
    df_prices,
    df_markets[['market_id', 'admin1', 'admin2']],
    on='market_id',
    how='left'
)

# Feature Product, Category, Price, Date, Governorate, Market, Unit
final_df = merged_df[[
    'commodity',    # Product
    'category',     # Category
    'price',        # Price
    'date',         # Date
    'admin1',       # Governorate
    'market',       # Market
    'unit'          # Unit
]]

final_df.columns = ['Product', 'Category', 'Price', 'Date', 'Governorate', 'Market', 'Unit']

final_df.to_csv('final_integrated_dataset.csv', index=False)

print("final_integrated_dataset.csv")
print(final_df.head())

