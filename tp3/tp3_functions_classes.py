from typing import Callable , List

# -------------------------------
# Exercise 1: Basic Functions
# -------------------------------

def power(base: float, exp: float) -> float:
    """
    Calculate a number raised to a given power.

    Parameters:
        base (float): The base number.
        exp (float): The exponent to raise the base to.

    Returns:
        float: The result of base raised to the power exp.

    Example:
        >>> power(2, 3)
        8
    """
    return base ** exp


def sum_of_powers(numbers: list[float], exp: float) -> float:
    """
    Calculate the sum of all numbers raised to a given exponent.

    Parameters:
        numbers (list[float]): A list of numbers to raise to a power.
        exp (float): The exponent to use.

    Returns:
        float: The sum of each number in the list raised to exp.

    Example:
        >>> sum_of_powers([1, 2, 3], 2)
        14   # 1^2 + 2^2 + 3^2
    """
    return sum(power(num, exp) for num in numbers)


# -------------------------------
# Exercise 2: Lambda and map/filter
# -------------------------------

def celsius_to_fahrenheit(celsius_list: list[float]) -> list[float]:
    """
    Convert a list of temperatures from Celsius to Fahrenheit.

    Parameters:
        celsius_list (list[float]): List of temperatures in Celsius.

    Returns:
        list[float]: List of temperatures converted to Fahrenheit.

    Example:
        >>> celsius_to_fahrenheit([0, 100])
        [32.0, 212.0]
    """
    return list(map(lambda c: (c * 9/5) + 32, celsius_list))


# -------------------------------
# Exercise 3: Closure Function
# -------------------------------

def multiplier(n: float) -> Callable[[float], float]:
    """
    Create a closure function that multiplies its input by a fixed factor.

    Parameters:
        n (float): The multiplier factor.

    Returns:
        Callable[[float], float]: A function that takes a float input and returns it multiplied by n.

    Example:
        >>> double = multiplier(2)
        >>> double(5)
        10
    """
    def inner(x: float) -> float:
        return x * n
    return inner



# -------------------------------
# Exercise 4 and 5 : Student Class
# -------------------------------

class Student:
    """
    A class representing a student with basic attributes and methods 
    to display and update their grade.

    Attributes:
        name (str): The student's name.
        age (int): The student's age.
        grade (float): The student's current grade.
    """

    def __init__(self, name: str, age: int, grade: float):
        """
        Initialize a Student instance with name, age, and grade.

        Parameters:
            name (str): The student's name.
            age (int): The student's age.
            grade (float): The student's initial grade.
        """
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        """
        Display the student's information in a readable format.

        Prints:
            Name, age, and grade of the student.
        """
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def update_grade(self, new_grade: float):
        """
        Update the student's grade to a new value and confirm the update.

        Parameters:
            new_grade (float): The new grade to assign to the student.

        Prints:
            A message indicating the old and new grade.
        """
        prev_grade = self.grade
        self.grade = new_grade
        print(f"{self.name}'s grade updated from {prev_grade} to {self.grade}")


# -------------------------------
# Exercise 6 & 7: Parent and Child Classes
# -------------------------------



class Person:
    """
    Base class representing a generic person.

    Attributes:
        name (str): Person's name.
        age (int): Person's age.
    """

    def __init__(self, name: str, age: int):
        """
        Initialize a Person instance.

        Parameters:
            name (str): Name of the person.
            age (int): Age of the person.
        """
        self.name = name
        self.age = age

    def introduce(self):
        """
        Print a generic introduction.

        Prints:
            A string like "Hello, I am <name>, <age> years old."
        """
        print(f"Hello, I am {self.name}, {self.age} years old.")

    def work(self):
        """
        Generic work method.

        Prints:
            A string describing a generic activity.
        """
        print("Doing something generic...")


class Teacher(Person):
    """
    Subclass of Person representing a teacher.

    Attributes:
        subject (str): The subject taught by the teacher.
    """

    def __init__(self, name: str, age: int, subject: str):
        """
        Initialize a Teacher instance.

        Parameters:
            name (str): Teacher's name.
            age (int): Teacher's age.
            subject (str): Subject the teacher teaches.
        """
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        """
        Print teacher-specific introduction.

        Prints:
            A string like "Hello, I am <name>, <age> years old, and I teach <subject>."
        """
        print(f"Hello, I am {self.name}, {self.age} years old, and I teach {self.subject}.")

    def work(self):
        """
        Override generic work method.

        Prints:
            A string describing teaching activity.
        """
        print("Teaching students...")


# -------------------------------
# Exercise 8: Shared Interface
# -------------------------------
class Dog:
    """
    Class representing a dog.

    Methods:
        speak(): Prints the sound a dog makes.
    """
    def speak(self):
        """
        Print the dog's sound.

        Prints:
            "Woof!"
        """
        print("Woof!")


class Cat:
    """
    Class representing a cat.

    Methods:
        speak(): Prints the sound a cat makes.
    """
    def speak(self):
        """
        Print the cat's sound.

        Prints:
            "Meow!"
        """
        print("Meow!")


class Bird:
    """
    Class representing a bird.

    Methods:
        speak(): Prints the sound a bird makes.
    """
    def speak(self):
        """
        Print the bird's sound.

        Prints:
            "Chirp!"
        """
        print("Chirp!")



# -------------------------------
# Exercise 9: Polymorphism with Shapes
# -------------------------------

import math
from typing import List

class Shape:
    """Base class for geometric shapes.

    Methods:
        area(): Must be implemented by subclasses. Returns the area of the shape.
    """
    def area(self) -> float:
        """Area method must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement area() method.")


class Circle(Shape):
    """A circle shape defined by its radius.

    Attributes:
        radius (float): The radius of the circle.
    """
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Return the area of the circle."""
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    """A rectangle shape defined by width and height.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.width * self.height


def print_shapes_area(shapes: List[Shape]) -> None:
    """Print the area of each shape in the list.

    Parameters:
        shapes (List[Shape]): List of Shape instances (Circle, Rectangle, etc.)
    """
    for shape in shapes:
        print(f"{type(shape).__name__} area: {shape.area()}")





# -------------------------------
# Exercise 10: School Management System
# -------------------------------


class Person:
    """Base class representing a generic person.

    Attributes:
        name (str): Name of the person.
        age (int): Age of the person.
    """

    def __init__(self, name: str, age: int):
        """Initialize a Person instance.

        Parameters:
            name (str): Name of the person.
            age (int): Age of the person.
        """
        self.name = name
        self.age = age

    def introduce(self) -> str:
        """Return a generic introduction string."""
        return f"Hello, I am {self.name}, {self.age} years old."


class Student(Person):
    """Represents a student, subclass of Person.

    Attributes:
        grade (float): The student's grade.
    """

    def __init__(self, name: str, age: int, grade: float):
        """Initialize a Student instance.

        Parameters:
            name (str): Name of the student.
            age (int): Age of the student.
            grade (float): Student's grade.
        """
        super().__init__(name, age)
        self.grade = grade

    def introduce(self) -> str:
        """Return a student-specific introduction string."""
        return f"Hello, I am {self.name}, {self.age} years old, and my grade is {self.grade}."


class Teacher(Person):
    """Represents a teacher, subclass of Person.

    Attributes:
        subject (str): Subject the teacher teaches.
    """

    def __init__(self, name: str, age: int, subject: str):
        """Initialize a Teacher instance.

        Parameters:
            name (str): Name of the teacher.
            age (int): Age of the teacher.
            subject (str): Subject taught by the teacher.
        """
        super().__init__(name, age)
        self.subject = subject

    def introduce(self) -> str:
        """Return a teacher-specific introduction string."""
        return f"Hello, I am {self.name}, {self.age} years old, and I teach {self.subject}."


def introduce_all(people: List[Person]) -> None:
    """Loop through a list of people and print their introductions.

    Parameters:
        people (List[Person]): List of Person instances (Student or Teacher).
    """
    for person in people:
        print(person.introduce())




if __name__ == "__main__":
    shapes_list = [Circle(5), Rectangle(4, 6), Circle(3)]
    print('exo 9 test :\n')
    print_shapes_area(shapes_list)
    print('exo 10 test :\n')
    school_members = [
        Student("Alice", 16, 88.5),
        Teacher("Mr. Bob", 40, "Math"),
        Student("Charlie", 17, 92.0)
    ]

    introduce_all(school_members)
