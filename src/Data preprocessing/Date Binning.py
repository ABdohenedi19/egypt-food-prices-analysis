import pandas as pd

df = pd.read_csv('1_standardized_units.csv')

df['Date'] = pd.to_datetime(df['Date'])

df['Date'] = df['Date'].dt.strftime('%b-%Y')


output_name = '2_formatted_dates_full_data.csv'
df.to_csv(output_name, index=False)












