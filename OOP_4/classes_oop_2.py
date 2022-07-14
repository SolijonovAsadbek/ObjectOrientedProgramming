import math


class Vector:
    class_name = 'Vector class'

    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # instace method
    def calculate_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property  # o'zgaruvchi qabul qilmaydigan metod.
    def length(self):
        return self.calculate_length()

    @staticmethod
    def print_hello():
        print('Hello. I`m a Vector class')

    @classmethod
    def from_magnitude(cls, magnitude, radian):
        x = magnitude * 2 * radian
        y = magnitude * 2 + radian
        return cls(x, y)


v = Vector(3, 4)
print(v.calculate_length())  # instancemethod
print(v.length)  # @property

Vector.print_hello()  # @staticmethod
v.print_hello()  # @staticmethod

# @classmethod
fm = Vector.from_magnitude(magnitude=1.5, radian=1)
print(fm.length)
