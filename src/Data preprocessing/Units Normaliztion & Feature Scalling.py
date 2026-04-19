import pandas as pd


df = pd.read_csv('egypt_food_prices_no_missing_gov.csv')


def standardize_units(row):
    unit = str(row['Unit']).upper()
    price = row['Price']

    if '800 G' in unit:
        row['Price'] = round(price * 1.25, 2)
        row['Unit'] = 'KG'

    elif ' G' in unit and 'KG' not in unit:
        try:
            grams = float(''.join(filter(str.isdigit, unit)))
            if grams > 0:
                row['Price'] = round((price / grams) * 1000, 2)
                row['Unit'] = 'KG'
        except:
            pass

    return row



df_units = df.apply(standardize_units, axis=1)


df_units.to_csv('1_standardized_units.csv', index=False)








