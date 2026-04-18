import pandas as pd
import numpy as np
import random

df = pd.read_csv('robust_augmented_prices.csv')
markets_lookup = pd.read_csv('markets_lookup.csv')

all_governorates = markets_lookup[markets_lookup['admin1'] != 'National']['admin1'].unique()

national_data = df[df['Governorate'] == 'National'].copy()
real_geo_data = df[df['Governorate'] != 'National'].copy()

distributed_records = []

for _, row in national_data.iterrows():
    for gov in all_governorates:
        new_row = row.copy()
        new_row['Governorate'] = gov
        geo_variation = random.uniform(0.97, 1.03)
        new_row['Price'] = round(row['Price'] * geo_variation, 2)
        distributed_records.append(new_row)

final_geo_df = pd.concat([real_geo_data, pd.DataFrame(distributed_records)], ignore_index=True)

print(f"Original Rows: {len(df)}")
print(f"Rows after Geo-Distribution: {len(final_geo_df)}")

#print(final_geo_df.head())


final_geo_df.to_csv('final_geographical_distribution.csv', index=False)



