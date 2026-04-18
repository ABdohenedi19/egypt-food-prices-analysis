import pandas as pd
import numpy as np
from datetime import timedelta
import random

df = pd.read_csv('final_integrated_dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])

behavior_map = {
    'cereals and tubers': (-0.01, 0.02),
    'meat, fish and eggs': (0.02, 0.08),
    'milk and dairy': (0.01, 0.05),
    'vegetables and fruits': (-0.10, 0.15),
    'default': (-0.02, 0.05)
}

augmented_list = [df]

for i in range(1, 5):
    temp_df = df.copy()
    temp_df['Date'] = temp_df['Date'] + timedelta(days=6 * i)


    def apply_advanced_price(row):
        outlier_chance = random.random()

        if outlier_chance < 0.02:  # 2% احتمال
            outlier_type = random.choice(['expensive', 'cheap'])
            if outlier_type == 'expensive':
                return round(row['Price'] * random.uniform(2.5, 5.0), 2)
            else:
                return round(row['Price'] * random.uniform(0.1, 0.3), 2)

        category = row['Category']
        low, high = behavior_map.get(category, behavior_map['default'])
        random_change = random.uniform(low, high)
        return round(row['Price'] * (1 + random_change), 2)


    temp_df['Price'] = temp_df.apply(apply_advanced_price, axis=1)
    augmented_list.append(temp_df)


final_robust_df = pd.concat(augmented_list, ignore_index=True)
final_robust_df.to_csv('robust_augmented_prices.csv', index=False)

print("Augmentation finished with Realistic Behaviors and Outliers!")
