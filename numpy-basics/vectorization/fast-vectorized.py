#Vectorization: 
'''
Difference:
Broadcasting expands smaller arrays to larger array to match
it is faster than loops
1D->2D

Vectorization applies directly for entrie array
100x faster loops
matrix operation usuage

'''

import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
result = arr1 + arr2
print(result)

arr=np.array([10,20,30])
multiplied=arr *3
print(multiplied)