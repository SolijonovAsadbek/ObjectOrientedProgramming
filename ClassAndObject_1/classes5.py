class User:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    @property
    def full_name(self):
        return f"{self.fname} {self.lname}"

    @property
    def about(self):
        return f"{self.full_name} is {self.age} years old."

    def greet(self, user):
        print(f'{self.fname}: Hi {user.fname}!')  # boshqa bir obyektni ichiga kirish


alex = User(fname='Alex', lname='Benjamin', age=12)
edd = User(fname='Edd', lname='Sheeran', age=30)
print(alex.about)
edd.greet(alex)
alex.greet(edd)
