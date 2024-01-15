#!/usr/bin/python3

"""This module defines the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new instance of the Square class.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The ID of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Square.

        Returns:
            str: String representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        attributs = ["id", "width", "height", "x", "y"]
        if args:
            for x in range(0, len(args)):
               self. __setattr__(attributs[x], args[x])
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

