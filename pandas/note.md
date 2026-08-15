# Pandas — Introduction, Setup & Loading Data

## 1. What Pandas Is

**Pandas** is a data analysis library for Python used to read, clean, transform, and analyze structured data — CSV, Excel, SQL, JSON, and similar formats. Two things make it the standard tool for this work:

- **Ease of use** — reading a CSV into a usable structure is one line (`pd.read_csv(...)`), versus manually opening the file and parsing it with the built-in `csv` module.
- **Performance** — pandas is built on top of **NumPy**, so its core operations run as vectorized, compiled code rather than slow Python-level loops. This is why pandas scales well to large datasets — operations get applied across entire columns at once instead of looping row by row in pure Python.

Conceptually, pandas sits between "raw file on disk" and "structured table you can query, filter, and compute on."

---

## 2. Installation & Environment

```bash
pip install pandas
pip install jupyterlab
```

Using a **virtual environment** is good practice so package versions don't clash across projects, though not strictly required.

**Jupyter** isn't required for pandas itself, but it's a common companion tool because it renders DataFrames as clean, scrollable HTML tables in the browser — much easier to read than plain terminal output. Without it, `print(df)` still works, just in plainer text.

To launch a notebook:

```bash
cd path/to/your/project/folder
jupyter notebook
```

**Operational detail:** the terminal running this command acts as a local server — Jupyter runs *in the browser*, but the actual Python process lives in that terminal window. Closing the terminal kills the server (though the saved `.ipynb` file itself persists).

---

## 3. Real-World Data Files: The "Data + Schema" Pattern

A very common structure for real-world datasets — surveys, government data exports, API dumps — is:

| File type | Purpose |
|---|---|
| **Main data file** | The actual records — one row per entry, one column per field, but column names are often short/coded (e.g. `MainBranch`, `Hobbyist`) |
| **Schema / data dictionary file** | Maps each coded column name to its full, human-readable meaning |
| **README** | Explains what the other files contain |

Recognizing this pattern is useful well beyond any one dataset — whenever column names look cryptic, check for an accompanying schema or dictionary file before assuming you have to guess.

Example folder layout:
```
project/
└── data/
    ├── survey_results_public.csv
    └── survey_results_schema.csv
```

---

## 4. Loading Data: `read_csv` and the DataFrame

```python
import pandas as pd

df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')
```

- `pd` is the **universal convention** for importing pandas — virtually all documentation, tutorials, and codebases assume it.
- `pd.read_csv()` reads a CSV file directly into a **DataFrame** — pandas' core 2-dimensional structure (rows × columns, like a spreadsheet or SQL table). This replaces manually opening a file and building your own row/column structure.
- `df` and `schema_df` are just variable names — load related-but-distinct files into **separate** variables so one doesn't overwrite the other.

**Conceptual anchor:** the DataFrame is the backbone of the library. Nearly everything else in pandas — filtering, grouping, merging, cleaning — is an operation performed *on* a DataFrame. A DataFrame is essentially a collection of 1-dimensional **Series** objects (one per column) sharing a common row index.

---

## 5. Inspecting a DataFrame

### `.shape` — attribute, no parentheses
```python
df.shape   # → (num_rows, num_columns)
```
Returns a tuple of row and column counts.

> **Attribute vs. method:** `.shape` is an **attribute** — a stored property, accessed without `()`. `.info()` and `.head()` below are **methods** — they perform an action, so they need `()`. Mixing these up is a common early source of `TypeError`s.

### `.info()` — method
```python
df.info()
```
Reports:
- Row and column counts
- Every column name
- The **data type (dtype)** of each column

Common dtypes:
- `object` → usually **string** (text) data
- `int64` → integer
- `float64` → decimal number

Running `.info()` on a new dataset immediately surfaces potential issues — e.g., a column expected to be numeric showing up as `object` usually signals messy or mixed data that needs cleaning.

### Display options
By default, wide or long DataFrames get truncated in output (e.g., 20 of 85 columns shown, with `...` in between). To see everything:

```python
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
```

This is a **global display setting** — it changes how *all* DataFrames print afterward, and affects only what's shown, not the underlying data itself.

### `.head(n)` and `.tail(n)`
```python
df.head()      # first 5 rows (default)
df.head(10)    # first 10 rows
df.tail(10)    # last 10 rows
```
These are used constantly as a **sanity check** — after filtering, sorting, or transforming data, `.head()` is the fast way to confirm the operation did what was expected, without printing the entire dataset.

---

## 6. Using a Schema File to Decode Column Names

```python
schema_df
```

A schema DataFrame typically has (at least) two relevant columns: the coded **column name** and the corresponding **full question/field text**. Instead of guessing what `df['Hobbyist']` means, look it up in `schema_df` to get the actual description (e.g., "Do you code as a hobby?").

This is a preview of a broader workflow: rather than scrolling manually to find one row, **filtering DataFrames** (e.g., "grab the row where `column == 'Hobbyist'`") is the scalable way to look things up.

---

## Quick Reference

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

## Key Takeaways

1. **Attribute vs. method** (`.shape` vs `.info()`) — internalize this distinction early; it prevents a common class of errors.
2. `object` dtype ≈ string, not literally "any Python object" — this becomes more nuanced with mixed-type or messy columns.
3. The **data file + schema file** pattern shows up constantly in real datasets — get comfortable cross-referencing two tables.
4. `pd.set_option(...)` affects **display only**, never the underlying data — easy to conflate the two.
5. A DataFrame is a collection of Series sharing an index — this framing matters once selecting specific rows/columns (via `.loc`, `.iloc`, or column indexing) comes into play.

# Pandas — DataFrame & Series

## DataFrame
A **DataFrame** is pandas' core 2D data structure — rows and columns, like a table. You can think of it as similar to a dictionary where each key is a column and each value is a list of that column's data (a row-index is added automatically).

```python
people = {
    "first": ["Abhishek", "Ram", "Shyam", "Mohit"],
    "last": ["Karn", "Magar", "Shah", "Awasthi"],
    "email": ["abhishek@gmail.com", "rammagar@gmail.com", "shyamah@yahoo.com", "hitashi@gmail.com"]
}

import pandas as pd
df = pd.DataFrame(people)
df
```
```
    first     last       email
0   Abhishek  Karn       abhishek@gmail.com
1   Ram       Magar      rammagar@gmail.com
2   Shyam     Shah       shyamah@yahoo.com
3   Mohit     Awasthi    hitashi@gmail.com
```

This gives a table with columns `first`, `last`, `email`, and a default numeric row index (`0, 1, 2, 3`).

## Series
A **Series** is a single column of data — 1-dimensional, with an index. A DataFrame is essentially a collection of Series objects sharing the same index.

```python
df['email']
```
```
0    abhishek@gmail.com
1    rammagar@gmail.com
2    shyamah@yahoo.com
3    hitashi@gmail.com
Name: email, dtype: str
```

```python
type(df['email'])
# pandas.Series

df.email              # dot notation — same result as df['email']
```
```
0    abhishek@gmail.com
1    rammagar@gmail.com
2    shyamah@yahoo.com
3    hitashi@gmail.com
Name: email, dtype: str
```

**Prefer bracket notation over dot notation.** If a column name matches an existing DataFrame method/attribute (e.g. a column literally named `count`), dot notation will hit the method instead of the column. Brackets always work.

## Selecting Columns

```python
df['email']                 # single column → Series
df[['last', 'email']]       # multiple columns → DataFrame (note the double brackets)
```
```
    last       email
0   Karn       abhishek@gmail.com
1   Magar      rammagar@gmail.com
2   Shah       shyamah@yahoo.com
3   Awasthi    hitashi@gmail.com
```

```python
df.columns                  # list all column names
# Index(['first', 'last', 'email'], dtype='str')
```

## Selecting Rows — `iloc` vs `loc`

- **`iloc`** — select by **integer position**
- **`loc`** — select by **label** (with default index, labels happen to be integers too, but this changes once you set a custom index)

```python
df.iloc[0]              # first row (by position) → Series
```
```
first    Abhishek
last     Karn
email    abhishek@gmail.com
Name: 0, dtype: str
```

```python
df.iloc[[0, 1], 0]       # rows at position 0 & 1, column at position 0
```
```
0    Abhishek
1    Ram
Name: first, dtype: str
```

```python
df.iloc[[0, 1], [1, 2]]  # rows at position 0 & 1, columns at position 1 & 2
```
```
    last     email
0   Karn     abhishek@gmail.com
1   Magar    rammagar@gmail.com
```

```python
df.loc[0]                            # row with label 0
```
```
first    Abhishek
last     Karn
email    abhishek@gmail.com
Name: 0, dtype: str
```

```python
df.loc[[0, 1], ['last', 'email']]    # rows 0 & 1, specific columns by name
```
```
    last     email
0   Karn     abhishek@gmail.com
1   Magar    rammagar@gmail.com
```

**Row + column together:** first argument = rows, second = columns.
- With `iloc`, both must be integers.
- With `loc`, columns can be passed by name (single string or list of strings).

## Slicing
Works like list slicing, but `loc` slicing is **inclusive of the end value** (unlike normal Python slicing) — done deliberately so ranges like "hobbyist through employment" don't require guessing the next column name.

```python
df.loc[0:2]                     # rows with labels 0 through 2, inclusive
df.loc[0:2, 'Hobbyist':'Employment']   # row slice + column slice
```

## Quick Reference

```python
import pandas as pd

df = pd.DataFrame(people)

df['email']                          # column → Series
df[['last', 'email']]                # multiple columns → DataFrame
df.columns                           # all column names

df.iloc[0]                           # row by position
df.iloc[[0, 1], [1, 2]]              # rows & cols by position

df.loc[0]                            # row by label
df.loc[[0, 1], ['last', 'email']]    # rows & cols by label
df.loc[0:2, 'ColA':'ColC']           # inclusive slicing
```

## Key Takeaways
1. DataFrame = 2D (rows + columns); Series = 1D (single column). A DataFrame is a container of Series.
2. Use brackets `df['col']`, not dot notation, to avoid clashes with method/attribute names.
3. `iloc` = integer position, `loc` = label — with a default index they behave similarly, but this diverges once a custom index is set.
4. `loc` slicing includes the end label; standard Python/`iloc` slicing does not.

# Pandas — Filtering (Boolean Indexing)

## The Core Idea
A filter condition on a DataFrame doesn't return matching rows directly — it returns a **Series of True/False values** (a boolean mask), one per row, indicating whether that row meets the condition.

```python
df['Pass'] == "Yes"
```
```
0     True
1    False
2     True
3     True
Name: Pass, dtype: bool
```

Applying this mask to the DataFrame returns only the `True` rows.

## Basic Filtering

```python
filt = (df['Pass'] == "Yes")
df[filt]              # works, but...
df.loc[filt]           # preferred
```

**Prefer `df.loc[filt]` over `df[filt]`** — `loc` lets you also select specific columns in the same call, and keeps the row/column selection pattern consistent with everything else you do with `loc`.

```python
df.loc[filt, 'first']
```
```
0    Abhishek
3    Mohit
Name: first, dtype: str
```

**Note:** `filter` is a built-in Python keyword — avoid naming your variable `filter`; use `filt` instead. Wrapping each condition in its own parentheses (even when not strictly required) makes multi-condition filters easier to read.

## AND / OR / NOT

Pandas doesn't use Python's `and`/`or` keywords for filters — it uses:
- `&` for **and**
- `|` for **or**
- `~` in front of a filter to **negate** it

```python
filt = (df['Pass'] == "Yes") & (df['Marks'] > 80)
df[filt]
```
```
    first     last     email                Pass  Marks
0   Abhishek  Karn     abhishek@gmail.com    Yes   97
3   Mohit     Awasthi  hitashi@gmail.com     Yes   86
```

```python
df.loc[~filt, 'first']    # everyone who did NOT meet the filter
```
```
1    Ram
2    Shyam
Name: first, dtype: str
```

## Real-World Filtering — Salary Example

```python
high_salary = (df['ConvertedComp'] > 70000)
df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]
```
```
             Country          LanguageWorkedWith                          ConvertedComp
Respondent
6            Canada           Java;R;SQL                                   366420.0
9            New Zealand      Bash/Shell/PowerShell;C#;HTML/CSS;...        95179.0
13           United States    Bash/Shell/PowerShell;HTML/CSS;...           90000.0
16           United Kingdom   Bash/Shell/PowerShell;C#;HTML/CSS;...        455352.0
...          ...              ...                                          ...
88879        Finland          Bash/Shell/PowerShell;C++;Python             82488.0
88882        Netherlands      C#;HTML/CSS;Java;JavaScript;PHP;Python       588012.0

22289 rows × 3 columns
```

## Filtering with a List of Values — `.isin()`

Instead of chaining many `==` / `|` conditions for multiple valid values, pass a list and use `.isin()`:

```python
countries = ['Nepal']
filt_country = df['Country'].isin(countries)
df.loc[filt_country, ["Country", "Student", "ConvertedComp"]]
```
```
            Country    Student           ConvertedComp
Respondent
508         Nepal      Yes, full-time    NaN
592         Nepal      No                NaN
984         Nepal      No                10000.0
1355        Nepal      No                3168.0
1783        Nepal      No                1692.0
...         ...        ...               ...
87568       Nepal      Yes, full-time    2640.0
88543       Nepal      No                NaN

237 rows × 3 columns
```

`countries` can hold as many values as needed — `isin()` scales to any list length without writing repeated `|` conditions.

## Filtering on Substrings — `.str.contains()`

Some columns store multiple values in one string (e.g. `LanguageWorkedWith` = `"Bash/Shell/PowerShell;C#;Python"`), so an exact `==` match won't work. Use `.str.contains()` instead:

```python
filt = df['LanguageWorkedWith'].str.contains('Python', na=False)
filt
```
```
Respondent
1        True
2        True
3       False
4        True
5        True
...
88377   False
88601   False
88802   False
88816   False
88863   False
Name: LanguageWorkedWith, Length: 88883, dtype: bool
```

```python
df.loc[filt, "LanguageWorkedWith"]
```

**`na=False` is required** — rows with `NaN` in that column would otherwise raise an error during the string comparison, since `.str` methods can't operate on a missing value. Setting `na=False` treats those rows as non-matches instead of erroring.

## Quick Reference

```python
import pandas as pd

# Basic boolean mask
filt = (df['Pass'] == "Yes")
df.loc[filt]
df.loc[filt, 'first']              # mask + column selection

# AND / OR / NOT
filt = (df['Pass'] == "Yes") & (df['Marks'] > 80)
filt = (df['last'] == "Doe") | (df['first'] == "John")
df.loc[~filt]                       # negate a filter

# Filter by list of valid values
countries = ['Nepal', 'India']
filt = df['Country'].isin(countries)
df.loc[filt]

# Filter by substring in a delimited column
filt = df['LanguageWorkedWith'].str.contains('Python', na=False)
df.loc[filt]
```

## Key Takeaways
1. A filter condition produces a **boolean Series (mask)**, not the filtered data itself — applying it via `[]` or `.loc[]` is what actually filters.
2. Use `&`, `|`, `~` — not `and`/`or`/`not` — for combining/negating filters, and wrap each condition in parentheses.
3. `df.loc[filt, cols]` is the preferred pattern — filters rows and selects columns in one call.
4. `.isin([...])` replaces long chains of `==`/`|` when checking against multiple valid values.
5. `.str.contains(value, na=False)` is essential for "does this string-based column contain X" checks — always set `na=False` (or otherwise handle `NaN`) to avoid errors on missing data.

# Pandas — Modifying Rows & Columns

## Renaming Columns

**Replace all column names** — assign a full list to `.columns` (order matters, must match length):
```python
df.columns = ["First Name", "Last Name", "EMAIL", "PASS", "MARK"]
```

**Transform all column names** — use a list comprehension or `.str` methods (applies the same operation to every name at once):
```python
df.columns = [x.upper() for x in df.columns]      # uppercase all
df.columns = df.columns.str.replace(' ', '_')      # spaces → underscores
df.columns = df.columns.str.lower()                 # lowercase all
```

**Rename only specific columns** — use `.rename()` with a dict (`{old_name: new_name}`):
```python
df.rename(columns={'first_name': 'first', 'last_name': 'last'}, inplace=True)
```

As with most pandas modification methods, `inplace=True` is required to persist the change — otherwise you just see a preview.

## Updating Values by Row/Column — `loc` and `at`

**Update an entire row:**
```python
df.loc[2] = ['John', 'Smith', 'johnsmith@email.com']
```

**Update specific columns of a row** (pass a list of column labels + matching values):
```python
df.loc[2, ['last', 'email']] = ['Karna', 'sitakarna@gmail.com']
```
```
   first  last   email                pass  mark
0  Abhishek  Karn  abhishek@gmail.com  Yes   97
1  Ram       Magar rammagar@gmail.com  No    30
2  Sita      Karna sitakarna@gmail.com Yes   50
3  Mohit     Awasthi hitashi@gmail.com Yes   86
```

**Update a single value** — `loc` works fine, or use `.at[]` (built specifically for single-value access/updates, possibly for performance):
```python
df.loc[2, 'first'] = 'Sita'
df.at[2, 'mark'] = 99
```

**Update values matching a filter:**
```python
filt = (df['pass'] == 'No')
df.loc[filt, ['pass', 'mark']] = ['Yes', 35]
```

### ⚠️ SettingWithCopyWarning — always use `loc`/`at` to set values
Chaining brackets to set a value — e.g. `df[filt]['last'] = 'Smith'` — can silently **fail to update the DataFrame** and throws a `SettingWithCopyWarning`. This happens because that pattern can return a temporary copy rather than a view of the original data, so the assignment lands on something that gets discarded.

```python
df[filt]['last'] = 'Smith'      # ❌ warning, may not actually update df
df.loc[filt, 'last'] = 'Smith'   # ✅ correct — always update this way
```
**Never ignore this warning** — verify your update actually took effect.

## Updating an Entire Column

Reassign the column to a transformed version of itself:
```python
df['first'] = df['first'].str.lower()
```
```
   first     last    email                 pass  mark
0  abhishek  Karn    abhishek@gmail.com    Yes   97
1  ram       Magar   rammagar@gmail.com    Yes   35
2  sita      Karna   sitakarna@gmail.com   Yes   99
3  mohit     Awasthi hitashi@gmail.com     Yes   86
```

## `apply`, `applymap`, `map`, `replace` — the Four Easily-Confused Methods

### `apply` — call a function on values (works on Series **and** DataFrame, but differently)

**On a Series** — applies the function to every value in that column:
```python
df['email'].apply(len)
```
```
0    18
1    18
2    19
3    17
Name: email, dtype: int64
```
```python
df['email'].apply(str.upper)
```
```
0    ABHISHEK@GMAIL.COM
1    RAMMAGAR@GMAIL.COM
2    SITAKARNA@GMAIL.COM
3    HITASHI@GMAIL.COM
Name: email, dtype: str
```
Lambda version, same idea:
```python
df['mark'] = df['mark'].apply(lambda x: x / 2)
```

**On a DataFrame** — applies the function to each **Series (column, by default)**, not each individual value:
```python
df.apply(len)          # default axis='rows' → length of each column (i.e. row count)
```
```
first    4
last     4
email    4
pass     4
mark     4
dtype: int64
```
```python
df.apply(len, axis='columns')     # length of each row instead
```
```
0    5
1    5
2    5
3    5
dtype: int64
```
Because it operates per-Series, functions used here should make sense on a Series — e.g. `min()`:
```python
df.apply(lambda x: x.min())
```
```
first    abhishek
last     Awasthi
...
```
For numeric data, this is where you'd apply statistical/aggregate operations (min, max, sum, or something like `np.sqrt`) across each column.

### `applymap` — apply a function to **every individual element** (DataFrame only, no Series equivalent)
```python
df.loc[:, "first":"email"].map(len)     # newer pandas uses .map for this now (applymap is being phased out)
```
```
   first  last  email
0  8      4     18
1  3      5     18
2  4      5     19
3  5      7     17
```
This is the "elementwise" behavior people often expect from plain `apply` on a DataFrame — use `applymap`/`.map()` when you want per-cell, not per-column, application.

### `map` — substitute values in a **Series only**, using a dict
```python
df['first'].map({'abhishek': 'Shyam', 'sita': 'geeta'})
```
```
0    Shyam
1    NaN
2    geeta
3    NaN
Name: first, dtype: str
```
**Caveat:** any value *not* in the dict gets converted to `NaN`. Only use `map` when you intend to replace *every* value (or are fine with unmatched ones becoming `NaN`).

### `replace` — same substitution idea as `map`, but **keeps unmatched values unchanged**
```python
df['first'] = df['first'].replace({'abhishek': 'Shyam', 'sita': 'geeta'})
```
```
   first  last    email                 pass  mark
0  Shyam  Karn    abhishek@gmail.com    Yes   48.5
1  ram    Magar   rammagar@gmail.com    Yes   17.5
...
```
Use `replace` instead of `map` whenever you only want to substitute *some* values and leave everything else as-is.

## Real-World Example — Renaming and Value Mapping

```python
df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)

df['Hobbyist'] = df['Hobbyist'].map({'Yes': True, 'No': False})
```
Since `Hobbyist` only ever contains `"Yes"`/`"No"`, `map` is safe here — there's nothing else that would fall through to `NaN`. If a column had a third possible value (e.g. "Not sure"), `replace` would be the safer choice to avoid losing that data.

## Quick Reference

```python
# Renaming columns
df.columns = [...]                                   # replace all
df.columns = [x.upper() for x in df.columns]          # transform all
df.columns = df.columns.str.replace(' ', '_')
df.rename(columns={'old': 'new'}, inplace=True)        # rename specific

# Setting values — always via loc/at
df.loc[row_label, 'col'] = value
df.loc[row_label, ['col1', 'col2']] = [val1, val2]
df.at[row_label, 'col'] = value
df.loc[filt, 'col'] = value                            # conditional update

# Updating an entire column
df['col'] = df['col'].str.lower()

# apply / applymap / map / replace
df['col'].apply(func)              # Series → function per value
df.apply(func)                     # DataFrame → function per column (axis='rows' default)
df.apply(func, axis='columns')     # DataFrame → function per row
df.applymap(func)                  # DataFrame → function per individual element
df['col'].map({'old': 'new'})       # Series substitution — unmatched → NaN
df['col'].replace({'old': 'new'})   # Series substitution — unmatched unchanged
```

## Key Takeaways
1. Most modification methods return a preview by default — always confirm the result, then set `inplace=True` (or reassign) to persist it.
2. **Never** set values via chained indexing (`df[filt]['col'] = x`) — it can silently fail. Always use `df.loc[filt, 'col'] = x` or `.at[]`.
3. `apply` behaves differently on a Series (per-value) vs. a DataFrame (per-column, or per-row with `axis='columns'`) — `applymap`/`.map()` on a DataFrame is what applies per individual cell.
4. `map` (on a Series) replaces unmatched values with `NaN`; `replace` leaves them untouched — pick based on whether you're substituting *all* values or just *some*.
5. `.at[]` is functionally similar to `.loc[]` for single-value access but may exist for performance reasons — `.loc[]` works fine in virtually all cases.

# Pandas — Adding & Removing Rows and Columns
*(Note: this topic has changed significantly in modern pandas — `.append()` was deprecated in 1.4 and removed in 2.0. Corrections below reflect current pandas.)*

## Adding a Column — Combine Existing Columns

```python
df['full_name'] = df['first'] + ' ' + df['last']
```
```
   first     last     email                Pass  Marks  full_name
0  Abhishek  Karn     abhishek@gmail.com    Yes   97     Abhishek Karn
1  Ram       Magar    rammagar@gmail.com    No    30     Ram Magar
2  Shyam     Shah     shyamah@yahoo.com     Yes   50     Shyam Shah
3  Mohit     Awasthi  hitashi@gmail.com     Yes   86     Mohit Awasthi
```

`+` on two string Series concatenates them element-wise. **Must use bracket notation** (`df['full_name'] = ...`) — dot notation (`df.full_name = ...`) would just set a Python attribute on the DataFrame object instead of creating a column.

You can also build a new column with `.apply()` (covered in the previous video's notes) for anything more complex than string concatenation — e.g. numeric calculations across columns.

## Removing Columns — `.drop()`

```python
df.drop(columns=['first', 'last'], inplace=True)
```
```
   email                Pass  Marks  full_name
0  abhishek@gmail.com    Yes   97     Abhishek Karn
1  rammagar@gmail.com    No    30     Ram Magar
2  shyamah@yahoo.com     Yes   50     Shyam Shah
3  hitashi@gmail.com     Yes   86     Mohit Awasthi
```

Returns a new DataFrame by default — `inplace=True` needed to persist, same pattern as every other modifying method.

## Splitting One Column Into Several

```python
df['full_name'].str.split(' ', expand=True)
```
```
   0         1
0  Abhishek  Karn
1  Ram       Magar
2  Shyam     Shah
3  Mohit     Awasthi
```
`expand=True` turns the resulting list-per-row into separate DataFrame columns instead of one column of lists.

Assign that result directly to new columns:
```python
df[['first', 'last']] = df['full_name'].str.split(' ', expand=True)
```
```
   email                Pass  Marks  full_name       first     last
0  abhishek@gmail.com    Yes   97     Abhishek Karn  Abhishek  Karn
1  rammagar@gmail.com    No    30     Ram Magar      Ram       Magar
2  shyamah@yahoo.com     Yes   50     Shyam Shah      Shyam     Shah
3  hitashi@gmail.com     Yes   86     Mohit Awasthi   Mohit     Awasthi
```

## Adding Rows — Modern Approach (`.append()` no longer exists)

The original video uses `df.append(...)`, which **was removed in pandas 2.0**. There are two current replacements:

### Option 1 — `pd.concat()` (general-purpose, works for one row or many)
A single dict must be wrapped in a **list** so pandas knows it's one row:
```python
pd.concat([df, pd.DataFrame([{'first': 'Dinesh', 'last': 'Thagunna'}])], ignore_index=True)
```
```
   email  Pass  Marks  full_name  first     last
0  abhishek@gmail.com  Yes  97.0  Abhishek Karn  Abhishek  Karn
1  rammagar@gmail.com  No   30.0  Ram Magar      Ram       Magar
2  shyamah@yahoo.com   Yes  50.0  Shyam Shah     Shyam     Shah
3  hitashi@gmail.com   Yes  86.0  Mohit Awasthi  Mohit     Awasthi
4  NaN                 NaN  NaN   NaN            Dinesh    Thagunna
```

For multiple new rows at once, build a list of dicts:
```python
new_rows = [{'email': 'nihari@gmail.com', 'Pass': 'Yes', 'Marks': 45.6}]
df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
```
```
   email               Pass  Marks  full_name      first  last
0  abhishek@gmail.com  Yes   97.0   Abhishek Karn  Abhishek  Karn
...
4  nihari@gmail.com    Yes   45.6   NaN            NaN       NaN
```
**Important:** `pd.concat()` doesn't have `inplace=True` — always reassign: `df = pd.concat([...])`.

To combine two full DataFrames (the video's `df.append(df2, ...)` case), the same pattern applies:
```python
df = pd.concat([df, df2], ignore_index=True, sort=False)
```

### Option 2 — `df.loc[len(df)] = {...}` (quick single-row add)
```python
df.loc[len(df)] = {'first': 'Dinesh', 'last': 'Thagunna'}
```
```
   email  Pass  Marks  full_name  first   last
0  abhishek@gmail.com  Yes  97.0  Abhishek Karn  Abhishek  Karn
...
4  NaN    NaN   NaN    NaN        Dinesh  Thagunna
```
`len(df)` gives the next available integer label, so this appends a new row at that index **in place** — no reassignment needed, unlike `pd.concat`. This is convenient for adding one row on the fly, but `pd.concat` is the better choice when adding many rows or combining DataFrames, since repeatedly growing a DataFrame row-by-row with `.loc` is inefficient at scale.

**`ignore_index=True` (for `concat`)** resets the row index to a clean `0, 1, 2, 3...` sequence rather than keeping conflicting/duplicate labels from the original pieces.

**`sort=False`** — relevant when the DataFrames being combined don't have identical column sets/order; without it, pandas may alphabetically sort the resulting columns. Only matters if column sets differ.

## Removing Rows — `.drop()`

**By index label:**
```python
df.drop(index=4, inplace=True)
```

**By condition** — pull the row labels from a filtered result:
```python
filt = df['Pass'] == 'No'
df.drop(index=df[filt].index, inplace=True)
```
```
   email               Pass  Marks  full_name      first     last
0  abhishek@gmail.com  Yes   97.0   Abhishek Karn  Abhishek  Karn
2  shyamah@yahoo.com   Yes   50.0   Shyam Shah     Shyam     Shah
3  hitashi@gmail.com   Yes   86.0   Mohit Awasthi  Mohit     Awasthi
4  NaN                 NaN   NaN    NaN            Dinesh    Thagunna
```
**Common mistake:** forgetting `inplace=True` (or reassignment) — `.drop()` returns a new DataFrame by default, so without persisting it, a subsequent print of `df` still shows the "removed" row.

## Quick Reference

```python
import pandas as pd

# Add column from existing columns
df['full_name'] = df['first'] + ' ' + df['last']

# Remove columns
df.drop(columns=['first', 'last'], inplace=True)

# Split a column into multiple new columns
df[['first', 'last']] = df['full_name'].str.split(' ', expand=True)

# Add a single row (in place)
df.loc[len(df)] = {'first': 'Dinesh', 'last': 'Thagunna'}

# Add one or many rows / combine DataFrames (must reassign — no inplace)
df = pd.concat([df, pd.DataFrame([{'first': 'Dinesh', 'last': 'Thagunna'}])], ignore_index=True)
df = pd.concat([df, df2], ignore_index=True, sort=False)

```

# Pandas — Sorting Data

## Sorting by a Single Column — `sort_values`

```python
df.sort_values(by='last')
```
```
   first     last     email                Pass  Marks
0  Abhishek  Karn     abhishek@gmail.com   Yes   97
1  Ram       Magar    rammagar@gmail.com   No    30
2  Shyam     Shah     shyamah@yahoo.com    Yes   50
3  Mohit     Awasthi  hitashi@gmail.com    Yes   86
```
Sorts alphabetically (strings) or numerically (numbers), ascending by default. (Reordered: Awasthi, Karn, Magar, Shah.)

```python
df.sort_values(by='last', ascending=False)   # descending
```
```
   first     last     email
2  Shyam     Shah     shyamah@yahoo.com
1  Ram       Magar    rammagar@gmail.com
0  Abhishek  Karn     abhishek@gmail.com
3  Mohit     Awasthi  hitashi@gmail.com
```

## Sorting by Multiple Columns

Pass a list to `by` — later columns act as tiebreakers for duplicate values in earlier ones:

```python
df.sort_values(by=['last', 'first'])
```
Sorts primarily by `last`; when `last` values are identical (e.g. two people both named "Doe"), sorts those tied rows by `first` (e.g. "Jane" before "John").

## Mixed Ascending/Descending Order

Pass a list to `ascending` that lines up positionally with the list passed to `by`:

```python
df.sort_values(by=['last', 'first'], ascending=[False, True])
```
```
   first  last     email
2  Shyam  Shah     shyamah@yahoo.com
1  Ram    Magar    rammagar@gmail.com
0  Abhishek Karn   abhishek@gmail.com
3  Mohit  Awasthi  hitashi@gmail.com
```
`last` sorts descending, `first` sorts ascending — each column gets its own direction independently.

As with other modifying methods, this returns a new DataFrame by default — add `inplace=True` to persist:
```python
df.sort_values(by=['last', 'first'], ascending=[False, True], inplace=True)
```

## Sorting the Index

To restore original row order after sorting values:
```python
df.sort_index(inplace=True)
```
```
   first     last     email
0  Abhishek  Karn     abhishek@gmail.com
1  Ram       Magar    rammagar@gmail.com
2  Shyam     Shah     shyamah@yahoo.com
3  Mohit     Awasthi  hitashi@gmail.com
```
Index is back to `0, 1, 2, 3` order, matching original insertion order.

## Sorting a Single Series

```python
df['last'].sort_values()
```
```
3    Awasthi
0    Karn
1    Magar
2    Shah
Name: last, dtype: str
```

## Real-World Example — Sorting Survey Data

Sort by country alphabetically:
```python
df.sort_values(by='Country', inplace=True)
df['Country'].head(50)
```
```
Respondent
26548    Afghanistan
5765     Afghanistan
...
19067    Albania
7830     Albania
Name: Country, Length: 50, dtype: str
```

Sort by country (ascending) but salary descending within each country:
```python
df.sort_values(by=['Country', 'ConvertedComp'], ascending=[True, False], inplace=True)
df[['Country', 'ConvertedComp']].head(50)
```
```
            Country       ConvertedComp
Respondent
26548       Afghanistan   50000.0
5765        Afghanistan   36000.0
...         ...           ...
19067       Albania       62000.0
7830        Albania       48000.0
```
**Reminder:** selecting multiple columns needs double brackets — `df[['Country', 'ConvertedComp']]`, not `df['Country', 'ConvertedComp']`.

This pattern is genuinely useful for spotting **outliers** — sorted data surfaces unusually high/low values immediately. Handling outliers more rigorously typically comes up later, in aggregation/grouping work.

## Getting Just the Largest/Smallest Values — `nlargest` / `nsmallest`

**On a Series** — returns just the value(s):
```python
df['ConvertedComp'].nlargest(10)
```
```
Respondent
25983    2000000.0
27354    2000000.0
33456    2000000.0
...
Name: ConvertedComp, dtype: float64
```

**On a DataFrame** — returns the full rows for those top/bottom N values in a given column:
```python
df.nlargest(10, 'ConvertedComp')
```
```
            Country          ConvertedComp   ...
Respondent
25983       United States    2000000.0       ...
27354       Germany          2000000.0       ...
```

```python
df.nsmallest(10, 'ConvertedComp')
```
```
            Country          ConvertedComp   ...
Respondent
1204        India            0.0             ...
5521        Nigeria          0.0             ...
```

`nlargest`/`nsmallest` on the full DataFrame is generally more useful than the Series version when you want surrounding context (other survey answers), not just the isolated salary figures.

## Quick Reference

```python
# Single column
df.sort_values(by='col')
df.sort_values(by='col', ascending=False)

# Multiple columns, same or mixed direction
df.sort_values(by=['col1', 'col2'])
df.sort_values(by=['col1', 'col2'], ascending=[False, True])

# Persist changes
df.sort_values(by='col', inplace=True)

# Restore original row order
df.sort_index(inplace=True)

# Sort a single Series
df['col'].sort_values()

# Top / bottom N values
df['col'].nlargest(10)         # Series → just the values
df.nlargest(10, 'col')         # DataFrame → full rows
df.nsmallest(10, 'col')
```

## Key Takeaways
1. `sort_values(by=[...], ascending=[...])` — the two lists line up **positionally**; each column can have its own sort direction.
2. Multi-column sort works as primary sort + tiebreaker(s), not independent sorts.
3. `nlargest`/`nsmallest` are more direct than sort + `head()`/`tail()` when you only need the top/bottom N rows.
4. Sorted output is a fast, practical way to spot outliers before deeper analysis — worth doing as an early sanity check on numeric columns.
5. Like other DataFrame-modifying methods, `sort_values()` and `sort_index()` return a new object by default — `inplace=True` needed to persist.


# Pandas — Aggregating & Grouping Data

## What Aggregation Means
An **aggregate function** takes multiple values and reduces them to a single result — mean, median, mode, sum, count, etc. This is the first real "statistics" step in the series — up to this point we've mostly reshaped/filtered data, not summarized it.

## Basic Aggregation — Single Column

```python
df['ConvertedComp'].median()
```
```
np.float64(57287.0)
```
Gives the median salary across the whole survey (~$57,287). `NaN` values are automatically ignored.

**Why median instead of mean?** The mean is heavily skewed by outliers — a handful of very high salaries pull the average up unrealistically. The median gives a more representative "typical" value. This becomes visible directly when comparing the two (see `.describe()` below): mean ≈ $127,000 vs. median ≈ $57,000 — a huge gap caused by a small number of extremely high earners.

## Aggregation Across the Whole DataFrame

```python
df.median(numeric_only=True)
```
```
CompTotal          62000.0
ConvertedComp       57287.0
WorkWeekHrs            40.0
CodeRevHrs               4.0
Age                     29.0
dtype: float64
```

**Note on modern pandas:** in current versions, `df.median()` alone will **raise an error** if the DataFrame contains non-numeric columns — you must explicitly pass `numeric_only=True` to restrict the calculation to numeric columns only. (Older pandas silently dropped non-numeric columns; this is no longer the default behavior.) The same applies to `.mean()`, `.sum()`, and similar aggregate methods run directly on a DataFrame.

## `.describe()` — Full Statistical Overview

```python
df.describe()
```
```
        CompTotal    ConvertedComp  WorkWeekHrs   CodeRevHrs   Age
count   5.594500e+04 5.582300e+04   64503.000000 49790.000000 79210.000000
mean    5.519014e+11 1.271107e+05   42.127197     5.084308     30.336699
std     7.331926e+13 2.841523e+05   37.287610     5.513931     9.178390
min     0.000000e+00 0.000000e+00   1.000000      0.000000     1.000000
25%     2.000000e+04 2.577750e+04   40.000000     2.000000     24.000000
50%     6.200000e+04 5.728700e+04   40.000000     4.000000     29.000000
75%     1.200000e+05 1.000000e+05   44.750000     6.000000     35.000000
max     1.000000e+16 2.000000e+06   4850.000000   99.000000    99.000000
```

Returns count, mean, standard deviation, min, the 25/50/75% quantiles, and max — for every numeric column at once. The `50%` row **is** the median (matches `.median()` above). Values shown in scientific notation (e.g. `5.728700e+04`) just mean "shift the decimal point that many places" — `5.72870e+04` = 57,287.

Can also be run on a single column: `df['ConvertedComp'].describe()` gives the same breakdown for just that Series.

**`count` here ≠ counting unique values** — it's the number of **non-missing (non-NaN)** rows for that column. In this dataset, `ConvertedComp` has ~55,800 non-null responses out of ~88,000 total rows — meaning roughly 30,000 people skipped the salary question. If you actually want a tally of how many times each *distinct value* occurs, that's `.value_counts()`, not `.count()`.

## `.value_counts()` — Counting Occurrences of Each Value

```python
df['Hobbyist'].value_counts()
```
```
Hobbyist
Yes    71257
No     17626
Name: count, dtype: int64
```

Useful for any categorical/text column — e.g. finding the most common answer to a survey question:
```python
df['SocialMedia'].value_counts()
```
Shows Reddit, YouTube, WhatsApp, etc. ranked by frequency, including some region-specific platforms (WeChat, VK, Weibo) that reflect the international spread of respondents.

**As percentages instead of raw counts** — pass `normalize=True`:
```python
df['SocialMedia'].value_counts(normalize=True)
```
```
Reddit                    0.169...
YouTube                   0.16...
...
I don't use social media  0.065777
LinkedIn                  0.053306
WeChat 微信                 0.007899
Snapchat                  0.007437
VK ВКонтáкте               0.007141
Weibo 新浪微博                 0.000663
Youku Tudou 优酷             0.000249
Hello                     0.000225
Name: proportion, dtype: float64
```
Each value is a proportion of the whole (multiply by 100 for a percentage). Note: in modern pandas, the resulting Series is named `proportion` (older pandas didn't label it this way).

## `groupby()` — Splitting Data Into Groups

The pandas documentation describes `groupby` as **split → apply → combine**: split the data into groups based on some key, apply a function to each group independently, then combine the results back into one structure.

```python
country_grp = df.groupby('Country')
country_grp
```
```
<pandas.api.typing.DataFrameGroupBy object at 0x...>
```
This returns a `DataFrameGroupBy` object — not a DataFrame itself. It's a container holding all rows split into buckets by unique `Country` value, waiting for you to tell it what function to apply.

### Inspecting a Single Group
```python
country_grp.get_group('Nepal')
```
Returns a full DataFrame containing only the rows where `Country == 'Nepal'` — conceptually equivalent to `df.loc[df['Country'] == 'Nepal']`, just retrieved through the group object instead of a fresh filter.

**Key distinction from filtering:** a plain filter (`df.loc[df['Country']=='Nepal']`) only gets you *one* country's data per filter you write. `groupby` splits the *entire* dataset into every country's group simultaneously, so a single function call afterward gives you results for **every** group at once — that's the real payoff.

## Applying a Function to Every Group

```python
country_grp['SocialMedia'].value_counts().head(50)
```
```
Country       SocialMedia
Afghanistan   Facebook               15
              YouTube                 9
              I don't use social media 6
              WhatsApp                4
              Instagram               1
              Twitter                 1
              LinkedIn                1
Albania       WhatsApp               18
              Facebook               16
              Instagram              13
              YouTube                10
              Twitter                 8
              LinkedIn                7
              Reddit                  6
              I don't use social media 4
              WeChat 微信               1
              Snapchat                1
Algeria       YouTube                42
              Facebook               41
              ...
```

This is a **multi-index Series** — the outer index is `Country`, the inner index is `SocialMedia`. (Multi-indexes are a topic of their own, not fully covered in this series — worth exploring separately if you work with grouped/pivoted data a lot.)

**Looking up one country's results:**
```python
country_grp['SocialMedia'].value_counts().loc['United States']
```
No need to re-filter — one `groupby` + one function call already computed results for every country; `.loc[]` just selects which slice to view.

**As percentages per group:**
```python
country_grp['SocialMedia'].value_counts(normalize=True).loc['United States']
```
```
SocialMedia
Reddit                    0.284346
Twitter                   0.173002
Facebook                  0.141874
YouTube                   0.122867
I don't use social media  0.092338
Instagram                 0.082410
LinkedIn                  0.050883
WhatsApp                  0.030380
Snapchat                  0.016263
WeChat 微信                  0.004639
VK ВКонтáкте                0.000449
Weibo 新浪微博                  0.000399
Hello                     0.000100
Youku Tudou 优酷              0.000050
Name: proportion, dtype: float64
```
Reddit is the top choice for ~28% of US respondents. Same pattern works for any country — e.g. China shows WeChat/Weibo dominating, Russia shows VK dominating, reflecting each region's actual platform landscape.

**Note on country naming:** some entries use official/full names rather than common short names — e.g. Russia appears as `"Russian Federation"` in this survey, not `"Russia"`. Searching the exact wrong string (`'Russia'`) raises a `KeyError`/`IndexError` since that label doesn't exist in the index — always check `df['Country'].unique()` or similar if a lookup unexpectedly fails.

## Standard Aggregates on Groups — median, mean, `.agg()`

```python
country_grp['ConvertedComp'].median()
```
```
Country
Afghanistan                    6222.0
Albania                       10818.0
Algeria                        7878.0
Andorra                       160931.0
Angola                          7764.0
...
Venezuela, Bolivarian Republic of...    6384.0
Viet Nam                       11892.0
Yemen                          11940.0
Zambia                          5040.0
Zimbabwe                       19200.0
Name: ConvertedComp, Length: 179, dtype: float64
```
Look up a specific country the same way as before: `.loc['Germany']`.

**Multiple aggregate functions at once — `.agg()`:**
```python
country_grp['ConvertedComp'].agg(['mean', 'median'])
```
```
              mean       median
Country
United States  ...        ...
India           ...        ...
...
```
Pass a list of function names (as strings) to get several statistics side by side in one call, instead of running each separately. Narrow to one country the usual way: `.loc['Canada']`.

## Running String Methods on a Group — Requires `.apply()`

Directly chaining `.str` onto a grouped column **fails**:
```python
country_grp['LanguageWorkedWith'].str.contains('Python').sum()
```
```
AttributeError: Cannot access attribute 'str' of 'SeriesGroupBy' objects, try using the apply method
```
This happens because grouping turns the column into a `SeriesGroupBy` object, not a plain Series — `.str` only exists on actual Series. The error message itself points to the fix: use `.apply()` with a function that receives **each group's Series individually**.

```python
country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
```
```
Country
Afghanistan     8
Albania        23
...
```
Here `x` inside the lambda is one country's `LanguageWorkedWith` Series — `.str.contains('Python').sum()` counts `True` values within that group. `.sum()` works on booleans because `True`/`False` are treated as `1`/`0`.

**Single-country equivalent (for comparison), using an ordinary filter:**
```python
filt = df['Country'] == 'India'
df[filt]['LanguageWorkedWith'].str.contains('Python').sum()
```
```
np.int64(3105)
```

## Worked Example — % of Respondents per Country Who Know Python

Goal: for each country, compute *(people who know Python) / (total respondents)* × 100.

**Step 1 — total respondents per country:**
```python
country_grp_respondents = df['Country'].value_counts()
```
```
Country
United States    20949
India              9061
Germany            5866
United Kingdom     5737
Canada             3395
...
Papua New Guinea      1
Saint Kitts and Nevis  1
Saint Vincent and the Grenadines  1
Sao Tome and Principe  1
Chad                   1
Name: count, Length: 179, dtype: int64
```

**Step 2 — respondents per country who know Python:**
```python
knowspython = country_grp['LanguageWorkedWith'].apply(lambda x: (x.str.contains('Python').sum()))
```

**Step 3 — combine both Series into one DataFrame with `pd.concat()`:**
```python
new_df = pd.concat([country_grp_respondents, knowspython], sort=False, axis='columns')
new_df
```
```
                count   LanguageWorkedWith
Country
United States   20949   10083
India            9061    3105
Germany          5866    2451
United Kingdom   5737    2384
Canada           3395    1558
...
Papua New Guinea    1       0
Saint Kitts and Nevis  1     0
Saint Vincent and the Grenadines  1  0
Sao Tome and Principe   1     1
Chad                    1     0

179 rows × 2 columns
```
`axis='columns'` tells `concat` to align the two Series **side by side** (matched on their shared `Country` index) rather than stacking them on top of each other, which is the default (`axis='rows'`/`axis=0`). `sort=False` avoids alphabetically resorting the result — matters here since column order/identity is meaningful.

**Step 4 — rename for clarity:**
```python
new_df.rename(columns={'count': 'Total-participants', 'LanguageWorkedWith': 'KnowsPython'}, inplace=True)
```
```
                Total-participants  KnowsPython
Country
United States   20949                10083
India            9061                 3105
Germany          5866                 2451
```

**Step 5 — calculate the percentage column:**
```python
new_df['Per%knows-python'] = (new_df['KnowsPython'] / new_df['Total-participants']) * 100
```
```
                Total-participants  KnowsPython  Per%knows-python
Country
United States   20949               10083        48.131176
India            9061                3105        34.267741
Germany          5866                2451        41.783157
United Kingdom   5737                2384        41.554820
Canada           3395                1558        45.891016
...
Papua New Guinea    1                  0           0.000000
Saint Kitts and Nevis  1               0           0.000000
Saint Vincent and the Grenadines  1    0           0.000000
Sao Tome and Principe   1              1         100.000000
Chad                    1              0           0.000000

179 rows × 3 columns
```

**Step 6 — sort by percentage:**
```python
new_df.sort_values(by='Per%knows-python', inplace=True, ascending=False)
new_df.head(30)
```
Countries with only 1–2 total respondents can show misleading 100% results (e.g. `Sao Tome and Principe` — 1 person, happened to know Python). Always sanity-check `Total-participants` alongside the percentage before drawing conclusions — small sample sizes are easy to misread as strong trends. Looking further down at countries with meaningful respondent counts (e.g. Uganda: 72 respondents, 65% know Python; United States: 20,949 respondents, 48% know Python) gives a more trustworthy picture.

**Look up a single country's stats directly:**
```python
new_df.loc['Japan']
```

### ⚠️ Watch for `RuntimeWarning: invalid value encountered in scalar divide`
This can appear when computing a percentage like `.sum() / x.count() * 100` inside a group `.apply()`, if any group ends up dividing by zero (e.g. a country with `NaN`-only or empty data for that column, where `.count()` returns 0). It's a **warning, not an error** — the calculation still runs, but the offending group returns `NaN` or `inf` for that value, which should be checked rather than ignored. It's usually safer to divide by the raw group size (`len(x)`) or a value you know is non-zero, and to inspect any group with 0 or missing data before trusting the output.

## Quick Reference

```python
import pandas as pd

# Single-column aggregates
df['col'].median()
df['col'].describe()

# Whole-DataFrame aggregates (numeric_only required in modern pandas)
df.median(numeric_only=True)
df.describe()

# Value frequency
df['col'].value_counts()
df['col'].value_counts(normalize=True)   # as proportions

# Grouping
grp = df.groupby('Country')
grp.get_group('Nepal')                    # one group as a DataFrame
grp['col'].value_counts()                 # per-group value counts (multi-index Series)
grp['col'].median()                       # per-group aggregate
grp['col'].agg(['mean', 'median'])        # multiple aggregates at once

# String methods on groups need .apply()
grp['col'].apply(lambda x: x.str.contains('value').sum())

# Combine two Series into one DataFrame (aligned on shared index)
new_df = pd.concat([series1, series2], axis='columns', sort=False)

# Rename, compute derived column, sort — all previously covered patterns
new_df.rename(columns={'old': 'new'}, inplace=True)
new_df['pct'] = (new_df['part'] / new_df['whole']) * 100
new_df.sort_values(by='pct', ascending=False, inplace=True)
```

## Key Takeaways
1. **Median over mean** for skewed real-world data like salaries — a few extreme outliers distort the mean much more than the median.
2. **`.count()` counts non-missing rows**, not occurrences of specific values — for frequency of distinct values, use `.value_counts()` instead.
3. **`groupby()` doesn't compute anything by itself** — it returns a `GroupBy` object; a function (`.median()`, `.value_counts()`, `.agg()`, `.apply()`) must be applied to actually get results, and that function runs independently on every group at once.
4. **`.str` and similar Series-only accessors don't work directly on a grouped column** — wrap the logic in `.apply(lambda x: ...)`, where `x` represents each group's Series individually.
5. **`pd.concat(..., axis='columns')`** is the right tool for combining two Series that share an index (e.g. two per-country stats) into one DataFrame — different from the default `axis='rows'`/`axis=0`, which stacks them vertically instead.
6. **Always check sample size (denominator) alongside a computed percentage/rate** — small groups can produce dramatic-looking but meaningless percentages (100% or 0% from n=1).
7. **Modern pandas is stricter about non-numeric data** in aggregate methods like `.median()`/`.mean()` called directly on a DataFrame — pass `numeric_only=True` explicitly, since older pandas used to do this implicitly.

# Pandas — Handling Missing Data & Casting Data Types

## Setting Up Sample Data With Missing Values

```python
import pandas as pd
import numpy as np

people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'],
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
    'email': [
        'CoreyMSchafer@gmail.com',
        'JaneDoe@email.com',
        'JohnDoe@email.com',
        None,
        'Anonymous@email.com',
        None,
        'NA'
    ],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}

df = pd.DataFrame(people)
```

Real-world data typically has missing values represented multiple inconsistent ways: an actual `np.nan`, a Python `None`, or **custom placeholder strings** like `'NA'` or `'Missing'` that someone used instead of a proper null. All of these need handling, but pandas only automatically recognizes `NaN`/`None` as missing — the string placeholders need to be converted explicitly.

## Standardizing Custom Missing Values

```python
df.replace(['NA', 'Missing'], np.nan, inplace=True)
df
```
```
   first   last     email                    age
0  Corey   Schafer  CoreyMSchafer@gmail.com  33
1  Jane    Doe      JaneDoe@email.com        55
2  John    Doe      JohnDoe@email.com        63
3  Chris   Schafer  NaN                      36
4  NaN     NaN      Anonymous@email.com      NaN
5  NaN     NaN      NaN                      NaN
6  NaN     NaN      NaN                      NaN
```
This replaces every occurrence of the strings `'NA'` and `'Missing'` throughout the entire DataFrame with a proper `np.nan`, so pandas' missing-value tools (`dropna`, `fillna`, `isna`, etc.) will actually recognize them.

**If loading from CSV instead of building a DataFrame manually**, this is handled more directly at load time — see the `na_values` section below, rather than replacing after the fact.

## Dropping Rows/Columns With Missing Values — `.dropna()`

### Default behavior — drop rows with *any* missing value
```python
df.dropna()
```
```
   first  last     email                    age
0  Corey  Schafer  CoreyMSchafer@gmail.com  33
1  Jane   Doe      JaneDoe@email.com        55
2  John   Doe      JohnDoe@email.com        63
```
Equivalent, written out explicitly with its default arguments:
```python
df.dropna(axis='index', how='any')
```

**Two arguments control this:**
- **`axis`** — `'index'` (default) drops **rows**; `'columns'` drops **columns** instead.
- **`how`** — `'any'` (default) drops if **any** value in that row/column is missing; `'all'` drops only if **every** value is missing.

### `how='all'` — only drop fully-empty rows
```python
df.dropna(axis='index', how='all')
```
```
   first  last     email                    age
0  Corey  Schafer  CoreyMSchafer@gmail.com  33
1  Jane   Doe      JaneDoe@email.com        55
2  John   Doe      JohnDoe@email.com        63
3  Chris  Schafer  NaN                      36
4  NaN    NaN      Anonymous@email.com      NaN
```
Keeps rows that have *some* data, even if partially missing — only drops rows (like index 5 and 6) where every single value is `NaN`.

### `axis='columns'` — drop columns instead of rows
```python
df.dropna(axis='columns', how='all')     # no columns fully empty → returns unchanged
df.dropna(axis='columns', how='any')     # any missing value anywhere in the column → drops it
```
With this sample data, `how='any'` on columns returns an **empty DataFrame** — because row 6 is entirely missing, every column has at least one `NaN`, so all columns get dropped under `how='any'`.

### `subset` — only check specific columns for missing values
```python
df.dropna(subset=['email'])
```
```
   first  last     email                    age
0  Corey  Schafer  CoreyMSchafer@gmail.com  33
1  Jane   Doe      JaneDoe@email.com        55
2  John   Doe      JohnDoe@email.com        63
4  NaN    NaN      Anonymous@email.com      NaN
```
Only rows missing an `email` get dropped — missing `first`/`last`/`age` values don't matter here. Useful when only certain fields are essential for your analysis.

**Multiple columns in `subset`** — combined with `how`:
```python
df.dropna(subset=['last', 'email'], how='all')
```
Drops a row only if **both** `last` and `email` are missing — a row missing just one of the two is kept. With a single-column `subset`, `how` doesn't matter (there's only one value being checked); it becomes meaningful once `subset` has multiple columns.

As with other modifying methods, `dropna()` returns a new DataFrame by default — `inplace=True` persists the change.

## Checking Missing Values Without Dropping — `.isna()`

```python
df.isna()
```
```
   first  last   email  age
0  False  False  False  False
1  False  False  False  False
2  False  False  False  False
3  False  False  True   False
4  True   True   False  True
5  True   True   True   True
6  True   True   True   True
```
Returns a boolean mask (same shape as `df`) — `True` wherever a value is missing. Useful for inspecting missingness patterns without actually removing or changing any data.

## Filling Missing Values — `.fillna()`

```python
df.fillna(0)
```
Replaces every `NaN` in the DataFrame with `0` (or any value/string you pass). Works for strings too — e.g. `df.fillna('MISSING')` — but is generally more useful for **numeric** data, where you might legitimately want missing values to count as zero (e.g. an ungraded assignment scored as 0).

**Caution:** filling with 0 changes the actual value used in later calculations (means, sums, etc.) — only do this when 0 is a genuinely correct substitute for "missing," not just a placeholder. For most analysis, leaving values as `NaN` (which most aggregate functions ignore automatically) is safer than filling arbitrarily.

Like other modifying methods, needs `inplace=True` to persist.

## Casting Data Types — `.astype()`

### Why this matters
```python
df.dtypes
```
```
first    str
last     str
email    str
age      str
dtype: object
```
Even though the `age` column *looks* numeric when printed, it's stored as strings (`object`/`str` dtype) — likely because it was loaded/created with mixed types. Trying to run numeric operations on it fails:
```python
df['age'].mean()
```
```
TypeError: can only concatenate str (not "int") to str
```

### Converting to numeric — watch out for `NaN`
```python
df['age'] = df['age'].astype(int)     # ❌ fails if NaN present
```
```
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
```
**Key gotcha:** `NaN` is internally a **float**, not an integer — a column containing any missing values *cannot* be cast to `int`, only to `float`. Two options when this happens:
1. Cast to `float` instead of `int` (keeps missing values as `NaN`).
2. Fill missing values first (e.g. with `fillna(0)`), *then* cast to `int` — only appropriate if 0 is a sensible substitute for missing data in that column.

```python
df['age'] = df['age'].astype(float)
df.dtypes
```
```
first     str
last      str
email     str
age    float64
dtype: object
```
```python
df['age'].mean()
```
```
np.float64(46.75)
```

**Casting an entire DataFrame at once** (only sensible when all columns share a target type):
```python
df.astype(float)
```

## Real-World Application — Custom NA Values When Loading a CSV

Rather than replacing placeholder strings *after* loading (as done above), pandas can treat them as missing **at load time**:
```python
na_vals = ['NA', 'Missing']
df = pd.read_csv('data/survey_results_public.csv', na_values=na_vals)
```
Any occurrence of those strings in the raw CSV gets converted straight to `NaN` on import — cleaner than a manual `.replace()` step afterward, and avoids accidentally missing a spot.

## Worked Example — Average Years of Coding Experience

Goal: compute the mean of the `YearsCode` column from the Stack Overflow survey data.

**First attempt — fails immediately:**
```python
df['YearsCode'].mean()
```
```
TypeError: can only concatenate str (not "int") to str
```
The column is stored as strings, same root issue as above.

**Second attempt — cast to float, still fails:**
```python
df['YearsCode'].astype(float)
```
```
ValueError: could not convert string to float: 'Less than 1 year'
```
Unlike the earlier example, this column isn't just numbers-as-strings plus `NaN` — some respondents selected **non-numeric text options** on the survey itself (`'Less than 1 year'`, `'More than 50 years'`), not just a formatting quirk.

**Diagnose what's actually in the column — `.unique()`:**
```python
df['YearsCode'].unique()
```
Lists every distinct value present, including the string options mixed in with numeric strings and `NaN`. Different from `.value_counts()` — `.unique()` just shows what values exist, without tallying how often each occurs; useful here because the goal is spotting anomalies, not frequency.

**Replace the string options with reasonable numeric stand-ins:**
```python
df['YearsCode'].replace('Less than 1 year', 0, inplace=True)
df['YearsCode'].replace('More than 50 years', 51, inplace=True)
```
- `'Less than 1 year'` → `0` (a fair approximation).
- `'More than 50 years'` → `51` (an arbitrary but reasonable stand-in — the exact number chosen has minimal impact on the overall average, since very few respondents likely fall in this bucket, but it's worth being aware that this is an approximation, not the true value).

**Now casting and computing works:**
```python
df['YearsCode'] = df['YearsCode'].astype(float)
df['YearsCode'].mean()      # ~11.5 years
df['YearsCode'].median()    # ~9 years
```

This example ties together several concepts from across the series: inspecting real column values with `.unique()` before assuming a clean cast will work, using `.replace()` to normalize inconsistent categorical/text values into numeric ones, and only then casting the dtype and running aggregates.

## Quick Reference

```python
import pandas as pd
import numpy as np

# Normalize custom missing-value placeholders
df.replace(['NA', 'Missing'], np.nan, inplace=True)

# Or, when loading from CSV directly:
df = pd.read_csv('file.csv', na_values=['NA', 'Missing'])

# Dropping missing data
df.dropna()                                  # drop rows with ANY missing value
df.dropna(how='all')                         # drop rows only if ALL values missing
df.dropna(axis='columns', how='all')         # same logic, but for columns
df.dropna(subset=['col1', 'col2'])           # only check specific columns
df.dropna(subset=['col1', 'col2'], how='all')# drop only if BOTH subset cols missing

# Inspecting missing values without dropping
df.isna()

# Filling missing values
df.fillna(0)

# Casting dtypes
df.dtypes                       # check current types
df['col'] = df['col'].astype(float)   # use float, not int, if NaN present
df.astype(float)                # cast whole DataFrame at once

# Diagnosing unexpected values before casting
df['col'].unique()              # see all distinct values, including anomalies
df['col'].replace('text value', numeric_value, inplace=True)
```

## Key Takeaways
1. Missing data shows up in more forms than just `NaN`/`None` — custom placeholder strings (`'NA'`, `'Missing'`, etc.) are common and must be explicitly converted before pandas' missing-value tools will recognize them.
2. `dropna()`'s two key arguments — `axis` (rows vs. columns) and `how` (`'any'` vs `'all'`) — combine with an optional `subset` to precisely control what counts as "droppable." Always reason through which combination matches your actual requirement rather than defaulting blindly.
3. **`NaN` is a float internally** — a column with missing values can only be cast to `float`, never directly to `int`. Fill missing values first if you truly need an integer column.
4. Before casting a column to a numeric type, check `.unique()` for stray non-numeric text — a `ValueError: could not convert string to float` almost always means there's a text value hiding among what looks like a numeric column.
5. When loading from CSV, `na_values=[...]` in `read_csv()` is cleaner than replacing placeholder strings after the fact — it standardizes missing values right at import.
6. Filling missing values with a specific number (`fillna(0)`) changes what your calculations actually compute — only do this when the fill value is a genuinely correct stand-in, not just a convenient placeholder.

# Pandas — Date/Time Data & Time Series

## Why This Needs Special Handling
Date columns loaded from CSV are read in as **plain strings** by default, not as actual date/time objects. This means date/time-specific methods (day of week, filtering by year, resampling, etc.) won't work until the column is explicitly converted.

```python
df = pd.read_csv('data/ETH_1h.csv')
df.loc[0, 'Date'].day_name()
```
```
AttributeError: 'str' object has no attribute 'day_name'
```
Confirms the column is just text — `day_name()` is a date/time method, not a string method.

## Converting a Column to Date/Time — `pd.to_datetime()`

```python
df['Date'] = pd.to_datetime(df['Date'])
```
If the date strings are in a **standard, recognizable format**, pandas can often infer it automatically. This dataset's format (`2020-03-13 08-PM`) is unusual enough that automatic parsing fails:
```
ValueError: Unknown string format
```

### Passing an Explicit Format String
When auto-detection fails, tell pandas exactly how to read the string using [Python's `strftime`/`strptime` format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) (worth bookmarking — nobody memorizes these):

```python
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
```
```
   Date                 Symbol  Open    High    Low     Close   Volume
0  2020-03-13 20:00:00  ETHUSD  124.85  133.62  121.58  131.08  4572833.65
1  2020-03-13 19:00:00  ETHUSD  131.08  135.10  130.97  132.83  5024822.86
...
499 2020-02-22 01:00:00  ETHUSD  129.67  133.10  127.53  128.71  4131472.70
```
Format code breakdown for this example: `%Y` = 4-digit year, `%m` = month, `%d` = day, `%I` = 12-hour clock hour, `%p` = AM/PM marker. `8-PM` correctly parsed into `20:00:00` (24-hour time).

Now date/time methods work:
```python
df.loc[0, 'Date'].day_name()
```
```
'Friday'
```

## Parsing Dates While Loading the CSV

Rather than converting after loading, you can parse dates **at read time** using `parse_dates` + a custom parser function, since a non-standard format still needs explicit instructions:

```python
from datetime import datetime

d_parser = lambda x: datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv('data/ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser)
```
`parse_dates` takes a list of column names to convert. `date_parser` receives each individual date **string** (not the whole column) and must return a parsed `datetime` — `datetime.strptime(x, format)` does the actual parsing here, using the same format codes as before.

**Note for modern pandas:** `date_parser` was **deprecated in pandas 2.0** and removed in later versions. The current recommended approach is:
```python
df = pd.read_csv('data/ETH_1h.csv', parse_dates=['Date'])
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
```
i.e., convert with `pd.to_datetime()` and an explicit `format=` after loading (as shown at the top) — this is now the standard, format-safe approach regardless of pandas version, so it's the one to default to.

## Running Date/Time Methods on an Entire Series — the `.dt` Accessor

Just like `.str` unlocks string methods on a whole Series, `.dt` unlocks date/time methods:

```python
df['Date'].dt.day_name()
```
```
0      Friday
1      Friday
2      Friday
3      Friday
4      Friday
       ...
495    Saturday
496    Saturday
497    Saturday
498    Saturday
499    Saturday
Name: Date, Length: 500, dtype: str
```

Store this as a new column for quick reference:
```python
df['Day'] = df['Date'].dt.day_name()
```
```
   Date                 Symbol  Open    High    Low     Close   Volume     Day
0  2020-03-13 20:00:00  ETHUSD  124.85  133.62  121.58  131.08  4572833.65  Friday
...
495 2020-02-22 05:00:00 ETHUSD  133.17  136.37  131.73  133.64  8433803.91  Saturday
```

## Min, Max, and Time Deltas

```python
df['Date'].min()
```
```
Timestamp('2020-02-22 01:00:00')
```
```python
df['Date'].max() - df['Date'].min()
```
```
Timedelta('20 days 19:00:00')
```
Subtracting two date/times produces a **`Timedelta`** — a duration object representing the span between them. Useful for quickly checking how much time a dataset actually covers.

## Filtering by Date

### Using string comparisons (before setting a date index)
```python
filt = df['Date'] >= '2020-02-25'
df.loc[filt]
```
```
   Date                 Symbol  Open    High    Low     Close   Volume     Day
0  2020-03-13 20:00:00  ETHUSD  124.85  133.62  121.58  131.08  4572833.65  Friday
...
424 2020-02-25 04:00:00  ETHUSD  113.60  115.03  110.22  112.22  5175382.39  Tuesday
...
428 2020-02-25 00:00:00  ETHUSD  114.19  116.29  109.29  111.62  1949263.30  Tuesday

429 rows × 8 columns
```
Pandas can compare an actual `Timestamp` column directly against a plain **string** like `'2020-02-25'` — it's smart enough to interpret the string as a date for comparison purposes. This also works with `pd.to_datetime('2020-02-25')` explicitly if preferred, and combining bounds with `&` works exactly like any other filter (e.g. `(df['Date'] >= '2019-01-01') & (df['Date'] < '2020-01-01')` for a full year range).

### Using a Date as the Index — Simpler Slicing
```python
df.set_index('Date', inplace=True)
df.index
```
```
DatetimeIndex(['2020-03-13 20:00:00', '2020-03-13 19:00:00',
               '2020-03-13 18:00:00', '2020-03-13 17:00:00',
               '2020-03-13 16:00:00', '2020-03-13 15:00:00',
               '2020-03-13 14:00:00', '2020-03-13 13:00:00',
               '2020-03-13 12:00:00', '2020-03-13 11:00:00',
               ...
               '2020-02-22 10:00:00', '2020-02-22 09:00:00', ...])
```
Once the index is a `DatetimeIndex`, filtering becomes much simpler — no explicit comparison needed:
```python
df['2019']              # all rows in year 2019 (if present in data)
```

**Sort the index first** for range slicing to work reliably (data may be loaded newest-first):
```python
df = df.sort_index()
```
```
                     Symbol  Open    High    Low     Close   Volume     Day
Date
2020-02-22 01:00:00  ETHUSD  129.67  133.10  127.53  128.71  4131472.70  Saturday
2020-02-22 02:00:00  ETHUSD  129.40  130.29  127.25  129.67  2277747.91  Saturday
...
2020-03-13 20:00:00  ETHUSD  124.85  133.62  121.58  131.08  4572833.65  Friday
```

**Slicing a date range** (inclusive on both ends, like `.loc` slicing seen in earlier notes):
```python
df.loc['2020-01':'2020-02']       # all of January through February 2020
```

**Combining a date-range slice with a column** — grab just one metric over a range:
```python
df.loc['2020-02-22', 'High'].max()
```
```
np.float64(141.07)
```
```python
df.loc['2020-02-22', 'High'].mean()
```
```
np.float64(134.03608695652176)
```
This is where a `DatetimeIndex` really pays off — filtering by date and selecting a column collapses into one `.loc[]` call, no separate boolean filter needed.

## Resampling — Changing the Time Frequency

Resampling regroups time-indexed data into a **different time interval** (e.g., hourly → daily), applying an aggregate function to each new bucket.

### Resampling a single column
```python
highs = df['High'].resample('D').max()
```
```
Date
2020-02-22    141.07
2020-02-23    126.95
2020-02-24    ...
...
2020-03-13    ...
Freq: D, Name: High, dtype: float64
```
`'D'` = daily. Other common offset codes (all documented in the [pandas date offset docs](https://pandas.pydata.org/docs/user_guide/timeseries.html#offset-aliases), also worth bookmarking):
- `'H'` — hourly
- `'W'` — weekly
- `'M'` — monthly
- `'Q'` — quarterly
- `'Y'` — yearly

Look up a specific resampled date directly:
```python
highs['2020-02-23']
```
```
np.float64(126.95)
```

### Plotting Resampled Data
```python
%matplotlib inline
highs.plot()
```
`%matplotlib inline` is a Jupyter-specific "magic command" that makes plots render directly in the notebook (requires `matplotlib` installed — `pip install matplotlib` if missing). `.plot()` on a Series produces a quick line chart — genuinely useful for spotting trends at a glance once data is resampled to a sensible granularity (daily highs are far more readable as a chart than 500 raw hourly rows).

### Resampling Multiple Columns at Once
Running `.resample()` directly on the whole DataFrame applies **one aggregate function uniformly** to every column:
```python
df.resample('W').mean()
```
```
            Open        High        Low         Close       Volume
Date
2020-02-23  123.334043  126.340426  120.935532  123.758298  5.593096e+06
2020-03-01  111.118631  113.422143  108.767202  111.005595  5.477565e+06
2020-03-08  126.343333  128.841012  123.768810  126.297917  5.566568e+06
2020-03-15  136.775128  139.774872  133.863846  136.865214  5.472674e+06
```
This works, but often **doesn't make analytical sense uniformly** — e.g. averaging `High`/`Low` loses the actual weekly high/low, and averaging `Volume` is less meaningful than summing total trades for the period.

**Different aggregate function per column — `.agg()` with a dict:**
```python
df.resample('W').agg({
    'Close': 'mean',
    'High': 'max',
    'Low': 'min',
    'Volume': 'sum'
})
```
```
            Close       High    Low     Volume
Date
2020-02-23  123.758298  141.07  106.65  2.628755e+08
2020-03-01  111.005595  131.56  101.30  9.202308e+08
2020-03-08  126.297917  147.80  112.52  9.351834e+08
2020-03-15  136.865214  157.64  119.23  6.403028e+08
```
Dict keys = column names, values = the aggregate function to apply to that specific column — mean close price, actual weekly high/low, and total weekly volume, each computed with the function that's actually appropriate for it. This is the same `.agg()` pattern seen with `groupby()` in the previous video, applied here to time-based resampling instead of category-based grouping.

## Dropping Unneeded Columns (Recap With a Twist)
```python
df.dtypes
```
```
Symbol     str
Open       float64
High       float64
Low        float64
Close      float64
Volume     float64
Day        str
dtype: object
```
```python
df.drop(['Symbol', 'Day'], axis=1, inplace=True)
```
**Note:** `axis=1` here is equivalent to `axis='columns'` (seen in earlier notes) — pandas accepts both the integer and the string form; `1` means columns, `0` means rows (`index`). Either style works, but the string form (`axis='columns'`) is generally considered more readable/self-documenting.

## Quick Reference

```python
import pandas as pd
from datetime import datetime

# Converting to date/time
df['Date'] = pd.to_datetime(df['Date'])                          # auto-detect format
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p') # explicit format

# Parsing at load time (modern approach)
df = pd.read_csv('file.csv', parse_dates=['Date'])
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')

# .dt accessor for date methods on a whole Series
df['Date'].dt.day_name()
df['Day'] = df['Date'].dt.day_name()

# Min / max / duration
df['Date'].min()
df['Date'].max() - df['Date'].min()     # → Timedelta

# Filtering by date (before setting index)
filt = df['Date'] >= '2020-02-25'
df.loc[filt]

# Set date as index for simpler slicing
df.set_index('Date', inplace=True)
df = df.sort_index()                     # important before range slicing
df.loc['2020-01':'2020-02']              # inclusive date-range slice
df.loc['2020-02-22', 'High'].max()       # date + column together

# Resampling
df['High'].resample('D').max()           # single column, one function
df.resample('W').mean()                  # whole df, one function for all columns
df.resample('W').agg({                   # whole df, different function per column
    'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'
})

# Plotting (Jupyter)
%matplotlib inline
series.plot()
```

## Key Takeaways
1. Dates from CSV load as **plain strings** by default — always verify with `.dtypes` or by trying a `.dt` method before assuming date functionality will work.
2. When `pd.to_datetime()` can't auto-parse a format, pass `format=` with explicit `strftime` codes — this is more reliable than hoping pandas guesses correctly, and works identically whether converting after load or combined with `parse_dates` during load.
3. `date_parser` in `read_csv()` is **deprecated/removed** in modern pandas — convert with `pd.to_datetime(..., format=...)` after loading instead; this is now the standard approach across versions.
4. `.dt` is to date/time Series what `.str` is to string Series — the accessor needed to run per-value date methods across an entire column at once.
5. Setting the date column as the **index** (and sorting it) unlocks much simpler filtering/slicing syntax (`df.loc['2020-02']`) compared to manual boolean comparisons — worth doing whenever timestamps are unique per row.
6. **Resampling** changes the time granularity of the data (e.g. hourly → daily/weekly) and requires an aggregate function to decide how each new bucket's values are computed — use `.agg({col: func})` when different columns need different aggregation logic (mean price, but max high, min low, summed volume).
7. `axis=1`/`axis='columns'` and `axis=0`/`axis='index'` are interchangeable — the string form is generally clearer to read.