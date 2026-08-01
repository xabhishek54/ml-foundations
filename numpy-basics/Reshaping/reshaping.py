'''
Reshaping: Changing the dimensions of an array without modifying the data
eg 1d ->2d
2d->3d
usuage: arr.reshape()
reshape(rows,columns) specify new shape
reshape() returns a view whenever possible, meaning the new array shares the same data with the original array.
If a view isn't possible (for example, due to memory layout), NumPy creates a copy.
A view is a new array that looks different (different shape or slice) but uses the same underlying data as the original array.

Think of it like this:

View = another window looking at the same data.
Copy = a completely new set of data.
'''
import numpy as np;
arr=np.array([23,34,45,56,67,78])

arr.reshape([2,3])
print(arr.reshape([2,3]))
arr.reshape([2,3])
print(arr)
arr=arr.reshape([2,3])
print(arr)