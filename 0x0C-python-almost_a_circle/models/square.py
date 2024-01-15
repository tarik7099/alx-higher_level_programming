#!/usr/bin/python3

"""This is a rectangle base"""

from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        self.width =  value
        self.height = value
    def update(self, *args, **kwargs):
        attributs = ["id", "width", "height", "x", "y"]
        if args:
            for x in range(0, len(args)):
                setattr(self, attributs[x], args[x])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    