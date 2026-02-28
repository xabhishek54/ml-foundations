#Creating Array with default Values: 
# Using Zero Function(Filling with Zeroes as default)
import numpy as np
zeroes_array=np.zeros(3)
print(zeroes_array)

#Filling with Ones
#ones(shape), if 2d then put inside a tuple
ones_array=np.ones((2,3))
print(ones_array)

#Filling with Specific Values
#full(shape,value)
array=np.full((3,2),7)
print(array)