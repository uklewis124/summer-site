import pandas as pd
import os
import colorama

# Get whole dataframe as df
df = pd.read_csv("data_prep/data.csv")
print(df)

# Getting only columns containing numbers
stars_df = df.copy()
stars_df = stars_df[["HTML"], ["Java"]]
print(stars_df)
