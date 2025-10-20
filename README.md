# Advanced Programming - Python

**Course:** Advanced Programming – Python  
**Year:** 3rd Year Computer Security Engineering (2025/2026)  
**Institution:** Faculty of Mathematics and Computer Science, Batna 2

---

## Overview

This course teaches Python fundamentals and object-oriented programming through practical exercises. Students progress from procedural programming with functions to complete OOP design, learning data types, algorithms, and professional coding practices.

---

## Project Structure

```
advanced-python/
├── tp1_shape_calculator/
│   ├── part_a_procedural.py
│   ├── part_b_oop.py
│   └── README.md
│
├── tp2_data_types/
│   ├── data_types.py
│   ├── challenge.py
│   └── README.md
│
├── tp3_functions_classes/
│   ├── tp3_functions_classes.py
│   └── README.md
│
└── README.md
```

---

## Practical Work Details

### TP1 – Area and Perimeter Calculator

**Topics:** I/O operations, functions, dictionaries, classes, inheritance, polymorphism

**Part A - Procedural Approach:**
- User input validation
- Functions for calculations and data handling
- Dictionary-based storage
- File I/O with results.txt

**Part B - Object-Oriented Approach:**
- Base Shape class
- Subclasses: Circle, Rectangle, Square
- Method overriding and inheritance
- Polymorphic design

**Supported Shapes:** Circle, Rectangle, Square

Run:
```bash
python tp1_shape_calculator/part_a_procedural.py
python tp1_shape_calculator/part_b_oop.py
```

---

### TP2 – Python Built-In Data Types

**Topics:** Type system, mutability, data structures, real-world data processing

**Data Types Covered:**
- Numeric: int, float, complex
- Text: str, bool
- Sequences: list, tuple
- Mapping: dict
- Sets: set, frozenset
- Binary: bytes, bytearray
- Special: None

**Exercises:**
- Type inspection and conversion
- Mutable vs immutable behavior
- Sequence and dictionary operations
- Set operations and uniqueness
- Binary data handling
- Real dataset processing in challenge.py

Run:
```bash
python tp2_data_types/data_types.py
python tp2_data_types/challenge.py
```

---

### TP3 – Functions and Classes

**Topics:** Functions, closures, lambda expressions, OOP, inheritance, polymorphism

**10 Exercises:**

1. Basic functions: `power()`, `sum_of_powers()`
2. Lambda & map/filter: `celsius_to_fahrenheit()`
3. Closures: `multiplier(n)`
4. Simple class: `Student` with attributes
5. Methods & behavior: `Student.update_grade()`
6. Parent/child classes: `Person`, `Teacher`
7. Method overriding: `work()` in different classes
8. Shared interface: `Dog`, `Cat`, `Bird` with `speak()`
9. Polymorphism: `Shape`, `Circle`, `Rectangle` with `area()`
10. School management system: Complete OOP hierarchy

Run:
```bash
python tp3_functions_classes/tp3_functions_classes.py
```

---

## How to Run

```bash
# TP1 - Shape Calculator
python tp1_shape_calculator/part_a_procedural.py
python tp1_shape_calculator/part_b_oop.py

# TP2 - Data Types
python tp2_data_types/data_types.py
python tp2_data_types/challenge.py

# TP3 - Functions and Classes
python tp3_functions_classes/tp3_functions_classes.py
```

---

## Requirements

- Python 3.10+

---

## Key Concepts

- **Functions & Modularity:** Writing reusable, organized code
- **Data Structures:** Lists, dictionaries, sets for different use cases
- **Control Flow:** if/elif/else, loops, logical operations
- **Object-Oriented Programming:** Classes, inheritance, polymorphism
- **Type System:** Understanding and using Python's built-in types
- **File I/O:** Reading and writing data
- **Functional Programming:** Lambda, map, filter, closures
- **Error Handling:** Input validation and exception management
- **Type Hints & Documentation:** Professional code standards

---

## Learning Progression

TP1 → TP2 → TP3

From procedural functions to complete object-oriented systems, with focus on data structures and design patterns.