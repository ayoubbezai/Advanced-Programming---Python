# 📚 TP2 – Python Built-In Data Types

**Course:** Advanced Programming – Python  
**Year:** 3rd Year Computer Security Engineering (2025/2026)

---

## 📖 Overview

This practical work explores Python's **built-in data types** and their operations through practical exercises:
- **data_types.py** - Basic type demonstrations
- **challenge.py** - Real dataset processing

---

## 🎯 Features

- ✅ Explore all Python built-in types (numeric, string, sequences, dictionaries, sets, binary, None)
- ✅ Understand mutability and immutability
- ✅ Type inspection with `type()` function
- ✅ Real-world dataset processing examples
- ✅ Clear console output with formatted results

---

## 📂 Project Structure

```
tp2/
├── data_types.py       # Basic data type exploration
├── challenge.py        # Advanced dataset processing
└── README.md           # This file
```

---

## 🚀 How to Run

```bash
# Run basic data types exploration
python data_types.py

# Run challenge exercise
python challenge.py
```

---

## 📋 Data Types Covered

| Category | Types | Example |
|----------|-------|---------|
| Numeric | `int`, `float`, `complex` | `3`, `3.5`, `3+2j` |
| Text | `str` | `"Artificial Intelligence"` |
| Boolean | `bool` | `True`, `False` |
| Sequences | `list`, `tuple` | `[1,2,3]`, `("a","b")` |
| Mapping | `dict` | `{"ML": 95, "DL": 90}` |
| Sets | `set`, `frozenset` | `{1,2,3}`, `frozenset([1,2])` |
| Binary | `bytes`, `bytearray` | `b"text"` |
| Special | `NoneType` | `None` |

---

## 💡 Example Output

**data_types.py:**
```
Part 1. Numeric, String, and Boolean Basics:
<class 'int'>
<class 'float'>
Ayoub ChatGPT

Part 2. Numeric, String, and Boolean Basics:
[1, 2, 3, 4, 5] <class 'list'>
('AI', 'ML', 'NLP') <class 'tuple'>
```

**challenge.py:**
```
=== Numeric, String & Boolean ===
Sum of a and b: 14.5
Is a greater than b? True

=== Lists & Tuples ===
Unique & sorted numbers: [3, 5, 7, 9]

=== Dictionaries ===
Average AI score: 90.0
```

---

## 🧠 Key Concepts

**Mutable vs Immutable:**
- Mutable: `list`, `dict`, `set`, `bytearray` (can be modified)
- Immutable: `tuple`, `str`, `frozenset`, `bytes` (cannot be changed)

**Type Inspection:**
```python
type(42)              # <class 'int'>
type([1, 2, 3])       # <class 'list'>
type({"a": 1})        # <class 'dict'>
```

**Type Conversion:**
```python
int(3.14)             # 3
str(42)               # '42'
list((1, 2, 3))       # [1, 2, 3]
```

---

## ✨ Key Concepts Covered

- Type system and type inspection
- Mutability and immutability
- Sequences (lists, tuples, strings)
- Collections (dictionaries, sets)
- Binary data handling
- Null values and None type
- Type conversions
- Data processing and transformations