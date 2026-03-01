# 🐍 PR. 4 — Functional Treat
### 📊 Data Analyzer & Transformer Program

> 🎓 *Red & White Skill Education — "Quality is our Motto."*

---

## 🌟 What Is This Project?

**Functional Treat** is a fully interactive, menu-driven Python console program that lets you **analyze and transform numerical data** in a fun and structured way! 🎉

You load in a list of numbers and the program becomes your personal data scientist — summarizing stats, filtering values, sorting, calculating factorials, and more, all through a clean terminal menu. Every feature is designed to showcase a specific Python function concept, making it both a **practical tool** and a **learning showcase** rolled into one. 🧠✨

Whether you're a beginner learning Python functions or a developer brushing up on core concepts, **Functional Treat** walks you through the most important function features Python has to offer — all in one place!

---

## 🎯 Project Objectives

- ✅ Build a **menu-driven console interface** for user interaction
- ✅ Demonstrate **built-in functions** like `len()`, `sum()`, `min()`, `max()`
- ✅ Create **User-Defined Functions (UDFs)** with `__doc__` documentation strings
- ✅ Use **`*args`** and **`**kwargs`** for flexible function parameters
- ✅ Implement **function recursion** to calculate factorials
- ✅ Apply **lambda (anonymous) functions** with `filter()` and `map()`
- ✅ Utilize the **`global` keyword** to share data across functions
- ✅ **Return multiple values** from a single function
- ✅ Sort data using both **`sort()`** (in-place) and **`sorted()`** (new list)

---

## 🛠️ Tech Stack

| 🔧 Tool | Details |
|--------|---------|
| 🐍 Language | Python 3.10+ |
| 💻 Interface | Terminal / Console |
| 📦 Libraries | None — pure Python! |

---

## 🚀 How to Run

**1. Make sure Python 3.10 or higher is installed:**
```bash
python --version
```

**2. Run the program:**
```bash
python functional_treat.py
```

**3. Follow the on-screen menu and start exploring your data! 🎮**

---

## 🗂️ File Structure

```
📁 PR4-Functional-Treat/
│
├── 🐍 functional_treat.py     ← Main Python program
└── 📄 README.md               ← You're reading it!
```

---

## 🖥️ Program Walkthrough

### 🏠 The Main Menu

When you launch the program, you're greeted with a welcome message and a numbered menu listing all available operations. Each option maps directly to a Python concept being demonstrated. The menu loops continuously until you choose to exit — so you can explore as many options as you like in one session!

```
-------------------- Main Menu --------------------
1. Input Data
2. Display Data Summary       (Built-In Functions)
3. Calculate Factorial        (Recursion)
4. Filter Data by Threshold   (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
```
<img width="1062" height="290" alt="Screenshot Main Menu" src="https://github.com/user-attachments/assets/6934b73a-bc81-490f-bca2-27aac39df375" />


### 1️⃣ Option 1 — Input Data 📥

This is your **starting point** every session! Option 1 uses the **`global` keyword** so the array you enter is accessible to every other function in the program without needing to pass it around manually.

You simply type your numbers separated by spaces and hit Enter — the program converts them into a proper Python list and confirms the data was saved successfully. 🙌

**Concepts used:** `global` keyword, `list()`, `map()`, `int()`, `split()`

```python
def array():
    """This Function takes 1D array input separated by spaces."""
    global arr
    arr = list(map(int, input("Enter data for a 1D array (separated by spaces):\n").split()))
    print("Your data added successfully...")
```

![screenshot1_input](https://github.com/user-attachments/assets/224a2999-191b-44f3-b8bb-83e3823b9bd2)


### 2️⃣ Option 2 — Display Data Summary 📋

Once your data is loaded, option 2 gives you an instant **statistical snapshot** of your array using Python's most powerful **built-in functions**. No manual calculations needed — Python does all the heavy lifting!

It shows you:
- 🔢 **Total elements** — how many numbers you entered `(len())`
- ⬇️ **Minimum value** — the smallest number in the list `(min())`
- ⬆️ **Maximum value** — the largest number in the list `(max())`
- ➕ **Sum of all values** — total added together `(sum())`
- 📊 **Average value** — mean of the dataset `(sum() / len())`

**Concepts used:** `len()`, `min()`, `max()`, `sum()`, UDF with `__doc__`

```python
def summary():
    """Display Dataset Summary using Built-In functions."""
    print(f"-Total Elements: {len(arr)}")
    print(f"-Minimum value: {min(arr)}")
    print(f"-Maximum value: {max(arr)}")
    print(f"-Sum of all values: {sum(arr)}")
    print(f"-Average of values: {sum(arr)/len(arr)}")
```

![screenshot2_summary](https://github.com/user-attachments/assets/dabdc8c8-1f65-45f2-9b03-04fe5afac4cd)


---

### 3️⃣ Option 3 — Calculate Factorial 🔁

This option is a beautiful demonstration of **recursion** — a function that calls *itself* to solve a problem! 🤯

You enter any non-negative integer and the function recursively multiplies its way down to 1. For example:

```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

The recursive function keeps breaking the problem into smaller pieces (`n * factorial(n-1)`) until it hits the **base case** (`n == 0` or `n == 1`), then unwinds and delivers the answer.

**Concepts used:** Recursion, base case, function arguments, `__doc__`

```python
def factorial(n):
    """Recursive function to calculate factorial using given argument."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

![screenshot3_factorial](https://github.com/user-attachments/assets/37788941-ad5f-4ea3-865b-f2e925692ce4)


---

### 4️⃣ Option 4 — Filter Data by Threshold 🔍

Option 4 puts **lambda functions** in the spotlight! You enter a threshold number and the program uses a one-line anonymous function combined with Python's `filter()` to extract only the values that meet your criteria.

Think of it like a bouncer at a club — only numbers **greater than or equal to your threshold** get through! 🚪

For example, with threshold `50` and data `[29, 17, 93, 74, 30, 81, 42, 51]`:
```
Filtered Data (Values >= 50): [93, 74, 81, 51]
```

**Concepts used:** Lambda functions, `filter()`, conditional expressions

```python
def threshold():
    """Filters data using lambda function."""
    n = int(input("\nEnter a threshold value to filter out data above this value: "))
    filtered = list(filter(lambda x: x > n, arr))
    print(f"Filtered Data (Values >= {n}): \n{filtered}")
```

![screenshot4_filter](https://github.com/user-attachments/assets/bb8488d1-17cb-4eca-8436-b7f7e88c0f6c)


### 5️⃣ Option 5 — Sort Data 🔃

Sorting in Python has an important distinction between two approaches — and this option demonstrates **both**!

- 🔼 **Ascending** → Uses `.sort()` on a copy — modifies the list **in place**, returns `None`
- 🔽 **Descending** → Uses `sorted()` — **returns a brand new sorted list**, original stays untouched

This difference matters a lot in real projects — seeing them side-by-side makes the concept crystal clear! 💡

**Concepts used:** `.sort()` (in-place), `sorted()` (returns new list), method vs function

```python
# Ascending — .sort() modifies in place
a_sort = arr.copy()
a_sort.sort()

# Descending — sorted() returns a new list
d_sort = sorted(arr, reverse=True)
```

ASCENDING SORT:

![screenshot5_sort](https://github.com/user-attachments/assets/e5a236fd-8566-4d1a-9543-6405c99bf99b)


DESCENDING SORTED:

<img width="1020" height="497" alt="Screenshot Sorted" src="https://github.com/user-attachments/assets/229e736f-d23d-4323-a394-814866e43415" />


---

### 6️⃣ Option 6 — Display Dataset Statistics 📈

This option showcases one of Python's coolest features — **returning multiple values from a single function**! 🎁

The `data_statistic()` function computes four different stats and returns them all at once as a tuple. The calling code then **unpacks** all four values in one clean line:

```python
minimum, maximum, total, average = data_statistic()
```

The results are then printed in a neat labeled format — a great example of how Python functions can do a lot of work and hand back everything you need in one shot!

**Concepts used:** Return multiple values, tuple unpacking, UDF with `__doc__`

```python
def data_statistic():
    """Returns multiple statistics values."""
    maximum = max(arr)
    minimum = min(arr)
    total = sum(arr)
    average = total / len(arr)
    return minimum, maximum, total, average
```

![screenshot6_stats](https://github.com/user-attachments/assets/ebe11cc2-d013-4528-a203-3bb38e9891ff)


---

### 7️⃣ Option 7 — Exit Program 👋

When you're done exploring, option 7 gracefully breaks the `while True` loop and prints a friendly goodbye message. Clean, polite, and professional! 😊

![screenshot7_exit](https://github.com/user-attachments/assets/74e6979d-255c-4c2f-81d7-e446b04ff801)

---

## 🧠 Python Concepts Quick Reference

| 💡 Concept | 📍 Where It's Used | 🔑 Key Syntax |
|-----------|-------------------|--------------|
| 🌐 Global Keyword | `array()` function | `global arr` |
| 📚 Built-in Functions | `summary()` | `len()`, `sum()`, `min()`, `max()` |
| 📝 `__doc__` Strings | Every function | `"""description"""` |
| 🔁 Recursion | `factorial(n)` | `return n * factorial(n-1)` |
| ⚡ Lambda + filter() | `threshold()` | `filter(lambda x: x > n, arr)` |
| 🔃 In-place Sort | Option 5 Ascending | `.sort()` |
| 🔄 New List Sort | Option 5 Descending | `sorted(arr, reverse=True)` |
| 🎁 Multiple Return | `data_statistic()` | `return a, b, c, d` |
| 📦 Tuple Unpacking | `display_stat()` | `min, max, total, avg = func()` |

---

## ⚠️ Things to Know

- 🔴 Always **run Option 1 first** — all other options depend on the data being loaded
- 🟡 The sorting sub-menu labels both options as `"1."` — it's a display quirk; enter `2` for descending
- 🟢 Factorial correctly handles `0! = 1` and `1! = 1` through the recursive base case

---

## 👤 Author

Rensee Gajipara Aspiring Python Developer on a mission to master the fundamentals — building the foundation to become unstoppable.

