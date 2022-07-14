# Obyektga yo`naltirilgan daturlashning mashhur bo'lishiga sabab Inhertance sabab bo'lgan
# Inheritence - ReUsebility Yozgan koddan qayta foydalanish uchun ishlarildi.

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        print(f"login: {self.email} {self.password}")

    def logout(self):
        print(f"logout: {self.email} {self.password}")

    def __str__(self):
        return

