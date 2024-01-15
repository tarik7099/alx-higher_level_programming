#!/usr/bin/python3

"""This is a rectangle base"""

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        return self.__height * self.__width
    
    def display(self):
        Rectangle_str = ""
        print("\n" * self.__y , end='')
        for i in range(self.__height):
            Rectangle_str += " " * self.__x +"#" * self.__width + "\n" 
        print(Rectangle_str.strip("\n"))

    def __str__(self):
        return  f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    
    def update(self, *args, **kwargs):
        attributs = ["id", "width", "height", "x", "y"]
        if args:
            for x in range(0, len(args)):
                setattr(self, attributs[x], args[x])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        attrib = ["x", "y", "id", "width", "height"]
        value = [self.x , self.y , self.id,  self.width, self.height]
        dict  = {}
        for i in range(len(attrib)):
            dict[attrib[i]] = value[i]
        return dict