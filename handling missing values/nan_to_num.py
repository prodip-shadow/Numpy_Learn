import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])
cleaned_array = np.nan_to_num(arr, nan=3)
print(cleaned_array)
