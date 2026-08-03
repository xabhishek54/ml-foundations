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


---

# Array Manipulation

Unlike Python lists, **NumPy arrays have a fixed size after they are created**. Therefore, operations such as inserting, appending, or deleting elements **do not modify the original array**. Instead, they return a **new array** containing the changes.

---

# Inserting Elements

`np.insert()` inserts one or more values at a specified position and returns a new array.

### Syntax

```python
np.insert(array, index, values, axis=None)
```

### Parameters

- **array** → Original array
- **index** → Position where the value(s) should be inserted
- **values** → Value(s) to insert
- **axis**
  - `None` (default): Flattens the array before inserting
  - `0`: Insert row(s)
  - `1`: Insert column(s)

---

## Insert into a 1D Array

### Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

new_arr = np.insert(arr, 2, 25)

print(arr)
print(new_arr)
```

### Output

```python
[10 20 30 40 50]
[10 20 25 30 40 50]
```

### Description

The value `25` is inserted at index `2`. The original array remains unchanged because `np.insert()` returns a new array.

---

## Insert into a 2D Array

### Example

```python
import numpy as np

arr_2d = np.array([
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50]
])

# Insert a row
new_row = np.insert(arr_2d, 1, [5, 15, 25, 35, 45], axis=0)

# Insert a column
new_column = np.insert(arr_2d, 3, [5, 15], axis=1)

print(new_row)
print(new_column)
```

### Output

```python
[[ 1  2  3  4  5]
 [ 5 15 25 35 45]
 [10 20 30 40 50]]

[[ 1  2  3  5  4  5]
 [10 20 30 15 40 50]]
```

### Description

- `axis=0` inserts **rows**.
- `axis=1` inserts **columns**.
- `axis=None` (default) first flattens the array into one dimension before inserting.

---

# Appending Elements

`np.append()` adds one or more values to the end of an array and returns a new array.

### Syntax

```python
np.append(array, values, axis=None)
```

### Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

new_arr = np.append(arr, [50, 60])

print(arr)
print(new_arr)
```

### Output

```python
[10 20 30 40]
[10 20 30 40 50 60]
```

### Description

The values are added to the end of the array. The original array remains unchanged.

### Important Note

For multidimensional arrays, `axis=None` is the default, so NumPy first **flattens** the array before appending.

Example:

```python
import numpy as np

arr = np.array([
    [1, 2],
    [3, 4]
])

print(np.append(arr, [5, 6]))
```

### Output

```python
[1 2 3 4 5 6]
```

To append a **new row** instead:

```python
np.append(arr, [[5, 6]], axis=0)
```

---

# Concatenating Arrays

Concatenation joins two or more existing arrays into a single array.

### Syntax

```python
np.concatenate((array1, array2), axis=0)
```

### Axis

- `axis=0` → Join vertically (row-wise)
- `axis=1` → Join horizontally (column-wise)

For one-dimensional arrays, the axis can usually be omitted.

### Example

```python
import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([9,8,7,6])

new_arr = np.concatenate((arr1, arr2))

print(new_arr)
```

### Output

```python
[1 2 3 4 5 9 8 7 6]
```

### Description

All elements of the second array are placed after the first array.

### Requirement

All arrays must have the **same shape except along the concatenation axis**. Otherwise, NumPy raises a `ValueError`.

Example:

```python
a = np.array([[1,2]])
b = np.array([[3,4]])

np.concatenate((a, b), axis=0)
```

This works because both arrays have the same number of columns.

---

# Deleting Elements

`np.delete()` removes elements from an array and returns a new array.

### Syntax

```python
np.delete(array, index, axis=None)
```

### Parameters

- `axis=None` → Deletes after flattening the array
- `axis=0` → Delete row(s)
- `axis=1` → Delete column(s)

---

## Delete from a 1D Array

### Example

```python
import numpy as np

arr = np.array([1,2,3,4,5])

new_arr = np.delete(arr, (3,4))

print(arr)
print(new_arr)
```

### Output

```python
[1 2 3 4 5]
[1 2 3]
```

### Description

Elements at indices `3` and `4` are removed.

---

## Delete from a 2D Array

### Example

```python
import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

delete_row = np.delete(arr, 0, axis=0)
delete_column = np.delete(arr, 2, axis=1)

print(delete_row)
print(delete_column)
```

### Output

```python
[[4 5 6]]

[[1 2]
 [4 5]]
```

### Description

- `axis=0` removes rows.
- `axis=1` removes columns.

---

# Stacking Arrays

Stacking combines arrays either vertically or horizontally.

---

## Vertical Stack

### Syntax

```python
np.vstack((array1, array2))
```

### Example

```python
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.vstack((arr1, arr2)))
```

### Output

```python
[[1 2 3]
 [4 5 6]]
```

### Description

Stacks arrays one **below another** (row-wise).

---

## Horizontal Stack

### Syntax

```python
np.hstack((array1, array2))
```

### Example

```python
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.hstack((arr1, arr2)))
```

### Output

```python
[1 2 3 4 5 6]
```

### Description

Stacks arrays side by side (column-wise for multidimensional arrays).

### Requirements

- `np.vstack()` requires arrays to have the **same number of columns**.
- `np.hstack()` requires arrays to have the **same number of rows** (for 2D arrays).

If these conditions are not satisfied, NumPy raises a **ValueError**.

---

# Splitting Arrays

Splitting divides an array into multiple smaller arrays.

### Syntax

```python
np.split(array, sections)
```

### Example

```python
import numpy as np

arr = np.array([10,20,30,50,60,70])

print(np.split(arr, 3))
```

### Output

```python
[array([10, 20]), array([30, 50]), array([60, 70])]
```

### Description

`np.split()` divides an array into equal-sized parts and returns a **list of NumPy arrays**.

> **Note:** The total number of elements must be evenly divisible by the number of sections. Otherwise, NumPy raises a **ValueError**.

---

# Horizontal and Vertical Splitting

NumPy provides dedicated functions for splitting 2D arrays.

| Function | Purpose |
|----------|---------|
| `np.hsplit()` | Splits an array column-wise |
| `np.vsplit()` | Splits an array row-wise |

These functions are mainly used with multidimensional arrays.

---

# Choosing the Right Function

| Function | Use When |
|----------|----------|
| `np.insert()` | Insert elements at a specific position |
| `np.append()` | Add elements to the end |
| `np.concatenate()` | Join existing arrays |
| `np.vstack()` | Stack arrays vertically |
| `np.hstack()` | Stack arrays horizontally |
| `np.delete()` | Remove elements from an array |
| `np.split()` | Divide an array into equal parts |

---

# Quick Summary

| Operation | Function |
|-----------|----------|
| Insert element | `np.insert()` |
| Append element | `np.append()` |
| Join arrays | `np.concatenate()` |
| Delete element | `np.delete()` |
| Stack vertically | `np.vstack()` |
| Stack horizontally | `np.hstack()` |
| Split array | `np.split()` |
| Horizontal split | `np.hsplit()` |
| Vertical split | `np.vsplit()` |

> **Key Takeaway:** Since NumPy arrays have a fixed size, operations like **insert**, **append**, and **delete** always create and return a **new array** instead of modifying the original one.


---

# Broadcasting

Broadcasting is a feature in NumPy that allows arithmetic operations between arrays of **different shapes** without explicitly using loops.

Instead of manually iterating through elements, NumPy automatically **expands** the smaller array (or scalar) to match the shape of the larger array whenever possible.

This makes code simpler, faster, and more memory-efficient.

---

## Without Broadcasting

Using normal Python lists, we need a loop to apply an operation to every element.

### Example

```python
prices = [100, 200, 300, 400]
discount = 10  # percent

final_prices = []

for price in prices:
    final_price = price - (price * discount) / 100
    final_prices.append(final_price)

print(final_prices)
```

### Output

```python
[90.0, 180.0, 270.0, 360.0]
```

---

## Using Broadcasting

### Example

```python
import numpy as np

prices = np.array([100, 200, 300, 400])
discount = 10

final_prices = prices - (discount * prices) / 100

print(final_prices)
```

### Output

```python
[ 90. 180. 270. 360.]
```

### Description

The scalar value `10` is automatically applied to every element of the array. No loop is required.

---

# Broadcasting Rules

Broadcasting follows a few simple rules.

## Rule 1: Matching Shapes

Arrays with the same shape can be operated on element by element.

### Example

```python
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(arr1 + arr2)
```

### Output

```python
[5 7 9]
```

---

## Rule 2: Scalar Expansion

A single value (scalar) is automatically expanded to every element of the array.

### Example

```python
import numpy as np

arr = np.array([1,2,3])

print(arr + 10)
print(arr * 2)
```

### Output

```python
[11 12 13]
[2 4 6]
```

---

## Rule 3: Compatible Dimensions

A smaller array can be expanded to match a larger array if their dimensions are compatible.

### Example

```python
import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6]
])

vector = np.array([10,20,30])

print(matrix * vector)
```

### Output

```python
[[ 10  40  90]
 [ 40 100 180]]
```

### Description

The vector is automatically repeated for each row of the matrix before multiplication.

---

## Rule 4: Incompatible Shapes

If NumPy cannot match the shapes according to the broadcasting rules, it raises a **ValueError**.

### Example

```python
import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2])

print(arr1 + arr2)
```

### Output

```text
ValueError: operands could not be broadcast together with shapes (4,) (2,)
```

---

# Vectorization

Vectorization means performing an operation on an **entire NumPy array at once**, instead of processing one element at a time using loops.

NumPy performs these operations internally using optimized C code, making them much faster than Python loops.

---

## Without Vectorization

### Example

```python
list1 = [1,2,3]
list2 = [4,5,6]

result = [x + y for x, y in zip(list1, list2)]

print(result)
```

### Output

```python
[5, 7, 9]
```

---

## Using Vectorization

### Example

```python
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

result = arr1 + arr2

print(result)
```

### Output

```python
[5 7 9]
```

---

## Another Example

```python
import numpy as np

arr = np.array([10,20,30])

print(arr * 3)
```

### Output

```python
[30 60 90]
```

### Description

The multiplication is applied to every element automatically without writing a loop.

---

# Broadcasting vs Vectorization

Although these concepts are related, they are not the same.

| Broadcasting | Vectorization |
|--------------|---------------|
| Handles operations between arrays of different compatible shapes. | Performs operations on entire arrays without explicit loops. |
| Automatically expands smaller arrays when needed. | Uses optimized NumPy functions for high performance. |
| Example: `arr + 10` or `matrix * vector` | Example: `arr1 + arr2`, `arr * 5` |

> **Note:** Broadcasting is often used together with vectorization. Broadcasting first makes array shapes compatible, and then vectorized operations are applied.

---

# Advantages of Broadcasting and Vectorization

- Eliminates the need for explicit Python loops.
- Makes code shorter and easier to read.
- Improves performance significantly.
- Uses optimized NumPy implementations written in C.
- Works efficiently even with very large arrays.

---

# Quick Summary

| Concept | Example |
|----------|---------|
| Scalar Broadcasting | `arr + 10` |
| Array Broadcasting | `matrix * vector` |
| Vectorized Addition | `arr1 + arr2` |
| Vectorized Multiplication | `arr * 3` |
| Shape Mismatch | Raises `ValueError` |


---

# Handling Missing Values

Missing values are values that are **unknown, unavailable, or not recorded** in a dataset.

In NumPy, missing numerical values are represented using **`np.nan`** (Not a Number).

Handling missing values is an important preprocessing step because many mathematical operations and machine learning algorithms cannot work correctly with missing data.

---

# `np.nan`

`np.nan` is a special floating-point value that represents a missing or undefined numerical value.

### Syntax

```python
np.nan
```

### Example

```python
import numpy as np

arr = np.array([1, 2, np.nan, 4, 5, np.nan])

print(arr)
```

### Output

```python
[ 1.  2. nan  4.  5. nan]
```

### Description

Whenever an array contains `np.nan`, NumPy automatically converts the array to a floating-point datatype because `NaN` can only exist in floating-point arrays.

---

# Checking Missing Values

`np.isnan()` checks whether each element of an array is a missing value (`np.nan`).

It returns a Boolean array where:

- `True` → Element is `np.nan`
- `False` → Element is not `np.nan`

### Syntax

```python
np.isnan(array)
```

### Example

```python
import numpy as np

arr = np.array([1, 2, np.nan, 4, 5, np.nan])

print(np.isnan(arr))
```

### Output

```python
[False False  True False False  True]
```

### Description

This function is commonly used to identify missing values before cleaning or replacing them.

---

# Why Can't We Compare `np.nan`?

One of the most common interview questions is:

> **Why does `np.nan == np.nan` return `False`?**

### Example

```python
import numpy as np

print(np.nan == np.nan)
```

### Output

```python
False
```

### Explanation

According to the **IEEE 754 floating-point standard**, `NaN` is considered **not equal to any value**, including itself.

Therefore, **never use `==` to check for missing values**.

✅ Correct way:

```python
np.isnan(value)
```

---

# Replacing Missing Values

`np.nan_to_num()` replaces `np.nan` values with a specified number.

### Syntax

```python
np.nan_to_num(array, nan=value)
```

### Example

```python
import numpy as np

arr = np.array([1, 2, np.nan, 4, 5, np.nan])

cleaned_arr = np.nan_to_num(arr, nan=2)

print(cleaned_arr)
```

### Output

```python
[1. 2. 2. 4. 5. 2.]
```

### Description

All missing values (`np.nan`) are replaced with `2`.

> **Note:** If `nan` is not specified, NumPy replaces missing values with `0`.

---

# Infinite Values

Apart from missing values, NumPy also supports **positive** and **negative infinity**.

- `np.inf` → Positive infinity
- `-np.inf` → Negative infinity

These values may occur due to operations like:

- Division by zero
- Arithmetic overflow (e.g., numbers larger than the maximum representable value)

---

# Checking Infinite Values

`np.isinf()` checks whether each element is positive or negative infinity.

### Syntax

```python
np.isinf(array)
```

### Example

```python
import numpy as np

arr = np.array([1, 2, np.inf, 4, -np.inf, 6])

print(np.isinf(arr))
```

### Output

```python
[False False  True False  True False]
```

### Description

Returns `True` wherever an element is either `np.inf` or `-np.inf`.

---

# Replacing Infinite Values

`np.nan_to_num()` can also replace infinite values.

### Syntax

```python
np.nan_to_num(array, posinf=value, neginf=value)
```

### Example

```python
import numpy as np

arr = np.array([1, 2, np.inf, 4, -np.inf, 6])

cleaned_arr = np.nan_to_num(
    arr,
    posinf=999,
    neginf=-999
)

print(cleaned_arr)
```

### Output

```python
[   1.    2.  999.    4. -999.    6.]
```

### Description

- Positive infinity (`np.inf`) is replaced with `999`.
- Negative infinity (`-np.inf`) is replaced with `-999`.

---

# Quick Summary

| Function | Purpose |
|----------|---------|
| `np.nan` | Represents a missing value |
| `np.isnan()` | Checks for missing values |
| `np.nan_to_num()` | Replaces `np.nan` with a specified value |
| `np.inf` | Represents positive infinity |
| `-np.inf` | Represents negative infinity |
| `np.isinf()` | Checks for infinite values |

> **Interview Tip:** `np.nan == np.nan` returns **False** because, according to the IEEE 754 standard, **NaN is not equal to any value, including itself**. Always use `np.isnan()` to check for missing values.