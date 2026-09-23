"""
hsplit => horzinal split
vsplit => vartical split
"""

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])


print(np.split(arr1, 2))


import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print()
print(np.vsplit(arr, 3))
print()
print(np.hsplit(arr, 2))
