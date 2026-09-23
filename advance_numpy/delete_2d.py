import numpy as np

arr_2d = np.array([[10, 20, 30], [40, 50, 60]])

new_arr_2d_1 = np.delete(arr_2d, 0, axis=1)
new_arr_2d_0 = np.delete(arr_2d, 0, axis=0)

print(new_arr_2d_1)
print()
print(new_arr_2d_0)
