from datetime import datetime
from datetime import timedelta
""" Створення об'єкту datetime з доточною датою та часом."""
# now = datetime.now()
# print(f"Поточна дата та час: {now}")

""" Створюємо об'єкт datetime з вказаною датою та часом."""
# date_time = datetime(2023, 12, 22, 17, 11, 58)
# print(f"Вказана дата та час: {date_time}")

""" Методи datetime:
1. year, month, day: Отримання окремих компонентів дати.
2. hour, minute, second: Отримання окремих компонентів часу.
3. strftime(format): Форматування дати та часу в рядок
з використанням заданого формату."""

# now = datetime.now()
# print("Рік:", now.year)
# print("Місяць:", now.month)
# print("Число:", now.day)
# print("Години:", now.hour)
# print("Хвилини:", now.minute)
# print("Секунди:", now.second)
#
# format_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(f"Форматована дата та час: {format_date}")

""" Робота з інтервалами часу (timedelta)"""
# Створюємо timedelta з 5 днями, 7 годинами, 45 хвилинами.
# delta_days = timedelta(days=5, hours=7, minutes=45)
# print(delta_days)

# Створюємо timedelta з 3600 секундами (1 година).
# delta_seconds = timedelta(seconds=3600)
# print(delta_seconds)

""" Операції з timedelta"""
# now = datetime.now()

# Створюємо timedelta з 8 днями.
# delta = timedelta(days=8)

# Добавляємо delta до поточної дати.
# new_date = now + delta
# print(f"Дата через 8 днів: {new_date}")

""" Атрибути timedelta
timedelta має кілька атрибутів, які надають інформацію про його значення:

1. days: Кількість днів в інтервалі.
2. seconds: Кількість секунд в інтервалі (не включаючи дні).
3. microseconds: Кількість мікросекунд в інтервалі
(не включаючи дні та секунди)."""

# print(f"Днів у delta: {delta.days}")
# print(f"Секунд у delta: {delta.seconds}")
# print(f"Мікросекунд у delta: {delta.microseconds}")


""" Приклад використання timedelta для обчислення різниці між двома датами"""
# date_str1 = "2023-12-22"
# date_str2 = "2021-05-02"
#
# date_format = "%Y-%m-%d"
# date1 = datetime.strptime(date_str1, date_format)
# date2 = datetime.strptime(date_str2, date_format)
#
# difference = date1 - date2
# print(f"Дата 1: {date1}")
# print(f"Дата 2: {date2}")
# print(f"Різниця між датами: {difference.days} днів.")
