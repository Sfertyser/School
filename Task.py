import random
"""Задача: Магазин книг з інформацією про покупців
Створіть програму для інтернет-магазину книг, яка генерує список покупців.
Кожен покупець представлений словником з ключами
"ім'я", "прізвище", "адреса" та "кількість придбаних книг".
Кількість покупців та їхні дані визначаються випадковим чином."""
# "adress": f"{random.randint(1, 100)} вул. {random.choice(["Спортивна",
# "Миру", "Героїв танкістів", "Тараса Шевченка", "Гоголя"])}"


def gen_customers(num_customers):
    name_list = ["Олександр", "Оксана", "Дмитро", "Максим", "Ірина", "Софія"]
    surname_list = ["Агаштон", "Радченко", "Клименко", "Савчук", "Науменко",
                    "Єрмоленко"]

    customers = [
        {
            "name": random.choice(name_list),
            "surname": random.choice(surname_list),
            "adress": str(random.randint(1, 100)) + " вул. "
                      + random.choice(["Спортивна", "Миру", "Героїв танкістів",
                                       "Тараса Шевченка", "Гоголя"]),
            "count_of_books": random.randint(1, 20)
        }
        for _ in range(num_customers)
    ]
    return customers


def num_of_books(customers):
    return sum(customer["count_of_books"] for customer in customers)


def max_books(customers, n):
    return [customer for customer in customers if customer["count_of_books"]
            > n]


num_customers = 10
customers_list = gen_customers(num_customers)
print("Інформація про покупців: ")
for customer in customers_list:
    print(customer)

sum_of_books = num_of_books(customers_list)
print(f"\nЗагальна кількість придбаних книг: ")

n_books = 3
selected_customers = max_books(customers_list, n_books)
print(f"\nПокупці які придбали більше ніж {n_books} книги:")
for customer in selected_customers:
    print(customer)
"""Генерує список покупців з випадковими даними."""
"""Знаходить загальну кількість придбаних книг усіма покупцями."""
"""Знаходить покупців, які придбали більше ніж n книг."""
# Генеруємо список покупців
# Виводимо дані про покупців
# Знаходимо та виводимо загальну кількість придбаних книг
# Знаходимо та виводимо покупців, які придбали більше ніж 3 книги
