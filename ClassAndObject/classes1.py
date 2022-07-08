class User:
    pass

user = User()  # mutable class
user.first_name = 'Alex'
user.last_name = 'Benjamin'
user.age = 12
print(f"User: {user.first_name}, Age: {user.age}")
