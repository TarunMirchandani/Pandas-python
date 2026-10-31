import pandas as pd

df = pd.read_csv("data.csv", index_col="name")

# Creating variable
person = input("Enter any person name: ")

try:
    # Use .loc to look up the string label entered by the user
    result = df.loc[person]
    print(f"\nData for {person}:")
    print(result)

except KeyError:
    # This catches the error if the name does not exist in the index
    print(f"\nError: The name '{person}' was not found in the dataset.")
