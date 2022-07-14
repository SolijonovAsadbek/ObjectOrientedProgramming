# Dunder Methods 2

class Vector:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # string
    def __str__(self):
        return F"Vector({self.x}, {self.y})"

    # representation
    def __repr__(self):
        return F"Vector({self.x}, {self.y})"

    # is_equal
    def __eq__(self, other) -> bool:
        x = self.x == other.x
        y = self.y == other.y
        return x and y

    # addition
    def __add__(self, other) -> 'Vector':
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


v0 = v1 = Vector(3, 2)
v2 = Vector(3, 2)
print(f'v1 == v0 : {v1 == v0}')  # teng equal
print(f'v1 == v2 : {v1 == v2}')  # tengemas is not equal
