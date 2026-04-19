import pandas as pd

file_name = 'egypt_food_prices_final_sorted.csv'
df = pd.read_csv(file_name)

before_count = len(df)
df.dropna(subset=['Governorate'], inplace=True)
after_count = len(df)


output_name = 'egypt_food_prices_no_missing_gov.csv'
df.to_csv(output_name, index=False)







