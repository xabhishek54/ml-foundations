# NumPy Problem Set – Indexing, Slicing & Reshaping

## Topics Covered

- Indexing
- Negative Indexing
- Slicing
- Fancy Indexing
- Boolean Masking (Filtering)
- Reshaping Arrays
- Flattening Arrays (`ravel()` and `flatten()`)

---

# Level 1 – Indexing & Slicing

## Problem 1 – Accessing Elements

**Topics:** Indexing, Negative Indexing

Given:

```python
arr = np.array([12, 25, 38, 41, 56, 63, 74, 89])
```

Perform the following:

- Print the first element.
- Print the fourth element.
- Print the last element.
- Print the second last element.
- Print the element at index 5.

---

## Problem 2 – Slicing Practice

**Topics:** Slicing

Using the same array:

```python
arr = np.array([12, 25, 38, 41, 56, 63, 74, 89])
```

Print:

- The first four elements.
- Elements from index 2 to index 6.
- The last three elements.
- Every second element.
- Every third element.
- The array in reverse order.

---

## Problem 3 – Slice Prediction

**Topics:** Slicing

Without running the code, predict the output of:

```python
arr = np.arange(1,16)

print(arr[2:10:2])
print(arr[::-1])
print(arr[-5:])
print(arr[:-4])
```

After predicting, run the code and verify your answers.

---

# Level 2 – Fancy Indexing

## Problem 4 – Selecting Custom Elements

**Topics:** Fancy Indexing

Given:

```python
arr = np.array([15, 22, 37, 41, 58, 64, 79, 83, 95])
```

Using only fancy indexing:

- Extract the first, fourth and last elements.
- Extract indices `[2, 3, 5, 7]`.
- Rearrange the array into the order:

```text
95 15 58 37
```

without changing the original array.

---

## Problem 5 – Matrix Indexing

**Topics:** Indexing

Given:

```python
matrix = np.array([
    [12, 23, 34],
    [45, 56, 67],
    [78, 89, 90]
])
```

Print:

- 56
- 90
- Entire second row
- Entire first column
- Last row
- Last column

---

# Level 3 – Boolean Masking

## Problem 6 – Number Filtering

**Topics:** Boolean Masking

Create an array from **1 to 100**.

Find:

- Numbers divisible by 2
- Numbers divisible by 5
- Numbers divisible by both 2 and 5
- Numbers greater than 70
- Numbers between 25 and 50 (inclusive)

Do not use loops.

---

## Problem 7 – Cleaning Invalid Data

**Topics:** Boolean Masking

Given:

```python
data = np.array([45, -10, 78, -3, 23, 91, -15, 60])
```

Tasks:

- Extract only the valid values.
- Replace all negative values with 0.
- Find the mean of the cleaned data.
- Find the maximum value.
- Count how many values are greater than 50.

---

## Problem 8 – Student Scores

**Topics:** Boolean Masking

Given:

```python
scores = np.array([45, 62, 77, 81, 39, 55, 91, 68, 49, 84])
```

Find:

- All passing scores (≥ 50)
- All distinction scores (≥ 80)
- Number of failing students
- Average of passing students only

---

# Level 4 – Reshaping Arrays

## Problem 9 – Basic Reshaping

**Topics:** Reshaping

Create an array from **1 to 24**.

Perform the following:

- Reshape into a 4 × 6 matrix.
- Print its shape.
- Print its size.
- Print its dimensions.

---

## Problem 10 – Multiple Reshapes

**Topics:** Reshaping

Create:

```python
arr = np.arange(1, 37)
```

Reshape it into:

- 6 × 6
- 9 × 4
- 3 × 12
- 2 × 18

Observe how the data remains the same but the structure changes.

---

## Problem 11 – Automatic Dimension

**Topics:** Reshaping

Create:

```python
arr = np.arange(1, 49)
```

Use `-1` to reshape the array into:

- 6 rows
- 8 columns
- 3 rows
- 12 columns

Do not manually calculate the missing dimension.

---

# Level 5 – Flattening

## Problem 12 – Flatten Practice

**Topics:** Flattening

Given:

```python
matrix = np.array([
    [2,4,6],
    [8,10,12],
    [14,16,18]
])
```

Perform:

- Flatten using `.ravel()`
- Flatten using `.flatten()`
- Print both arrays.

---

## Problem 13 – View vs Copy

**Topics:** Flattening (`ravel()` vs `flatten()`)

Create:

```python
matrix = np.array([
    [1,2],
    [3,4]
])
```

Create:

```python
view = matrix.ravel()
copy = matrix.flatten()
```

Then:

- Change the first element of `view` to `100`.
- Print `matrix`.
- Print `view`.
- Print `copy`.

Now:

- Change the second element of `copy` to `999`.
- Print all three again.

Write one sentence explaining why the outputs differ.

---

# Level 6 – Mixed Challenge

## Problem 14 – Employee Dataset

**Topics Covered:**
- Boolean Masking
- Fancy Indexing
- Reshaping
- Flattening

Generate **60 random employee salaries** between **20,000 and 100,000**.

Tasks:

- Reshape into a 12 × 5 matrix.
- Find all salaries greater than 75,000.
- Print the salaries of employees at indices `[2, 8, 15, 24, 40]`.
- Flatten the matrix.
- Reverse the flattened array.
- Count employees earning below 40,000.

---

## Problem 15 – Final Challenge

**Topics Covered:**
- Indexing
- Slicing
- Fancy Indexing
- Boolean Masking
- Reshaping
- Flattening

Create:

```python
arr = np.arange(1,101)
```

Perform all of the following:

1. Reshape into a 10 × 10 matrix.
2. Print the fifth row.
3. Print the third column.
4. Extract all numbers divisible by 7.
5. Reverse the flattened array.
6. Select rows 2–5.
7. Select columns 4–8.
8. Using fancy indexing, print rows `[0, 3, 7]`.
9. Count how many values are greater than 80.
10. Compute the average of all values divisible by 5.

---

# Bonus Challenge

## Matrix Puzzle

**Topics Covered:**
- Reshaping
- Flattening
- Slicing

Create this matrix:

```text
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
```

Without creating a new array manually:

- Convert it into a 1D array.
- Reverse it.
- Reshape it into a 2 × 6 matrix.
- Reverse the columns only.
- Flatten it again.

---

# Rules

- Use NumPy whenever possible.
- Do **not** use Python loops unless explicitly required.
- Write clean, readable code with comments where appropriate.
- Try to solve each problem without searching for the solution first.