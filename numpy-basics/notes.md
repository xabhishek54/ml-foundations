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

### Output

```python
550
55.0
10
100
28.722813232690143
825.0
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

### Output

```python
(2, 3)
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

### Output

```python
6
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

### Output

```python
1
2
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

### Output

```python
float64
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

### Output

```python
[1 4 6]
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

### Output

```python
[15 25 35 45]
[ 50 100 150 200]
[2. 4. 6. 8.]
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


---

# Indexing

Indexing is used to access a specific element in a NumPy array.

- **Positive Indexing:** Starts from the beginning (`0, 1, 2, ...`)
- **Negative Indexing:** Starts from the end (`-1, -2, -3, ...`)
- If an index is outside the array's range, Python raises an **IndexError**.

### Syntax

```python
array[index]
```

### Example

```python
import numpy as np

arr = np.array([10, 25, 43, 67, 34, 19])

print(arr[2])
print(arr[0])
print(arr[-1])
```

### Output

```python
43
10
19
```

### Description

- `arr[2]` returns the element at index `2`.
- `arr[0]` returns the first element.
- `arr[-1]` returns the last element.

---

# Slicing

Slicing is used to access multiple elements from an array.

### Syntax

```python
array[start:stop:step]
```

- `start` → Starting index (inclusive)
- `stop` → Ending index (exclusive)
- `step` → Interval between elements (default is `1`)

If `start`, `stop`, or `step` are omitted, NumPy uses sensible defaults.

### Example

```python
import numpy as np

arr = np.array([10, 34, 23, 45, 34, 23, 12])

print(arr[1:5])
print(arr[:3])
print(arr[3:])
print(arr[::2])
print(arr[::-1])
```

### Output

```python
[34 23 45 34]
[10 34 23]
[45 34 23 12]
[10 23 34 12]
[12 23 34 45 23 34 10]
```

### Description

| Expression | Meaning |
|------------|---------|
| `arr[1:5]` | Elements from index `1` to `4` |
| `arr[:3]` | From beginning to index `2` |
| `arr[3:]` | From index `3` to the end |
| `arr[::2]` | Every second element |
| `arr[::-1]` | Reverses the array |

> **Note:** A negative step (`-1`) traverses the array in reverse order.

---

# Fancy Indexing

Fancy indexing allows you to select multiple elements at once by providing a list (or array) of indices.

### Syntax

```python
array[[index1, index2, index3]]
```

### Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[[0, 2, 4]])
```

### Output

```python
[10 30 50]
```

### Description

Instead of selecting one element, fancy indexing returns a new array containing all the specified indices.

---

# Filtering (Boolean Masking)

Filtering selects elements that satisfy a given condition.

Boolean masking is one of NumPy's most powerful features and is much faster than checking each element using Python loops.

### Syntax

```python
array[condition]
```

### Example

```python
import numpy as np

arr = np.array([12, 21, 344, 42, 53, 61])

print(arr[arr % 2 == 0])
```

### Output

```python
[ 12 344  42]
```

### Description

- `arr % 2 == 0` creates a Boolean array:
  ```python
  [ True False True True False False ]
  ```
- NumPy returns only the elements corresponding to `True`.

Boolean masking can be used with many conditions, such as:

```python
arr[arr > 50]      # Elements greater than 50
arr[arr < 20]      # Elements less than 20
arr[arr == 42]     # Elements equal to 42
arr[arr != 21]     # Elements not equal to 21
```

---

## Quick Summary

| Concept | Syntax |
|---------|--------|
| Indexing | `arr[index]` |
| Negative Indexing | `arr[-1]` |
| Slicing | `arr[start:stop:step]` |
| Reverse Array | `arr[::-1]` |
| Fancy Indexing | `arr[[0,2,4]]` |
| Boolean Masking | `arr[arr > value]` |
| Filter Even Numbers | `arr[arr % 2 == 0]` |

```

---

# Reshaping Arrays

Reshaping changes the dimensions (shape) of an array **without changing its data**.

For example:
- **1D → 2D**
- **2D → 3D**
- **3D → 1D**, etc.

A reshape is only possible if the **total number of elements remains the same**.

> **Formula:**  
> Total Elements = Product of Dimensions

For example:
- `(6,) → (2,3)` ✅ because `6 = 2 × 3`
- `(6,) → (3,2)` ✅ because `6 = 3 × 2`
- `(6,) → (4,2)` ❌ because `8 ≠ 6`

### Syntax

```python
array.reshape(rows, columns)
```

### Example

```python
import numpy as np

arr = np.array([23, 34, 45, 56, 67, 78])

arr = arr.reshape((2, 3))

print(arr)
```

### Output

```python
[[23 34 45]
 [56 67 78]]
```

### Description

- Reshape changes only the structure of the array.
- The data remains in the same order.
- `reshape()` usually returns a **view** of the original array rather than creating a copy.
- Since it returns a view, modifying the reshaped array may also affect the original array.

---

# Flattening Arrays

Flattening converts a multi-dimensional array into a one-dimensional array.

NumPy provides two common methods:

- `.ravel()` → Returns a **view** (shares memory with the original array whenever possible).
- `.flatten()` → Returns a **copy** (independent of the original array).

### Syntax

```python
array.ravel()

array.flatten()
```

### Example

```python
import numpy as np

arr_2d = np.array([
    [1, 2, 3],
    [23, 5, 67]
])

print(arr_2d.ravel())
print(arr_2d.flatten())
```

### Output

```python
[ 1  2  3 23  5 67]
[ 1  2  3 23  5 67]
```

### Description

Although both methods produce the same output, they behave differently:

| Method | Returns | Memory Usage |
|---------|----------|--------------|
| `.ravel()` | View | Shares memory with the original array |
| `.flatten()` | Copy | Creates a new independent array |

### Example of the Difference

```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])

view = arr.ravel()
copy = arr.flatten()

view[0] = 100

print(arr)
print(copy)
```

### Output

```python
[[100   2]
 [  3   4]]

[1 2 3 4]
```

### Explanation

- Changing `view` also changes the original array because it shares the same memory.
- Changing `copy` does **not** affect the original array because it is a separate copy.

---

## Quick Summary

| Concept | Syntax |
|---------|--------|
| Reshape Array | `arr.reshape(rows, columns)` |
| Flatten (View) | `arr.ravel()` |
| Flatten (Copy) | `arr.flatten()` |
| Total Elements Must Match | `rows × columns = original size` |