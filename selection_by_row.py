# Selection by row
 """ 

Option 1: If you want to get the first row by its position

Keep index_col="name" but use .iloc[] (integer-location) instead of .loc[]. .iloc[] always looks at row positions (0 for the first row, 1 for the second, etc.) regardless of what the index labels are:
 """