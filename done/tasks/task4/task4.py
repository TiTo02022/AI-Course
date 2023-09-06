from abc import ABC

class shape(ABC):
    def area(self):
        pass

class Rectangle(shape):
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        return self.height * self.width

class Circle(shape):
     def __init__(self,radius):
          self.radius = radius

     def area(self):
        return 3.14 * (self.radius ** 2)
             


rectangle = Rectangle(4, 5)
print(rectangle.area())
circle = Circle(3)
print(circle.area())