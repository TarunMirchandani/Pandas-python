import pandas as pd

# Create a Python list with numbers
data = [200, 245, 300, 345, 400]

# Convert the list into a Pandas Series
series = pd.Series(data)

# Print the Pandas Series to the console
print(series)


# =========================================================
# EXPECTED OUTPUT AFTER RUNNING THE CODE:
# =========================================================
# 
# 0    200
# 1    245
# 2    300
# 3    345
# 4    400
# dtype: int64
#
# Explanation: Left side shows automatic index labels (0 to 4),
# right side shows your data values, and 'dtype: int64' means 
# the data contains integers.
# =========================================================
# PART 2: Creating a Pandas Series with Custom Index (A, B, C, D, E)
# =========================================================

# Create custom labels for the index
custom_index = ['A', 'B', 'C', 'D', 'E']

# Pass the custom index inside pd.Series()
series_with_labels = pd.Series(data, index=custom_index)

# Print the updated Series to the console
print("\n--- Series with Custom Index ---")
print(series_with_labels)


# =========================================================
# EXPECTED OUTPUT FOR PART 2:
# =========================================================
# 
# A    200
# B    245
# C    300
# D    345
# E    400
# dtype: int64
#
# Explanation: Now instead of 0, 1, 2, 3, 4, the rows are labeled 
# with your custom letters A, B, C, D, E.

