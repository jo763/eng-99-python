#There are four pillars of OOP

# Abstraction

# Making life easy for the user by providing obvious inputs/outputs (black boxing)

# Encapsulation

# Making variables (and methods) private

# Inheritance

# Passing on attributes and methods to avoid repetition

# Polymorphism

# 'many forms' ability to overwrite methods/attributes

# Create a rectangle class
# it should have length and width attributes
# perimeter method
# area method
# then create a square class
# it should take have a side_length attribute
# perimeter and area methods available

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length

class Square(Rectangle):
    def side_length(self):
        x = Rectangle.perimeter(self)
        return x/4

q = Square(4,6)

print(q.side_length())


