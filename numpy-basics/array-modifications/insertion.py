'''
Array modifications creates a new array in nump because a numpy array when creeated has a fixed size

np.insert(array, index, value, axis=None)
array -> original array(It dont get modified btw)
index-
value-
axis=None, flattens if 2d then inserts (default)
axis=0, row wise
axis=1, column wise
'''
import numpy as np

#Inserting in a 1D array
arr=np.array([10,20,30,40,50])
print(f"Original array : {arr}")
new_arr=np.insert(arr,2,25)
print(f"The new array is: {new_arr}")

#insering in 2D array
arr_2d=np.array([[1,2,3,4,5],
                 [10,20,30,40,50]])
#Inserting a row at index 1
new_arr_2d_row=np.insert(arr_2d,1,[5,15,25,35,45])
new_arr_2d_row=np.insert(arr_2d,1,[5,15,25,35,45],axis=0)
new_arr_2d_column=np.insert(arr_2d,3,[5,15],axis=1)
print(f"The original array:\n{arr_2d}\n")
print(f"The Modigied array:\n{new_arr_2d_row}\n")
print(f"The Modified array:\n{new_arr_2d_column}\n")

