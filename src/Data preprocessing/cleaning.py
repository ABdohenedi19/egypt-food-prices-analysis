import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, '../../Data/preprocessed/preprocessed data.csv')
df = pd.read_csv(file_path)

df['Product'] = df['Product'].astype(str).str.strip()
df['Category'] = df['Category'].astype(str).str.strip()

# (Data Consolidation)
egg_mask = df['Product'].str.contains('Eggs', case=False, na=False)
df.loc[egg_mask, 'Product'] = 'Eggs'
df.loc[egg_mask, 'Unit'] = '1 piece'

# (Beef)
beef_mask = df['Product'].str.contains('Meat \(beef', case=False, na=False)
df.loc[beef_mask, 'Product'] = 'Meat (beef)'

# (Filtering)
df = df[~df['Product'].str.contains('Milk', case=False, na=False)]

# 
threshold = 500
product_counts = df['Product'].value_counts()
to_keep = product_counts[product_counts >= threshold].index

df_filtered = df[df['Product'].isin(to_keep)].copy()

output_path = os.path.join(BASE_DIR, 'cleaned_consolidated_prices.csv')
df_filtered.to_csv(output_path, index=False)

print(f"Original shape: {df.shape}")
print(f"Filtered shape: {df_filtered.shape}")
print(f"Products removed: {len(product_counts) - len(to_keep)}")
print(f"Final file saved as: {output_path}")