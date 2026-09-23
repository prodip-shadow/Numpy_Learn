"""
np.concatenarte((array1,array2),axis=0/1)

axis=0 -> vertical stacking
axis=1 -> horizonal stacking  [For 2D array]
"""

import numpy as np

arr1 = np.array([10, 20, 30])

arr2 = np.array([40, 50, 60])
newArr1 = np.concatenate((arr1, arr2), axis=0)

print(newArr1)
