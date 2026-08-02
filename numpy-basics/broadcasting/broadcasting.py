#Broadcasting
#Without Broadcasting:

prices=[100,200,300,400]
discount=10 #percent
final_prices=[]
for price in prices:
    final_price=price-(price*discount)/100
    final_prices.append(final_price)
print(final_prices)

#Loops are slow, so we use broadcasting where we apply different operations without using loops doesnt matter the size of array, basically faster
import numpy as np
prices=np.array([100,200,300,400])
discount =10
final_prices= prices-(discount *prices)/100
print(final_prices)

#How numpy handles arrays of differ shapes? (Boradcasting rules)
'''
1) matching dimension :[1,2,3]+[4,5,6]=[5,7,9]
2) EXpanding single elements eg: [1,2,3]+10 =[11,12,13] or [1,2,3] *2 =[1,4,6]

3) incompatible shapes: error, [1,2,3,4]+[1,2]:error
'''

#1d_2d
matrix=np.array([[1,2,3],[4,5,6]])
vector=np.array([10,20,30])

result = matrix *vector
print(result)

