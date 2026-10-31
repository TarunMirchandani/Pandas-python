#selection by column
import pandas as pd

# Removed the leading space from the file name
df = pd.read_csv("data.csv") 

# Selection by column and printing it completely
print(df["name"].to_string())


# if want to print two to three column at one time 
# print(df[["Name","Height"]].to_string())