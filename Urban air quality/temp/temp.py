import pandas as pd

df = pd.read_csv("stationfinal.csv")

# # Check columns
# print(df.columns)

# # Drop the correct column name with lowercase 'd'
# df.drop("Date", inplace=True, axis=1)

# # Save it back
# df.to_csv('stationfinal.csv', index=False)

# print("✅ Column dropped and saved successfully!")


print(df.isnull().sum())

import pandas as pd


# Fill with mean (for numeric columns)
df['PM2.5'] = df['PM2.5'].fillna(df['PM2.5'].mean(), inplace=True)
df['PM10'] = df['PM10'].fillna(df['PM10'].mean(), inplace=True)


