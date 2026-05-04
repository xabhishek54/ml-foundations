'''. Even–Odd Split
Create an array from 1 to 50.
Extract all even numbers.
Extract all odd numbers.
Compute mean of even numbers.
Compute sum of odd numbers.
No loops allowed.'''

import numpy as np

#Creating array from 1 to 50
arr=np.arange(1,51)
print(arr)
#Use Boolean indexing/ Boolean Masking, arr%2==0 creates an array of boolean of true and false, and when indexed only shows values where it is true
even_arr=arr[arr%2==0]
odd_arr=arr[arr%2!=0]
print("Even Array", even_arr)
print("Odd Array",odd_arr)

print("The mean of even numbers is", np.mean(even_arr))
print("The sum of odd numbers is", np.sum(odd_arr))




