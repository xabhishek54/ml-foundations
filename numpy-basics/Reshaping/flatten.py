'''Flatting array
usuage: converting multidimensional array into one dimensional
.ravel()-> view
.flatten()-> copy

'''
import numpy as np;
arr_2d=np.array([[1,2,3],[23,5,67]])
print(arr_2d.ravel())
print(arr_2d.flatten())
