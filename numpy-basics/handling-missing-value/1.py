'''
The builtin function in numpy array

np.isnan(): descirrbe a bit

np.nan
'''

import numpy as np
arr=np.array([1,2,np.nan,4,5,np.nan])
print(np.isnan(arr))
#Also we cant compare the values from np.nan directly(good interview questions , hpw can we ?)

print(np.nan==np.nan)

