import pandas as pd


file_name = 'egypt_food_prices_final_preprocessed.csv'
df = pd.read_csv(file_name)


df['Date'] = pd.to_datetime(df['Date'])

df.sort_values(by=['Date', 'Governorate'], ascending=[True, True], inplace=True)




output_name = 'egypt_food_prices_final_sorted.csv'
df.to_csv(output_name, index=False)



df.head(10)





