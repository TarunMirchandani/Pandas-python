# Selection by row
# Option 1: If you want to get the first row by its position Keep index_col="name" but use .iloc[](integer-location) instead of .loc[]. .iloc[] always looks at row positions (0 for the first row, 1 for the second, etc.) regardless of what the index labels are:


import pandas as pd

df = pd.read_csv("data.csv", index_col="name")
print(df.iloc[0])  # Works perfectly!


# Option 2: If you want to look up a row by a person's name
Keep .loc[] but pass the specific text label (the name) you are searching for

import pandas as pd

df = pd.read_csv("data.csv", index_col="name")
print(df.loc["Alice"])  # Looks up the row for Alice
