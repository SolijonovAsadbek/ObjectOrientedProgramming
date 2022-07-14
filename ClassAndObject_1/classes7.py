# Alternatives to Dataclass:
from dataclasses import dataclass


# class NameCard2:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name} is {self.age} years old.'
#
#     def __repr__(self):
#         return f'NameCard2({self.name}, {self.age})'
#
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age


# @dataclass
# class NameCard:
#     fname: str
#     lname: str


# alex = NameCard('Alex', 'Zhang')
# bob = NameCard('Bob', 'Smith')
# bob2 = NameCard('Alex', 'Zhang')
# print(alex)
# print(bob)
# print(alex == bob)
# print(alex == bob2)
# print([alex, bob, bob2])

from collections import namedtuple

NameCard = namedtuple('NameCard', 'fname lname')

alex = NameCard('Alex', 'Zhang')
bob = NameCard('Bob', 'Smith')
bob2 = NameCard('Alex', 'Zhang')
print(alex)
print(bob)
print(alex == bob)
print(alex == bob2)
print([alex, bob, bob2])