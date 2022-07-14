class Vector:
    class_name = 'Vector'  # "class veriable"

    def __init__(self):
        self.name = 'Vector'  # "instance variable"


print(Vector.class_name)  # "class veriable"
print(Vector.name)  # "instance variable"
v = Vector()
print(v.name)  # "instance variable"
print(v.class_name)  # "class veriable"
