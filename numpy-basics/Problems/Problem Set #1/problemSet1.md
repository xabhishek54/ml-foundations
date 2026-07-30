# NumPy Problem Set (Foundation)

## Level 1 – Core Concepts

### Problem 1 – Even–Odd Split

Create an array from **1 to 50**.

Tasks:
- Extract all even numbers.
- Extract all odd numbers.
- Compute the **mean** of even numbers.
- Compute the **sum** of odd numbers.

**Constraint:** Do not use loops.

---

### Problem 2 – Reshape Challenge

Create an array from **1 to 24**.

Tasks:
- Reshape it into a **4 × 6** matrix.
- Print:
  - Shape
  - Total number of elements
  - Number of dimensions
- Multiply the entire matrix by **3**.

---

### Problem 3 – Identity Matrix

Create a **5 × 5** identity matrix.

Tasks:
- Convert it to integer type.
- Replace all diagonal values with **9**.
- Keep all other values as **0**.

Expected Output:

```text
[[9 0 0 0 0]
 [0 9 0 0 0]
 [0 0 9 0 0]
 [0 0 0 9 0]
 [0 0 0 0 9]]
```

---

# Level 2 – Matrix Thinking

### Problem 4 – Student Marks Analysis

Given:

```python
marks = np.array([
    [78, 85, 90, 88, 92],
    [66, 74, 80, 70, 68],
    [90, 92, 94, 96, 98],
    [50, 60, 65, 58, 62]
])
```

Tasks:
- Calculate the total marks of each student.
- Calculate the average marks of each student.
- Find the index of the highest-scoring student.
- Calculate the average marks for each subject.
- Calculate the overall class average.

---

### Problem 5 – Temperature Analysis

Generate **30 random temperatures** between **15 and 40**.

Tasks:
- Find the mean temperature.
- Find the standard deviation.
- Find the hottest day.
- Find the coldest day.
- Count how many temperatures are greater than **30**.

**Constraint:** No loops.

---

# Level 3 – NumPy Thinking

### Problem 6 – Broadcasting

Create:

```python
A = np.array([10, 20, 30])

B = np.array([
    [1],
    [2],
    [3]
])
```

Tasks:
- Add `A` and `B`.
- Print the result.
- Explain why the resulting shape is what it is.

---

### Problem 7 – Data Cleaning

Given:

```python
data = np.array([10, 20, -5, 30, -2, 40, -1])
```

Negative values are invalid.

Tasks:
- Replace all negative values with **0**.
- Compute the mean of the cleaned data.
- Compute the variance of the cleaned data.

---

### Problem 8 – Mini Data Analyst Challenge

Generate **100 random integers** between **0 and 100**.

Tasks:
- Calculate the percentage of values greater than **75**.
- Calculate the percentage of values less than **25**.
- Find the median **without using `np.median()`**.
- Sort the array.

---

# Level 4 – Challenge Problems

### Problem 9 – Matrix Pattern

Create the following matrix using NumPy:

```text
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
```

Tasks:
- Reshape it into **5 × 4**.
- Flatten it into a 1D array.
- Reverse the flattened array.

---

### Problem 10 – Salary Dataset

Generate salaries for **200 employees**.

Requirements:
- Random integers between **20,000** and **100,000**.

Tasks:
- Find the average salary.
- Find the top 10 highest salaries.
- Find the bottom 10 lowest salaries.
- Count how many employees earn above the average salary.
- Calculate the standard deviation.
- Briefly explain what a high standard deviation means in the context of salaries.

---

# Bonus Challenge

Without using loops, create the following matrix:

```text
[[1 1 1 1 1 1]
 [0 0 0 0 0 0]
 [1 1 1 1 1 1]
 [0 0 0 0 0 0]
 [1 1 1 1 1 1]
 [0 0 0 0 0 0]]
```

---

## Rules

- Prefer NumPy functions over Python loops.
- Write clean and readable code.
- Comment your logic where necessary.
- Try solving each problem without looking up the solution first.