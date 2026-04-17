import pandas as pd
from datetime import timedelta
import os

current_dir = os.getcwd()
file_name = 'final_integrated_dataset.csv'


try:
    df = pd.read_csv('final_integrated_dataset.csv')

    df['Date'] = pd.to_datetime(df['Date'])

    augmented_list = [df]
    for i in range(1, 5):
        temp_df = df.copy()
        temp_df['Date'] = temp_df['Date'] + timedelta(days=6 * i)
        temp_df['Price'] = round(temp_df['Price'] * (1.05 ** i), 2)
        augmented_list.append(temp_df)

    final_augmented_df = pd.concat(augmented_list, ignore_index=True)

    final_augmented_df.to_csv('augmented_food_prices.csv', index=False)

    print(f"Success! Total rows: {len(final_augmented_df)}")
    print("New file 'augmented_food_prices.csv' created in your folder.")

except FileNotFoundError:
    print("Error: this folder is not found.")
