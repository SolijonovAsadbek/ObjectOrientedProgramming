# dataclass
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str
    email: str

    def __str__(self):
        return f'User {self.name} with email {self.email}'


alex = User('Alex', 'alex@gmail.com')
bob = User('Bob', 'bob@gmail.com')
# bob.name = 'Bob Smith'  # immutable
# alex.name = 'Alex Smith'  # immutable
# bob.email = 'epopnpdna@gmail.com'  # immutable
print(alex)
print(bob)
print(bob == alex)
print(bob is alex)
print(bob == bob)
print(bob is bob)
print(bob.name)
print(bob.email)
print(bob.__dict__)
print(alex.__dict__)
print(alex.__dict__ == bob.__dict__)
print(alex.__dict__ is bob.__dict__)
print(alex.__dict__ == alex.__dict__)
print(alex.__dict__ is alex.__dict__)
print(bool(alex))
print(bool(bob))
