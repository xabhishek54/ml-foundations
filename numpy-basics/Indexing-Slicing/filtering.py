'''
filtering: slecting elements which passes a particular condition
boolean_masking: 10x faster then loops
'''
import numpy as np
arr=np.array([12,21,344,42,53,61])

print(arr[arr%2==0])

