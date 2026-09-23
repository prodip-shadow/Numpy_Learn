"""
.ravel() => views
.flatten() => copy
"""

import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.ravel())    # view -> original array will be changed
print(arr_2d.flatten())  # copy -> original array will not be changed
