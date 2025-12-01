import math

PI = math.pi


# ==============================================================
# Base Class
# ==============================================================

class Shape:
    """A generic base class representing a geometric shape."""

    def area(self) -> float:
        """Return the area of the shape (0.0 for base class)."""
        return 0.0

    def perimeter(self) -> float:
        """Return the perimeter of the shape (0.0 for base class)."""
        return 0.0

    def __str__(self) -> str:
        """Return a generic description of the shape."""
        return "Generic Shape"


# ==============================================================
# Circle Class
# ==============================================================

class Circle(Shape):
    """A circle shape defined by its radius."""

    def __init__(self, radius: float):
        """
        Initialize a circle.

        Parameters:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self) -> float:
        """Return the area of the circle."""
        return PI * (self.radius ** 2)

    def perimeter(self) -> float:
        """Return the circumference of the circle."""
        return 2 * PI * self.radius

    def __str__(self) -> str:
        """Return a string representation of the circle."""
        return f"Circle (radius={self.radius})"


# ==============================================================
# Rectangle Class
# ==============================================================

class Rectangle(Shape):
    """A rectangle shape defined by its length and width."""

    def __init__(self, length: float, width: float):
        """
        Initialize a rectangle.

        Parameters:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.length * self.width

    def perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

    def __str__(self) -> str:
        """Return a string representation of the rectangle."""
        return f"Rectangle (length={self.length}, width={self.width})"


# ==============================================================
# Square Class
# ==============================================================

class Square(Rectangle):
    """A square (special case of a rectangle with all sides equal)."""

    def __init__(self, side: float):
        """
        Initialize a square.

        Parameters:
            side (float): The length of each side.
        """
        super().__init__(side, side)

    def __str__(self) -> str:
        """Return a string representation of the square."""
        return f"Square (side={self.length})"

class Trinalle(Shape):
    def __init__(self , base , hight):
        self.base = base ;
        self.hight = hight
    def area(self) -> float:
        return (self.base * self.hight)/2

# ==============================================================
# Input Functions
# ==============================================================

def ask_for_circle() -> Circle:
    """Prompt the user to input a valid radius and return a Circle object."""
    while True:
        try:
            radius = float(input("Enter radius: "))
            if radius <= 0:
                print("❌ Radius must be positive.\n")
                continue
            return Circle(radius)
        except ValueError:
            print("❌ Invalid input. Please enter a number.\n")


def ask_for_rectangle() -> Rectangle:
    """Prompt the user to input valid rectangle dimensions and return a Rectangle object."""
    while True:
        try:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            if length <= 0 or width <= 0:
                print("❌ Length and width must be positive.\n")
                continue
            return Rectangle(length, width)
        except ValueError:
            print("❌ Invalid input. Please enter numbers.\n")


def ask_for_square() -> Square:
    """Prompt the user to input a valid side length and return a Square object."""
    while True:
        try:
            side = float(input("Enter side length: "))
            if side <= 0:
                print("❌ Side must be positive.\n")
                continue
            return Square(side)
        except ValueError:
            print("❌ Invalid input. Please enter a number.\n")


# ==============================================================
# File Output
# ==============================================================

def write_result_to_file(shape: Shape):
    """
    Append the shape details, area, and perimeter to 'results.txt'.

    If the file doesn't exist, it is created automatically.
    """
    with open("tp1/results.txt", "a") as file:
        file.write(f"Shape: {shape}, Area={shape.area()}, Perimeter={shape.perimeter()}\n")


# ==============================================================
# Main Program
# ==============================================================

def main():
    """
    Main program loop for the OOP Shape Calculator.

    Steps:
        1. Ask the user which shape to calculate.
        2. Collect its dimensions using helper functions.
        3. Create an object (Circle, Rectangle, or Square).
        4. Display the results.
        5. Save them to 'results.txt'.
        6. Repeat until the user exits.
    """
    print("📐 Welcome to the OOP Shape Calculator!")
    print("You can calculate the area and perimeter of: circle, rectangle, or square.")
    print("Type 'exit' anytime to quit.\n")

    while True:
        shape_name = input("Enter shape name (circle / rectangle / square) or 'exit': ").lower().strip()

        if shape_name == "exit":
            print("\n👋 Goodbye! Results saved to 'results.txt'.")
            break

        match shape_name:
            case "circle":
                shape = ask_for_circle()
            case "rectangle":
                shape = ask_for_rectangle()
            case "square":
                shape = ask_for_square()
            case _:
                print("❌ Invalid shape name. Try again.\n")
                continue

        print(f"\n✅ {shape}")
        print(f"   ➤ Area: {shape.area()}")
        print(f"   ➤ Perimeter: {shape.perimeter()}\n")

        write_result_to_file(shape)
        print("💾 Result saved successfully.\n")


# ==============================================================
# Entry Point
# ==============================================================

if __name__ == "__main__":
    main()
