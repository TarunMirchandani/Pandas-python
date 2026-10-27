import pandas as pd

# Creating a Python dictionary with correct quotes
data = {
"name": ["Om", "Jay", "Jagdish"], 
"age": [12 , 13 ,14]
}

# Converting the dictionary into a Pandas DataFrame (Capital D and F)
df = pd.DataFrame(data)

print("--- Creating a DataFrame ---")
print(df)


# =========================================================
# EXPECTED OUTPUT:
# =========================================================
#
# --- Creating a DataFrame ---
#       name  age
# 0       Om   12
# 1      Jay   13
# 2  Jagdish   14
#
# Explanation: Pandas converted the dictionary into a clean table 
# with 'name' and 'age' as columns and automatic index 0, 1, 2.
