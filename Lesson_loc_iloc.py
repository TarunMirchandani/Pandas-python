import pandas as pd

# Data and Series setup
data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])

print("--- Original Series ---")
print(series)

# 1. Using .loc (Label/Name se search)
print("\n--- Using loc ---")
print(series.loc['C'])

# 2. Using .iloc (Position number se search)
print("\n--- Using iloc ---")
print(series.iloc[2])


# =========================================================
# EXPECTED OUTPUT:
# =========================================================
#
# --- Original Series ---
# A    10
# B    20
# C    30
# D    40
# E    50
# dtype: int64
#
# --- Using loc ---
# 30
#
# --- Using iloc ---
# 30
#
# Explanation: .loc used the letter 'C' to find 30. 
# .iloc used the position number 2 (0, 1, 2) to find 30.
