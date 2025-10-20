# 🧮 TP3 – Functions and Classes

**Course:** Advanced Programming – Python  
**Year:** 3rd Year Computer Security Engineering (2025/2026)

---

## 📖 Overview

This practical work explores Python **functions**, **closures**, **lambda expressions**, and **object-oriented programming** through 10 hands-on exercises covering classes, inheritance, and polymorphism.

---

## 🎯 Features

- ✅ Basic and higher-order functions
- ✅ Lambda, map, and filter operations
- ✅ Closures and function factories
- ✅ Class design with attributes and methods
- ✅ Inheritance and method overriding
- ✅ Polymorphism with shared interfaces
- ✅ OOP school management system

---

## 📂 Project Structure

```
tp3/
├── tp3_functions_classes.py    # All 10 exercises implemented
└── README.md                    # This file
```

---

## 🚀 How to Run

```bash
# Run main demonstrations
python tp3_functions_classes.py
```

---

## 📋 Exercises Overview

| # | Concept | Key Functions/Classes |
|---|---------|----------------------|
| 1 | Basic Functions | `power()`, `sum_of_powers()` |
| 2 | Lambda & map/filter | `celsius_to_fahrenheit()` |
| 3 | Closures | `multiplier()` |
| 4 | Simple Class | `Student` with attributes |
| 5 | Methods & Behavior | `Student.update_grade()` |
| 6 | Parent/Child Classes | `Person`, `Teacher` |
| 7 | Method Overriding | `Person.work()`, `Teacher.work()` |
| 8 | Shared Interface | `Dog`, `Cat`, `Bird` with `speak()` |
| 9 | Polymorphism | `Shape`, `Circle`, `Rectangle` with `area()` |
| 10 | School Management | `introduce_all()` with polymorphism |

---

## 💡 Example Usage

**Exercise 1: Basic Functions**
```python
>>> power(2, 3)
8
>>> sum_of_powers([1, 2, 3], 2)
14  # 1^2 + 2^2 + 3^2
```

**Exercise 2: Lambda & map**
```python
>>> celsius_to_fahrenheit([0, 100])
[32.0, 212.0]
```

**Exercise 3: Closure**
```python
>>> double = multiplier(2)
>>> double(5)
10
```

**Exercise 4 & 5: Student Class**
```python
>>> s = Student("Alice", 16, 88.5)
>>> s.display_info()
Name: Alice, Age: 16, Grade: 88.5
>>> s.update_grade(92.0)
Alice's grade updated from 88.5 to 92.0
```

**Exercise 6 & 7: Inheritance**
```python
>>> t = Teacher("Mr. Bob", 40, "Math")
>>> t.introduce()
Hello, I am Mr. Bob, 40 years old, and I teach Math.
>>> t.work()
Teaching students...
```

**Exercise 8: Shared Interface**
```python
>>> Dog().speak()
Woof!
>>> Cat().speak()
Meow!
>>> Bird().speak()
Chirp!
```

**Exercise 9: Polymorphism**
```python
>>> shapes = [Circle(5), Rectangle(4, 6)]
>>> print_shapes_area(shapes)
Circle area: 78.53981633974483
Rectangle area: 24
```

**Exercise 10: School Management System**
```python
>>> school = [Student("Alice", 16, 88.5), Teacher("Mr. Bob", 40, "Math")]
>>> introduce_all(school)
Hello, I am Alice, 16 years old, and my grade is 88.5.
Hello, I am Mr. Bob, 40 years old, and I teach Math.
```

---

## 🧠 Key Concepts

- **Functions** - Modular, reusable code blocks
- **Higher-order Functions** - Functions that take/return other functions
- **Lambda** - Anonymous functions for simple operations
- **map() & filter()** - Functional programming utilities
- **Closures** - Functions that capture outer scope variables
- **Classes** - Blueprint for creating objects
- **Attributes** - Object data (name, age, grade, etc.)
- **Methods** - Object behaviors (functions inside classes)
- **Inheritance** - Child classes inherit from parent classes
- **super()** - Call parent class methods
- **Polymorphism** - Same method name, different behavior per class
- **Shared Interface** - Multiple classes implementing same method

---

## ✨ Summary

Master Python functions and OOP design patterns through practical exercises, building toward a complete school management system demonstrating inheritance and polymorphism.