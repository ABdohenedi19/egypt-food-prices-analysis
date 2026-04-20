import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(BASE_DIR, '../../Data/preprocessed/preprocessed data.csv')
output_file = os.path.join(BASE_DIR, '../../Data/preprocessed/final_cleaned_data.csv')

df = pd.read_csv(input_file)

df['Date'] = pd.to_datetime(df['Date'])
if 'Year' not in df.columns:
    df['Year'] = df['Date'].dt.year

def clean_outliers_preserving_order(data):
   
    grouped = data.groupby(['Product', 'Year'])['Price']

    q1 = grouped.transform(lambda x: x.quantile(0.25))
    q3 = grouped.transform(lambda x: x.quantile(0.75))
    iqr = q3 - q1

    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    mask = (data['Price'] >= lower_limit) & (data['Price'] <= upper_limit)

    return data[mask].copy()

print(f"Shape before cleaning: {df.shape}")
df_final = clean_outliers_preserving_order(df)
print(f"Shape after cleaning: {df_final.shape}")

df_final.to_csv(output_file, index=False)
print(f"Success! Cleaned data saved at: {output_file}")