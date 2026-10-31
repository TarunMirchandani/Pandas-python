#selection by column
import pandas as pd

# Removed the leading space from the file name
df = pd.read_csv("data.csv") 

# Selection by column and printing it completely
print(df["name"].to_string())
