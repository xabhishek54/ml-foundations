# Slicing uses:
# Syntax: arr[start:stop:step] or arr[start:stop], start to (end -1)
# negative step, -1 reverses the array
import numpy as np
arr=np.array([10,34,23,45,34,23,12])
print(arr[1:5]) #index from 1 to 5
print(arr[:3]) #index from begin to 2
print(arr[3:]) #index from 3 to end
print(arr[::2]) #all elements but step 2
print(arr[::-1]) #Reverse the arr
