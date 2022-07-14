from dataclasses import dataclass


# dataclass oddiy klasslarga qaraganda ancha yaxshiroq va hotirada saqlashda ham ustunlik qiladi
# yana bir imkoniyatlaridan biri ularni immutable(O`zgarmas) qilish imkonini beradi.
@dataclass(frozen=True)  # frozen=True class malumotlarini read-only qilish uchun ishlatiladi.
class User:
    fname: str
    lname: str
    age: int

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
alex.fname = 'Ali'  #immutable ma`lumot
print(alex.about)
edd.greet(alex)
alex.greet(edd)
