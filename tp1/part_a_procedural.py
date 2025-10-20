# basic input output
import math
PI = math.pi

def ask_for_circle_dimensions() -> dict[str, float]:
    """
    Prompt the user to enter the radius of a circle.

    Returns:
        dict[str, float]: 
            A dictionary containing the circle's radius.  
            Example: {'radius': 5.0}
    """
    while True:
        try:
            radius = float(input('Enter the radius: '))
            if radius <= 0:
                print("❌ Radius must be a positive number. Try again.")
                continue
            return {'radius': radius}
        except ValueError:
            print("❌ Radius must be a number. Try again.")


def ask_for_rectangle_dimensions() -> dict[str, float]:
    """
    Prompt the user to enter the dimensions of a rectangle.

    The function ensures that both width and length are positive numbers,
    and that the length is greater than or equal to the width.

    Returns:
        dict[str, float]: 
            A dictionary containing the rectangle's width and length.  
            Example: {'width': 4.0, 'length': 6.0}
    """
    while True:
        try:
            width = float(input('Enter the width: '))
            if width <= 0:
                print('❌ Width must be a positive number. Try again.')
                continue

            length = float(input('Enter the length: '))
            if length <= 0:
                print('❌ length must be a positive number. Try again.')
                continue

            if length < width:
                print('❌ length must be greater than or equal to the width. Try again.')
                continue

            return {'width': width, 'length': length}

        except ValueError:
            print('❌ Width and length must be numbers. Try again.')


def ask_for_square_dimensions() -> dict[str, float]:
    """
    Prompt the user to enter the side length of a square.

    Returns:
        dict[str, float]: 
            A dictionary containing the square's side length.  
            Example: {'side': 5.0}
    """
    while True:
        try:
            side = float(input('Enter the side length: '))
            if side <= 0:
                print('❌ Side length must be a positive number. Try again.')
                continue
            return {'side': side}
        except ValueError:
            print('❌ Side length must be a number. Try again.')


def ask_for_dimensions(shape: str) -> dict[str, float | str]:
    """
    Ask the user for dimensions of the specified shape.

    Supported shapes:
        - "circle": prompts for radius
        - "rectangle": prompts for width and length
        - "square": prompts for side length

    Parameters:
        shape (str): The name of the shape ('circle', 'rectangle', or 'square').

    Returns:
        dict[str, float | str]: 
            A dictionary containing the shape name and its dimensions.  
            Examples:
                {'shape': 'circle', 'radius': 5.0}
                {'shape': 'rectangle', 'width': 4.0, 'length': 6.0}
                {'shape': 'square', 'side': 3.0}
    """
    match shape.lower():
        case "circle":
            data = ask_for_circle_dimensions()
            return {'shape': 'circle', **data}
        case "rectangle":
            data = ask_for_rectangle_dimensions()
            return {'shape': 'rectangle', **data}
        case "square":
            data = ask_for_square_dimensions()
            return {'shape': 'square', **data}
        case _:
            print("❌ Unknown shape. Please choose 'circle', 'rectangle', or 'square'.")
            return {}


def area_and_perimeter_calc(shape: dict[str, float | str]) -> dict[str, float | str]:
    """
    Calculate the area and perimeter of a given geometric shape.

    Supported shapes:
        - "circle": uses radius
        - "rectangle": uses width and length
        - "square": uses side length

    Parameters:
        shape (dict[str, float | str]): 
            A dictionary containing the shape name and its dimensions.  
            Examples:
                {'shape': 'circle', 'radius': 5.0}
                {'shape': 'rectangle', 'width': 4.0, 'length': 6.0}
                {'shape': 'square', 'side': 3.0}

    Returns:
        dict[str, float | str]: 
            The same shape dictionary updated with its calculated area and perimeter.  
            Examples:
                {'shape': 'circle', 'radius': 5.0, 'area': 78.54, 'perimeter': 31.42}
                {'shape': 'rectangle', 'width': 4.0, 'length': 6.0, 'area': 24.0, 'perimeter': 20.0}
                {'shape': 'square', 'side': 3.0, 'area': 9.0, 'perimeter': 12.0}
    """
    match shape['shape']:
        case 'circle':
            r = shape['radius']
            area = PI * r ** 2
            perimeter = 2 * PI * r

        case 'rectangle':
            w = shape['width']
            h = shape['length']
            area = w * h
            perimeter = 2 * (w + h)

        case 'square':
            s = shape['side']
            area = s ** 2
            perimeter = 4 * s

        case _:
            print("❌ Unknown shape type.")
            return {}

    return {**shape, 'area': area, 'perimeter': perimeter}

def write_in_results_file(shape: dict[str, float | str]):
    """
    Append a shape's calculated details to a text file named 'results.txt'.

    This function records:
        - the shape name
        - its specific dimensions (radius, width/length, or side)
        - its area
        - its perimeter

    If the file does not exist, it will be created automatically.
    If it already exists, new results will be appended at the end.

    Parameters:
        shape (dict[str, float | str]):
            A dictionary containing:
                - 'shape' (str): Shape name ('circle', 'rectangle', or 'square')
                - dimensions (float): depending on the shape:
                    * 'radius' for circles
                    * 'width' and 'length' for rectangles
                    * 'side' for squares
                - 'area' (float): calculated area
                - 'perimeter' (float): calculated perimeter

    File Output Example (results.txt):
        Shape: Circle (radius=20.0), Area: 1256.6370614359173, Perimeter: 125.66370614359172
        Shape: Rectangle (width=4.0, length=6.0), Area: 24.0, Perimeter: 20.0
        Shape: Square (side=5.0), Area: 25.0, Perimeter: 20.0
    """
    with open('tp1/results.txt', 'a') as file:
        match shape['shape']:
            case 'circle':
                file.write(
                    f"Shape: Circle (radius={shape['radius']}), "
                    f"Area: {shape['area']}, "
                    f"Perimeter: {shape['perimeter']}\n"
                )

            case 'rectangle':
                file.write(
                    f"Shape: Rectangle (width={shape['width']}, length={shape['length']}), "
                    f"Area: {shape['area']}, "
                    f"Perimeter: {shape['perimeter']}\n"
                )

            case 'square':
                file.write(
                    f"Shape: Square (side={shape['side']}), "
                    f"Area: {shape['area']}, "
                    f"Perimeter: {shape['perimeter']}\n"
                )

            case _:
                file.write("❌ Unknown shape type — cannot write to file.\n")


def main():
    """
    Main program loop for shape area and perimeter calculation.

    This function:
        1. Prompts the user to choose a shape (circle, rectangle, or square).
        2. Asks for the corresponding dimensions.
        3. Calculates the area and perimeter.
        4. Displays the results on screen in a readable format.
        5. Saves the results into 'results.txt'.
        6. Repeats until the user chooses to exit.
    """
    print("📐 Welcome to the Shape Calculator!")
    print("You can calculate the area and perimeter of a circle, rectangle, or square.")
    print("Type 'exit' anytime to quit.\n")

    while True:
        shape_name = input("Enter shape name (circle / rectangle / square) or 'exit' to quit: ").lower().strip()

        if shape_name == 'exit':
            print("\n👋 Goodbye! All results have been saved in 'results.txt'.")
            break

        if shape_name not in ['circle', 'rectangle', 'square']:
            print("❌ Invalid shape. Please choose circle, rectangle, or square.\n")
            continue

        # Get user input for dimensions
        shape_data = ask_for_dimensions(shape_name)

        # Calculate area and perimeter
        result = area_and_perimeter_calc(shape_data)

        # Display results neatly
        print("\n✅ Calculation Result:")
        match result['shape']:
            case 'circle':
                print(
                    f"   ➤ Shape: Circle (radius = {result['radius']})\n"
                    f"   ➤ Area: {result['area']}\n"
                    f"   ➤ Perimeter: {result['perimeter']}\n"
                )
            case 'rectangle':
                print(
                    f"   ➤ Shape: Rectangle (width = {result['width']}, length = {result['length']})\n"
                    f"   ➤ Area: {result['area']}\n"
                    f"   ➤ Perimeter: {result['perimeter']}\n"
                )
            case 'square':
                print(
                    f"   ➤ Shape: Square (side = {result['side']})\n"
                    f"   ➤ Area: {result['area']}\n"
                    f"   ➤ Perimeter: {result['perimeter']}\n"
                )

        # Save to file
        write_in_results_file(result)

        print("💾 Result saved to 'results.txt'.\n")


if __name__ == "__main__":
    main()


