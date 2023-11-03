try:
    tasks = ["1", "2", "3"]
    choice_library = ["+", "-", "=", "/"]
    user_choice = input("Введіть номер завдання (1-3): ")
    while user_choice not in tasks:
        user_choice = input("Помилка! введіть номер завдання (1-3): ")
    match user_choice:
        case "1":
            """Завдання 1: Створення класу для представлення бібліотеки з інкапсуляції.
            Створіть клас Library, який представляє бібліотеку з каталогом книг
            та методами для додавання та видалення книг.
            Приховати каталог книг із використанням інкапсуляції."""


            class Library:
                def __init__(self):
                    self.__catalog = set()

                def add_book(self, book):
                    book_lower = book.lower()
                    if book_lower in self.__catalog:
                        print(f"Книга '{book}' вже є в каталозі.")
                    else:
                        self.__catalog.add(book_lower)
                        print(f"Додано книгу '{book}' до каталогу.")

                def remove_book(self, book):
                    book_lower = book.lower()
                    if book_lower in self.__catalog:
                        self.__catalog.remove(book_lower)
                        print(f"Книга '{book}' видалена з каталогу.")
                    else:
                        print(f"Книга '{book}' не знайдена в каталозі.")

                def get_catalog(self):
                    if not self.__catalog:
                        return []
                    return list(self.__catalog)


            my_library = Library()
            print("Пояснення:\n"
                  "'+' - Добавити книгу в каталог.\n"
                  "'-' - Видалити книгу з каталогу.\n"
                  "'=' - Вивести список книг в каталозі.\n"
                  "'/' - Завершити роботу програми.")
            while True:
                library_choice = input("Введіть одну із дій ('+' '-' '=' '/'): ")
                while library_choice not in choice_library:
                    library_choice = input("Помилка! введіть одну із дій ('+' '-' '=' '/'): ")
                match library_choice:
                    case "+":
                        my_library.add_book(input("Введіть назву книги яку ви хочете добавити в каталог: "))
                        print("")
                    case "-":
                        my_library.remove_book(input("Введіть назву книги яку ви хочете видалити з каталога: "))
                        print("")
                    case "=":
                        print("Каталог книг в бібліотеці:")
                        print(my_library.get_catalog())
                        print("")
                    case "/":
                        print("Програму завершено.")
                        break

        case "2":
            """Завдання 2: Створення класу подання співробітника з допомогою інкапсуляції.
            Створіть клас Employee, який представляє співробітника з ім'ям, посадою та зарплатою.
            Приховати дані про зарплату за допомогою інкапсуляції."""


            class Employee:
                def __init__(self, name, position, salary):
                    self.name = name
                    self.position = position
                    self.__salary = salary

                def get_salary(self):
                    return self.__salary

                def set_salary(self, new_salary):
                    if new_salary >= 0:
                        self.__salary = new_salary
                        print(f"Зарплата співробітника {self.name} оновлена: {new_salary}")
                    else:
                        print("Зарплата не може бути від'ємною.")


            employee1 = Employee("Іван", "Менеджер", 50000)
            choice_employee = ("info", "salary")
            print("Варіанти:\n"
                  "'info' - Інформація про робітника.\n"
                  "'salary' - Змінити зарплату.\n"
                  "'quit' - Вийти з програми.")

            while True:
                employee_choice = input("Введіть одну із дій ('info' 'salary' 'quit'): ")
                while employee_choice not in choice_employee:
                    employee_choice = input("Помилка! введіть одну із дій ('info' 'salary' 'quit'): ")
                match employee_choice:
                    case "info":
                        print(f"Ім'я: {employee1.name}")
                        print(f"Посада: {employee1.position}")
                        print(f"Зарплата: {employee1.get_salary()}")
                        print("")
                    case "salary":
                        employee1.set_salary(int(input("Введіть нову зарплату: ")))
                        print("")
                    case "quit":
                        print("Програму завершено.")
                        break
        case "3":
            """Завдання 3: Створення класу представлення магазину з допомогою інкапсуляції.
            Створіть клас Store, який представляє магазин з асортиментом товарів
            та методами для додавання та видалення товарів.
            Приховати асортименти товарів з використанням інкапсуляції."""


            class Store:
                def __init__(self):
                    self.__inventory = {}

                def add_item(self, item, quantity):
                    item_lower = item.lower()
                    if item_lower in self.__inventory:
                        self.__inventory[item_lower] += quantity
                        print(f"Додано {quantity} одиниць товару '{item}' до асортименту.")
                    else:
                        self.__inventory[item_lower] = quantity
                        print(f"Додано {quantity} одиниць товару '{item}' до асортименту.")

                def remove_item(self, item, quantity):
                    item_lower = item.lower()
                    if item_lower in self.__inventory:
                        if self.__inventory[item_lower] >= quantity:
                            self.__inventory[item_lower] -= quantity
                            print(f"Видалено {quantity} одиниць товару '{item}' з асортименту.")
                            if self.__inventory[item_lower] == 0:
                                del self.__inventory[item_lower]
                        else:
                            print(f"У вас немає достатньої кількості товару '{item}' в асортименті.")
                    else:
                        print(f"Товар '{item}' не знайдений в асортименті.")

                def get_inventory(self):
                    return self.__inventory


            my_store = Store()
            choice_Store = ["+", "-", "=", "/"]
            while True:
                store_choice = input("Введіть одну із дій ('+' '-' '=' '/'): ")
                while store_choice not in choice_Store:
                    store_choice = input("Помилка! введіть одну із дій ('+' '-' '=' '/'): ")
                match store_choice:
                    case "+":
                        item = input("Введіть назву товару: ")
                        quantity = int(input("Введіть кількість товару: "))
                        my_store.add_item(item, quantity)

                    case "=":
                        inventory = my_store.get_inventory()
                        print("Асортимент товарів в магазині:")
                        for item, quantity in inventory.items():
                            print(f"{item}: {quantity} одиниць")

                    case "-":
                        item_to_remove = input("Введіть назву товару для видалення: ")
                        remove_quantity = int(input("Введіть кількість товару для видалення: "))
                        my_store.remove_item(item_to_remove, remove_quantity)

                    case "/":
                        print("Програму завершено.")
                        break
except Exception:
    print("Помилка! зв'яжіться з розробником програми.")
