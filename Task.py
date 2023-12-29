from datetime import datetime
"""
Розрахунок різниці між датами

Напишіть програму, яка приймає введення користувача у вигляді двох дат в форматі
"YYYY-MM-DD". Розрахуйте та виведіть на екран різницю в днях між цими датами.

Вимоги до програми:

1. Використайте бібліотеку datetime для роботи з датами.
2. Запитуйте користувача про введення двох дат.
3. Розрахуйте різницю між цими датами.
4. Виведіть на екран кількість днів, яка розділяє ці дві дати.

Обидві ці задачі дозволять вам використовувати бібліотеку datetime
для роботи з часовими та датовими даними в Python.
"""


def difference(input_date_str1, input_date_str2):
    user_date1 = (datetime.strptime(input_date_str1, "%Y-%m-%d"))
    user_date2 = (datetime.strptime(input_date_str2, "%Y-%m-%d"))
    days_left = abs((user_date2 - user_date1).days)
    print(f"Різниця між днями складає {days_left} днів.")


user_date1 = input("Введіть першу дату у форматі (YYYY-MM-DD): ")
user_date2 = input("Введіть другу дату у форматі (YYYY-MM-DD): ")
difference(user_date1, user_date2)
