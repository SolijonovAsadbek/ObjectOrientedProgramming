class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


alex = User(first_name='Alex', last_name='Benjamin', age=12)
edd = User(first_name='Edd', last_name='Sheeran', age=30)

print(f"User: {alex.first_name}, Age: {alex.age}")
print(f"User: {alex.full_name()}, Age: {alex.age}")
# print(f"User: {alex.full_name}, Age: {alex.age}")  # property yozish
print(f"User: {edd.first_name}, Age: {edd.age}")
print(f"User: {edd.full_name()}, Age: {edd.age}")
# print(f"User: {edd.full_name}, Age: {edd.age}")  # property yozish
