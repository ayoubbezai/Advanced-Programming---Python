# basic input output

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

    The function ensures that both width and height are positive numbers,
    and that the height is greater than or equal to the width.

    Returns:
        dict[str, float]: 
            A dictionary containing the rectangle's width and height.  
            Example: {'width': 4.0, 'height': 6.0}
    """
    while True:
        try:
            width = float(input('Enter the width: '))
            if width <= 0:
                print('❌ Width must be a positive number. Try again.')
                continue

            height = float(input('Enter the height: '))
            if height <= 0:
                print('❌ Height must be a positive number. Try again.')
                continue

            if height < width:
                print('❌ Height must be greater than or equal to the width. Try again.')
                continue

            return {'width': width, 'height': height}

        except ValueError:
            print('❌ Width and height must be numbers. Try again.')


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
        - "rectangle": prompts for width and height
        - "square": prompts for side length

    Parameters:
        shape (str): The name of the shape ('circle', 'rectangle', or 'square').

    Returns:
        dict[str, float | str]: 
            A dictionary containing the shape name and its dimensions.  
            Examples:
                {'shape': 'circle', 'radius': 5.0}
                {'shape': 'rectangle', 'width': 4.0, 'height': 6.0}
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
