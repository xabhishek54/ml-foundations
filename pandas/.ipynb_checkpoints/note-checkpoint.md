# Pandas Notes — Video 1: Introduction, Installation & Loading Data

**Source:** Corey Schafer's Python Pandas Tutorial series (Video #1)

---

## 1. What Pandas Is and Why It Matters

**Pandas** is a data analysis library for Python that lets you read, clean, transform, and analyze structured data (CSV, Excel, SQL, JSON, etc.) with far less code than native Python. Two things make it the default tool for data work:

- **Ease of use** — reading a CSV into a usable structure is one line (`pd.read_csv(...)`), versus manually handling file I/O and parsing with the built-in `csv` module.
- **Performance** — pandas is built on top of **NumPy**, so its core operations run as vectorized, compiled code rather than slow Python-level loops. This is *why* pandas scales to real datasets — keep this in mind for later videos when you see operations applied across entire columns at once instead of using `for` loops.

Think of pandas as the layer that sits between "raw file on disk" and "structured table you can query, filter, and compute on."

---

## 2. Installation

```bash
pip install pandas
pip install jupyterlab
```

- Corey uses a **virtual environment** here — not mandatory, but good practice so package versions don't clash across projects.
- **Jupyter** isn't required for pandas itself, but it's used throughout this series because it renders DataFrames as clean, scrollable HTML tables in the browser — much easier to eyeball your data than reading printed text in a terminal. You *can* follow along in any regular editor; you'll just use `print(df)` instead, and it'll look plainer.

To launch Jupyter from the terminal:

```bash
cd path/to/your/project/folder
jupyter notebook
```

**Important operational detail:** the terminal running this command is now acting as a local server. Jupyter runs *in the browser*, but the browser is just the interface — the actual Python process lives in that terminal window. Closing the terminal kills the server and you lose access to the notebook (though your saved `.ipynb` file itself persists).

---

## 3. The Dataset

The series uses the **Stack Overflow Developer Survey** (2019 data in this video) — real-world, messy, relatable data rather than a toy dataset. This is a deliberate pedagogical choice: real data has quirks (missing values, inconsistent types, long text fields) that toy datasets hide, and those quirks are exactly what you need practice handling.

After downloading and unzipping, the folder contains:

| File | Purpose |
|---|---|
| `survey_results_public.csv` | The actual data — **one row per respondent, one column per question/answer** |
| `survey_results_schema.csv` | A lookup table: maps each cryptic column name (e.g. `MainBranch`) to the full question text that was actually asked |
| `README` | Explains what the above files are |

**Why this matters conceptually:** this is a very common real-world pattern — a "data" file with short/coded column names, plus a separate "schema" or "data dictionary" file that decodes them. You'll hit this pattern constantly outside tutorials too (e.g. survey exports, government datasets, API responses with field codes).

Folder was organized as:
```
pandas_demo/
└── data/
    ├── survey_results_public.csv
    └── survey_results_schema.csv
```

---

## 4. Loading Data: `read_csv` and the DataFrame

```python
import pandas as pd

df = pd.read_csv('data/survey_results_public.csv')
```

- `pd` is the **universal convention** for the pandas import alias — always use it; every tutorial, StackOverflow answer, and codebase you'll ever see assumes `pd`.
- `pd.read_csv()` reads a CSV file directly into a **DataFrame** — pandas' core 2-dimensional data structure (rows × columns, like a spreadsheet or SQL table). This single call replaces manually opening a file, creating a `csv.reader`, and looping over rows to build your own structure.
- `df` is just a variable name (short for "DataFrame") — a convention, not a keyword.

**Key conceptual point for later:** the DataFrame is the backbone of the entire library. Almost everything else you'll learn in pandas (filtering, grouping, merging, cleaning) is really "operations you perform *on* a DataFrame." The next video digs into DataFrame vs. the 1-dimensional **Series** type, which is worth paying close attention to since a DataFrame is essentially a collection of Series objects sharing an index.

Load the schema file the same way, into a **separate** variable so it doesn't overwrite your main data:

```python
schema_df = pd.read_csv('data/survey_results_schema.csv')
```

---

## 5. Inspecting a DataFrame — Shape, Info, Display Options

### `.shape` (attribute, no parentheses)
```python
df.shape
```
Returns a tuple: `(number_of_rows, number_of_columns)`. This dataset: **88,883 rows × 85 columns**.

> Note the distinction: `.shape` is an **attribute** (a stored property, no `()`), while `.info()` and `.head()` below are **methods** (they *do* something, so they need `()`). Getting this distinction right early avoids a lot of confusing `TypeError`s later.

### `.info()` (method)
```python
df.info()
```
Gives you:
- Row count and column count (confirms `.shape`)
- **Every column name**
- The **data type (dtype)** of each column

Dtypes you'll see constantly:
- `object` → usually means **string** (text) data
- `int64` → integer
- `float64` → decimal number

This is one of the first things you should run on any new dataset — it tells you at a glance what you're working with and flags potential issues (e.g., a column you expect to be numeric showing up as `object` usually means there's messy/mixed data in it — something pandas handles more explicitly in later videos on data cleaning).

### Display options — seeing everything instead of truncated output
By default, Jupyter truncates wide/long DataFrames (e.g., only shows ~20 of 85 columns, with `...` in between). To see everything:

```python
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
```

This is a **global setting** for your session — it changes how *all* DataFrames print from that point on, not just one specific `df`. Useful to set near the top of a notebook once you know roughly how big your data is.

### `.head(n)` and `.tail(n)`
```python
df.head()      # first 5 rows (default)
df.head(10)    # first 10 rows
df.tail(10)    # last 10 rows
```
These are the methods you'll reach for constantly — not to analyze data, but as a **sanity check**: after applying a filter, sort, or transformation, `.head()` is how you quickly confirm "did that actually do what I expected?" without dumping the entire dataset to screen.

---

## 6. Using the Schema File to Decode Column Names

```python
schema_df
```

`schema_df` has (at least) two relevant columns: the coded **column name** (matching `df`'s columns) and the **full question text**. So instead of guessing what `df['Hobbyist']` means, you look it up in `schema_df` and see the actual survey question (e.g., "Do you code as a hobby?").

This is a preview of a more general and important workflow point: rather than scrolling manually to find one row, later videos cover **filtering DataFrames** (e.g., "grab the row where `column == 'Hobbyist'`") — a much more scalable way to look things up than eyeballing a printed table.

---

## Quick Reference — Code from This Video

```python
import pandas as pd

# Load data
df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')

# Explore shape/structure
df.shape                 # (rows, columns) tuple — attribute, no parens
df.info()                # row/col counts + dtypes — method, needs parens

# Show everything instead of truncated view
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# Peek at data without printing everything
df.head()                # first 5 rows
df.head(10)              # first 10 rows
df.tail(10)              # last 10 rows
```

---

## Things Worth Remembering Going Forward

1. **Attribute vs. method** distinction (`.shape` vs `.info()`) — this trips people up early and is worth internalizing now.
2. `object` dtype ≈ string, not literally "any Python object" in the everyday sense — this becomes more nuanced once you deal with mixed-type or messy columns later.
3. The "data file + schema file" pattern is common in the real world, not just this tutorial — get comfortable cross-referencing two tables.
4. `pd.set_option(...)` changes **display behavior only** — it doesn't alter your underlying data, just what gets printed. Easy to conflate the two when you're new.
5. Next video (per Corey): DataFrame vs. Series in depth, and how to select specific rows/columns — worth reviewing `.shape` and `.info()` output from this video again once that lands, since column selection builds directly on knowing what columns exist and what type each is.