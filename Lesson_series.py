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

