# NumPy Basics Notes

> Each example below also includes the expected output for better understanding.

## Importing NumPy

```python
import numpy as np
```

`numpy` is imported with the alias `np` to make code shorter and easier to write.

---

# Creating Arrays

## 1D Array

### Syntax

```python
np.array([values])
```

### Example

```python
import numpy as np

arr_1d = np.array([15, 20, 30, 40])
print(arr_1d)
```

### Output

```python
[15 20 30 40]
```

### Description

A 1D array stores elements in a single row, similar to a Python list.

---

## 2D Array

### Syntax

```python
np.array([[row1], [row2]])
```

### Example

```python
import numpy as np

arr_2d = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])

print(arr_2d)
```

### Output

```python
[[1 2 3]
 [2 3 4]
 [4 5 6]]
```

### Description

A 2D array stores data in rows and columns like a matrix.

---

# Arrays with Default Values

## Array Filled with Zeroes

### Syntax

```python
np.zeros(shape)
```

### Example

```python
import numpy as np

zeroes_array = np.zeros(3)
print(zeroes_array)
```

### Output

```python
[0. 0. 0.]
```

### Description

Creates an array filled with `0` values.

---

## Array Filled with Ones

### Syntax

```python
np.ones(shape)
```

### Example

```python
import numpy as np

ones_array = np.ones((2, 3))
print(ones_array)
```

### Output

```python
[[1. 1. 1.]
 [1. 1. 1.]]
```

### Description

Creates an array filled with `1` values.

---

## Array Filled with Specific Value

### Syntax

```python
np.full(shape, value)
```

### Example

```python
import numpy as np

array = np.full((3, 2), 7)
print(array)
```

### Output

```python
[[7 7]
 [7 7]
 [7 7]]
```

### Description

Creates an array where every element contains the same value.

---

# Creating Number Sequences

## arange()

### Syntax

```python
np.arange(start, stop, step)
```

### Example

```python
import numpy as np

arr = np.arange(2, 22, 2)
print(arr)
```

### Output

```python
[ 2  4  6  8 10 12 14 16 18 20]
```

### Description

Works similarly to Python's `range()` function and creates numbers in a sequence.

---

# Identity Matrix

## eye()

### Syntax

```python
np.eye(size)
```

### Example

```python
import numpy as np

identity_matrix = np.eye(4)
print(identity_matrix)
```

### Output

```python
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```

### Description

Creates an identity matrix where diagonal elements are `1` and others are `0`.

---

# Multi-Dimensional Arrays (Matrix)

### Example

```python
import numpy as np

matrix = np.array([
    [2, 4, 5],
    [8, 10, 12]
])

print(matrix)
```

### Output

```python
[[ 2  4  5]
 [ 8 10 12]]
```

### Description

A matrix is basically a 2D NumPy array.

---

# NumPy Aggregation Functions

### Example

```python
import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90,100])

print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))
```

## Common Aggregation Functions

| Function    | Description                |
| ----------- | -------------------------- |
| `np.sum()`  | Returns total sum          |
| `np.mean()` | Returns average value      |
| `np.min()`  | Returns smallest value     |
| `np.max()`  | Returns largest value      |
| `np.std()`  | Returns standard deviation |
| `np.var()`  | Returns variance           |

---

# NumPy Array Properties

## shape

### Syntax

```python
array.shape
```

### Example

```python
import numpy as np

arr_2d = np.array([
    [1,2,3],
    [5,3,2]
])

print(arr_2d.shape)
```

### Description

Returns the number of rows and columns.

---

## size

### Syntax

```python
array.size
```

### Example

```python
print(arr_2d.size)
```

### Description

Returns the total number of elements stored in the array.

---

## ndim

### Syntax

```python
array.ndim
```

### Example

```python
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[2,3,4]])

print(arr1.ndim)
print(arr2.ndim)
```

### Description

Returns the number of dimensions of the array.

---

## dtype

### Syntax

```python
array.dtype
```

### Example

```python
import numpy as np

arr = np.array([10, 23.3])
print(arr.dtype)
```

### Description

Shows the datatype of array elements such as `int`, `float`, or `str`.

---

## astype()

### Syntax

```python
array.astype(datatype)
```

### Example

```python
import numpy as np

arr = np.array([1.2, 4.5, 6.8])
int_arr = arr.astype(int)

print(int_arr)
```

### Description

Converts array elements into another datatype.

---

# Array Operations

### Example

```python
import numpy as np

arr = np.array([10,20,30,40])

print(arr + 5)
print(arr * 5)
print(arr / 5)
```

### Description

NumPy allows mathematical operations directly on arrays.

| Operation | Meaning                       |
| --------- | ----------------------------- |
| `arr + 5` | Adds 5 to every element       |
| `arr * 5` | Multiplies every element by 5 |
| `arr / 5` | Divides every element by 5    |

---

# NumPy Performance Example

### Example

```python
import numpy as np

testarray = [1,2,3,4,5] * 100000
array = np.array(testarray)

print(array)
```

### Description

NumPy arrays are faster and more memory-efficient than normal Python lists for large datasets.

---

# Quick Summary

| Concept             | Function         |
| ------------------- | ---------------- |
| Create array        | `np.array()`     |
| Zeroes array        | `np.zeros()`     |
| Ones array          | `np.ones()`      |
| Fill with value     | `np.full()`      |
| Sequence of numbers | `np.arange()`    |
| Identity matrix     | `np.eye()`       |
| Sum                 | `np.sum()`       |
| Mean                | `np.mean()`      |
| Dimensions          | `array.ndim`     |
| Shape               | `array.shape`    |
| Datatype            | `array.dtype`    |
| Type conversion     | `array.astype()` |
