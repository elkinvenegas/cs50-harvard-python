
# 🧮 CS50 Python – Week 1: Calculator ─ Basic Arithmetic and Data Types

## 📘 Overview
## 📖 Explanation
## 🚀 Technologies Used
## ⚙️ How to Run This Program
## 💻 Interact with the Program
## 🧠 What I Learned
## 📎 Resources

This project contains small Python programs that explore fundamental concepts of arithmetic, data types, and output formatting.

It's part of my learning journey through the Harvard [CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python/) course by Harvard University. The project includes examples of alternative ways to write equivalent expressions and highlights best practices for writing cleaner, more readable code.

---

## 📖 Explanation

In this exercise, we explored how to perform basic arithmetic operations ─ such as addition and division ─ using different data types. The code demonstrates the use of the `int()` and `float()` functions to cast user input into the appropriate numeric type. We also learned about the `round()` function for controlling decimal precision and used f-strings to format the final output in a clean, readable way.

---

## 🚀 Technologies Used

- **Python 3.11.9**
- **Visual Studio Code**
- **CS50 Library (used in the course structure, but not required in this script)**
- **Markdown (.md) for documentation**

---

## ⚙️ How to Run `calculator.py`

Follow these steps to run the `calculator.py` script:

1. **Clone the repository:**

```
git clone https://github.com/elkinvenegas/cs50-python-projects.git
```

2. Navigate into the project folder:

```
cd cs50-python-projects/week_1_functions  # or the folder where calculator.py is located
```

3. Run the script:

```
python calculator.py
```

ℹ️ If you're on **macOS** or **Linux**, and `python` doesn't work, try:

```
python3 calculator.py
```

4. 💻 **Interact with the Program**

The program prompts for two numbers and demonstrates arithmetic operations like addition or division, depending on the version of the code you're running:

- Integer and Float Arithmetic
- Rounding Results with `round()`
- Formatted Output Using f-strings

**Example Output**:

```
Without rounding (basic division):

What's x? 2
What's y? 3
0.6666666666666666

With rounding (using `round()` or formatted string):

What's x? 2
What's y? 3
0.67
```

---

## 🧠 What I Learned

✅ How to take user input with `input()` and convert it to integers or floats  
✅ The difference between `int` and `float` in arithmetic operations  
✅ How to format large numbers with commas (e.g., `1,000`) using `f"{value:,}"`  
✅ How to limit decimal places in division using `round()` and formatted strings like `f"{value:.2f}"`  

---

## 📎 Resources

- [CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python/)
- [View the Full Repository on GitHub](https://github.com/elkinvenegas/cs50-python-projects)
