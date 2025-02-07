#!/usr/bin/python3

"""Following of basegeometry class"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def __init__(self):
        """
        empty class
        """
        pass

    def area(self):
        """
        Raises an Exception to indicate that this method
        is not implemented in BaseGeometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the variable.
            value (int): The value to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
