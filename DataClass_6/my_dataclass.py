# dataclass
from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str

    def __str__(self):
        return f'User {self.name} with email {self.email}'


alex = User('Alex', 'alex@gmail.com')
bob = User('Bob', 'bob@gmail.com')
bob.name = 'Bob Smith'
alex.name = 'Alex Smith'
print(alex)
print(bob)
