# Завдання 1: Створення класу для представлення бібліотеки з інкапсуляції.
# Створіть клас Library, який представляє бібліотеку з каталогом книг та методами для додавання та видалення книг.
# Приховати каталог книг із використанням інкапсуляції.
class Library:
    def __init__(self):
        # Приватне поле каталогу книг, починається з пустого списку.
        self.__catalog = []

    def add_book(self, book):
        # Метод для додавання книги до каталогу.
        self.__catalog.append(book)
        print(f"Книга '{book}' додана до каталогу.")

    def remove_book(self, book):
        # Метод для видалення книги з каталогу.
        if book in self.__catalog:
            self.__catalog.remove(book)
            print(f"Книга '{book}' видалена з каталогу.")
        else:
            print(f"Книга '{book}' не знайдена в каталозі.")

    def get_catalog(self):
        # Метод для отримання списку всіх книг в каталозі (інформація про інкапсульований каталог).
        return self.__catalog


# Приклад використання класу Library:
my_library = Library()

my_library.add_book("Книга 1")
my_library.add_book("Книга 2")
my_library.add_book("Книга 3")

print("Каталог книг в бібліотеці:")
print(my_library.get_catalog())

my_library.remove_book("Книга 2")

print("Оновлений каталог книг в бібліотеці:")
print(my_library.get_catalog())


# Завдання 2: Створення класу подання співробітника з допомогою інкапсуляції.
# Створіть клас Employee, який представляє співробітника з ім'ям, посадою та зарплатою.
# Приховати дані про зарплату за допомогою інкапсуляції.


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        # Приватне поле для зарплати.
        self.__salary = salary

    def get_salary(self):
        # Метод для отримання зарплати співробітника (інформація про інкапсульовану зарплату).
        return self.__salary

    def set_salary(self, new_salary):
        # Метод для зміни зарплати співробітника (за необхідності).
        if new_salary >= 0:
            self.__salary = new_salary
            print(f"Зарплата співробітника {self.name} оновлена: {new_salary}")
        else:
            print("Зарплата не може бути від'ємною.")


# Приклад використання класу Employee:
employee1 = Employee("Іван", "Менеджер", 50000)

print(f"Ім'я: {employee1.name}")
print(f"Посада: {employee1.position}")
print(f"Зарплата: {employee1.get_salary()}")

employee1.set_salary(55000)  # Зміна зарплати на 55000
print(f"Оновлена зарплата: {employee1.get_salary()}")

employee1.set_salary(-1000)  # Намагання встановити від'ємну зарплату


# Завдання 3: Створення класу представлення магазину з допомогою інкапсуляції.
# Створіть клас Store, який представляє магазин з асортиментом товарів та методами для додавання та видалення товарів.
# Приховати асортименти товарів з використанням інкапсуляції.


class Store:
    def __init__(self):
        # Приватне поле для асортименту товарів, починається з пустого словника.
        self.__inventory = {}

    def add_item(self, item, quantity):
        # Метод для додавання товару до асортименту магазину.
        if item in self.__inventory:
            # Якщо товар вже є в асортименті, додати кількість до існуючого товару.
            self.__inventory[item] += quantity
        else:
            # Якщо товар відсутній в асортименті, створити новий запис.
            self.__inventory[item] = quantity
        print(f"Додано {quantity} одиниць товару '{item}' до асортименту.")

    def remove_item(self, item, quantity):
        # Метод для видалення товару з асортименту магазину.
        if item in self.__inventory and self.__inventory[item] >= quantity:
            self.__inventory[item] -= quantity
            if self.__inventory[item] == 0:
                del self.__inventory[item]
            print(f"Видалено {quantity} одиниць товару '{item}' з асортименту.")
        else:
            print(f"Товар '{item}' не знайдено в асортименті або недостатньо кількості.")

    def get_inventory(self):
        # Метод для отримання асортименту товарів (інформація про інкапсульований асортимент).
        return self.__inventory


# Приклад використання класу Store:
my_store = Store()

my_store.add_item("Футболка", 100)
my_store.add_item("Джинси", 50)
my_store.add_item("Кросівки", 30)

print("Асортимент товарів у магазині:")
print(my_store.get_inventory())

my_store.remove_item("Футболка", 20)

print("Оновлений асортимент товарів у магазині:")
print(my_store.get_inventory())

# Програма повинна вивести трикутник як на малюнку.
# Програма отримує число - скільки вивести рядків.
# Кожен рядок має номер та число вирівняне по правому краю з кількистю нулів відповіно до номера рядку.

# Запит користувача про кількість рядків
num_rows = int(input("Введіть кількість рядків: "))

# Використовуємо цикл для створення трикутника
for i in range(1, num_rows + 1):
    # Створюємо рядок з номером та нулями, вирівняними по правому краю
    row = f"{i:2d} {'0' * i}"
    print(row)
