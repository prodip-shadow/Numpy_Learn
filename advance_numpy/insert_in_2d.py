""" """

import numpy as np

arr_2d = np.array([[1, 2], [2, 3]])

# insert a new row
new_arr_2d_row = np.insert(arr_2d, 1, [5, 6], axis=1)
new_arr_2d_column = np.insert(arr_2d, 1, [5, 6], axis=0)
new_arr_2d_none = np.insert(arr_2d, 1, [5, 6], axis=None)


print(new_arr_2d_row)
print()
print(new_arr_2d_column)
print()
print(new_arr_2d_none)
