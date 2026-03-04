import numpy as np

arr_2d=np.array([[1,2,3],
                [5,3,2]])

#Shape Property: no. of rows and columns
print(arr_2d.shape,"(rowsxcolumns)")

#Size Property: No. of values stored
print(arr_2d.size, "Values Stored")

#ndim: no. of dimensions
arr1=np.array([1,2,3])
arr2=np.array([[1,2,3],[2,3,4],[4,3,2]])
arr3=np.array([
    [[2,3,4],[1,1,1]],
    [[3,4,5],[2,2,2]],
    [[2,3,1],[3,3,3]]
])
arr4=np.array([
        [
            [[2,3],[4,5]]
        ],
        [
            [[3,4],[2,3]]
        ]
    ])
print(arr1.ndim,"-D Array")
print(arr2.ndim,"-D Array")
print(arr3.ndim,"-D Array")
print(arr4.ndim,"-D Array")

#.dtype attribute: data type of elements, returns the data type(int,float,str)
arr=np.array([10,23.3])
print(arr.dtype)


#.astype(_datatype_): Converts the datatype

arr=np.array(["12345"])
int_arr=arr.astype(int)
print(int_arr)

arr=np.array([1.2,4.5,6.8,3.5])
print(arr.dtype)
int_arr=arr.astype(int)
print(int_arr)
