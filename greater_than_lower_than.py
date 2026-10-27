import pandas as pd

# Setting up the Series (Using data from the previous series)
data = [200, 245, 300, 345, 400]
series = pd.Series(data)

print("--- Original Series ---")
print(series)

# 1. Finding values greater than or equal to 300
print("--- Greater than or equal to 300 ---")
print(series[series >= 300])

# 2. Finding values less than 300
print("--- Less than 300 ---")
print(series[series < 300])


# =========================================================
# EXPECTED OUTPUT:
# =========================================================
#
# --- Original Series ---
# 0    200
# 1    245
# 2    300
# 3    345
# 4    400
# dtype: int64
#
# --- Greater than or equal to 300 ---
# 2    300
# 3    345
# 4    400
# dtype: int64
#
# --- Less than 300 ---
# 0    200
# 1    245
# dtype: int64
#
# Explanation: Writing series[series >= 300] tells Pandas to check 
# every value and only return the rows where the condition is True.
