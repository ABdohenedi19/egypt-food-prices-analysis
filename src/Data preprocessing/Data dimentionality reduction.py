import pandas as pd

file_name = 'final_geographical_distribution.csv'
df = pd.read_csv(file_name)


if 'Market' in df.columns:
    df.drop(columns=['Market'], inplace=True)
    print("Deleted succesfully")
else:
    print("Column not found")

output_name = 'egypt_food_prices_final_preprocessed.csv'
df.to_csv(output_name, index=False)





