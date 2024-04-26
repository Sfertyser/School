# class Person:
#     def __init__(self, name, age, company):
#         self.name = name
#         self.age = age
#         self.company = company
#
#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Company: {self.company}")
#
#     def __del__(self):
#         print("Видалено людину з ім'ям:", self.name)
#
#
# artem = Person("Артем", 14, "Google")
# print(artem.name)
# print(artem.age)
# print(artem.company)
# artem.age = 15
# print(artem.age)
# artem.display_info()
# sergiy = Person("Сергій", 15, "Microsoft")
# print(sergiy.name)
# print(sergiy.age)
# sergiy.company = "Samsung"
# print(sergiy.company)
# sergiy.display_info()
# andriy = Person("Андрій", 16, "Amazon")
#
#
# class Hello:
#     def say_hello(self, message):
#         print(message)
#
#
# artem = Hello()
# artem.say_hello("hello")


"""
1. Створити клас для представлення точки в 2D просторі:
Клас повинен мати два атрибути: x та y, що відповідають координатам точки.
Додати методи для отримання та встановлення значень атрибутів,
а також для обчислення відстані до іншої точки.
"""


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_x(self):
#         return self.x
#
#     def set_x(self, new_x):
#         self.x = new_x
#
#     def get_y(self):
#         return self.y
#
#     def set_y(self, new_y):
#         self.y = new_y
#
#     def distance(self, other_point):
#         dx = self.x - other_point.x
#         dy = self.y - other_point.y
#         return (dx**2 + dy**2)**0.5
#
#
# point1 = Point(2, 3)
# print(point1.get_x(), point1.get_y())
# point2 = Point(5, 7)
# print(point2.get_x(), point2.get_y())
# distance = point1.distance(point2)
# print(distance)


"""
2. Створити клас для представлення прямокутника:
Клас повинен мати чотири атрибути: x, y, width та height,
що відповідають координатам лівого нижнього кута,
ширині та висоті прямокутника відповідно.
Додати методи для отримання та встановлення значень атрибутів,
а також для обчислення площі та периметра прямокутника.
"""


# class Pryamokutnik:
#     def __init__(self, x, y, width, lenth):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.lenth = lenth
#
#     def get_area(self):
#         return self.width * self.lenth
#
#     def ger_perimetr(self):
#         return (self.width + self.lenth) * 2
#
#     def get_x(self):
#         return self.x
#
#     def set_x(self, new_x):
#         self.x = new_x
#
#     def get_y(self):
#         return self.y
#
#     def set_y(self, new_y):
#         self.y = new_y
#
#     def get_lenth(self):
#         return self.lenth
#
#     def get_width(self):
#         return self.width
#
#
# pryamokutnik1 = Pryamokutnik(3, 4, 5, 2)
# print(pryamokutnik1.get_lenth(), pryamokutnik1.get_width())
# print(pryamokutnik1.get_area(), pryamokutnik1.ger_perimetr())

"""
3. Створити клас для представлення банківського рахунку:
Клас повинен мати два атрибути: balance та interest_rate,
що відповідають залишку на рахунку та процентній ставці відповідно.
Додати методи для отримання та встановлення значень атрибутів,
а також для внесення та зняття коштів, а також для нарахування відсотків.
"""


class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest


account = BankAccount(1000, 0.05)
print(account.get_balance())
account.deposit(700)
account.withdraw(300)
print(account.get_balance())
account.calculate_interest()
print(account.get_balance())
