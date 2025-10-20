# 🧮 TP1 – Area and Perimeter Calculator

**Course:** Advanced Programming – Python  
**Year:** 3rd Year Computer Security Engineering (2025/2026)

---

## 📘 Overview

This project calculates the **area and perimeter** of three geometric shapes:
- Circle
- Rectangle  
- Square

The project is implemented in **two versions**:
- **Part A:** Procedural approach using functions and dictionaries
- **Part B:** Object-oriented approach using classes and inheritance

---

## 🎯 Features

- ✅ User input validation (positive numbers only)
- ✅ Multiple calculations in a loop until user exits
- ✅ Automatic file storage in `results.txt`
- ✅ Clear, formatted console output
- ✅ OOP design with Shape base class and specialized subclasses

---

## 📂 Project Structure

```
tp1/
├── part_a_procedural.py    # Functions, dictionaries, file handling
├── part_b_oop.py           # Classes, inheritance, polymorphism
├── results.txt             # Auto-generated results file
└── README.md               # This file
```

---

## 🧮 Formulas

| Shape | Area | Perimeter |
|-------|------|-----------|
| Circle | A = πr² | C = 2πr |
| Rectangle | A = L × W | P = 2(L + W) |
| Square | A = s² | P = 4s |

---

## 🚀 How to Run

```bash
# Part A (Procedural)
python part_a_procedural.py

# Part B (OOP)
python part_b_oop.py
```

---

## 💡 Example Usage

```
📐 Welcome to the Shape Calculator!
You can calculate the area and perimeter of a circle, rectangle, or square.
Type 'exit' anytime to quit.

Enter shape name (circle / rectangle / square) or 'exit': circle
Enter the radius: 5

✅ Calculation Result:
   ➤ Shape: Circle (radius = 5.0)
   ➤ Area: 78.53981633974483
   ➤ Perimeter: 31.41592653589793

💾 Result saved to 'results.txt'.
```

---

## 📝 Results File Format

Results are appended to `results.txt`:

```
Shape: Circle (radius=5.0), Area: 78.53981633974483, Perimeter: 31.41592653589793
Shape: Rectangle (width=4.0, length=6.0), Area: 24.0, Perimeter: 20.0
Shape: Square (side=3.0), Area: 9.0, Perimeter: 12.0
```

---

## 🏗️ OOP Design (Part B)

| Class | Purpose |
|-------|---------|
| `Shape` | Base class with `area()`, `perimeter()`, `__str__()` |
| `Circle` | Inherits Shape, takes radius |
| `Rectangle` | Inherits Shape, takes length & width |
| `Square` | Inherits Rectangle, takes single side value |

All classes override `__str__()` for readable output.

---

## ✨ Key Concepts Covered

- Functions & Modularity
- Control Flow (match/if statements)
- Loops & User Interaction
- Dictionaries & Data Structures
- File I/O (append mode)
- Object-Oriented Programming
- Inheritance & Polymorphism
- Input Validation & Error Handling