'''
np.delete(arrat,index,axis=None)
axis=None: deletion from flattened array
axis=0:...
axis=1:...
'''

import numpy as np
arr1= np.array([1,2,3,4,5])

new_arr1=np.delete(arr1,(3,4))
print(f"{arr1}\n\n{new_arr1}")

#2d array deletion

arr_2d=np.array([[1,2,3],[4,5,6]])
new_arr_2d_1=np.delete(arr_2d,0,axis=0)
new_arr_2d_2=np.delete(arr_2d,2,axis=1)
print(f"\n\n{arr_2d}\n\n{new_arr_2d_1}\n\n{new_arr_2d_2}")