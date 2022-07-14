# Default value

class Dog:
    def __init__(self, name, age, speak):
        self.name = name
        self.age = age
        self.speak = speak

    def say(self, value='Wow'):
        self.speak = value
        return self.speak

    def __str__(self):
        return f"{self.name} is {self.age} years old"


bethoven = Dog("Bethoven", 1, "Woof")
doggie = Dog('Doggie', age=2, speak="Woof Woof")
print(bethoven)
print(doggie)
print(doggie.say())
print(bethoven.say())
