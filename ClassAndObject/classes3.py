class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


alex = User(first_name='Alex', last_name='Benjamin', age=12)
bob = User(first_name='Edd', last_name='Sheeran', age=30)

print(f"User: {alex.first_name}, Age: {alex.age}")
print(f"User: {bob.first_name}, Age: {bob.age}")
