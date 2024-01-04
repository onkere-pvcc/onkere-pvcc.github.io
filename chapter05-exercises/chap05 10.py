def find_hypot(side1, side2):
    """
    Calculate the length of the hypotenuse of a right-angled triangle.

    Args:
    side1 (float): Length of the first side.
    side2 (float): Length of the second side.

    Returns:
    float: Length of the hypotenuse.
    """
    hypotenuse = (side1 ** 2 + side2 ** 2) ** 0.5
    return hypotenuse

# Example usage:
side1 = 3.0
side2 = 4.0
hypotenuse = find_hypot(side1, side2)
print("Hypotenuse:", hypotenuse)
