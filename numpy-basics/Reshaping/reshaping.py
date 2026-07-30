'''
Reshaping: Changing the dimensions of an array without modifying the data
eg 1d ->2d
2d->3d
usuage: arr.reshape()
reshape(rows,columns) specify new shape
if dimensions match
reshaping dont create copy but make changes on actual array
give views instead of copy
'''
import numpy as np;
arr=np.array([23,34,45,56,67,78])

arr=arr.reshape([2,3])
print(arr)