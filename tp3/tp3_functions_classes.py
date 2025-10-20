from typing import Callable

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

    