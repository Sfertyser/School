from datetime import datetime, timedelta
# try:
#     choice = int(input("Введіть номер завдання(1-5): "))
#     while choice <= 0 or choice >= 6:
#         choice = int(input("Помилка, введіть номер завдання(1-5): "))
#     match choice:
#
#         case 1:  # Обчислення віку
#             current_year = datetime.now().year
#             year_of_birth = int(input("Введіть рік вашого народження: "))
#             if 1900 < year_of_birth <= current_year:
#                 age = current_year - year_of_birth
#                 print(f"Ваш вік: {age} років")
#             else:
#                 print("Помилка, ви вказали неправильний рік народження.")
#
#         case 2:  # Тривалість подорожі
#             start_time = input("Введіть час початку подорожі (ГГ:ХХ): ")
#             end_time = input("Введіть час завершення подорожі (ГГ:ХХ): ")
#             format_str = '%H:%M'
#             start_datetime = datetime.strptime(start_time, format_str)
#             end_datetime = datetime.strptime(end_time, format_str)
#             duration = end_datetime - start_datetime
#             hours = duration.seconds // 3600
#             minutes = (duration.seconds % 3600) // 60
#             print(f"Тривалість подорожі: {hours} годин {minutes} хвилин")
#
#         case 3:  # Облік терміну дії продукту
#             input_date = input("Введіть дату виробництва (РРРР-ММ-ДД): ")
#             production_date = datetime.strptime(input_date, "%Y-%m-%d")
#             expiry_days = int(input("Введіть термін придатності у днях: "))
#             expiry_date = production_date + timedelta(days=expiry_days)
#             print(f"Продукт буде придатний до:"
#                   f" {expiry_date.strftime('%Y-%m-%d')}")
#
#         case 4:  # Розрахунок терміну виконання завдань
#             start_date_str = input("Введіть дату початку проекту"
#                                    " (у форматі РРРР-ММ-ДД): ")
#             start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
#             duration = int(input("Введіть кількість днів на виконання: "))
#             end_date = start_date + timedelta(days=duration)
#             print(f"Дата завершення проекту: {end_date.strftime('%Y-%m-%d')}")
#
#         case 5:  # Час до наступного святкування
#             birthday_str = input("Введіть свою дату народження у форматі"
#                                  " (РРРР-ММ-ДД): ")
#             birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
#             current_date = datetime.now()
#             next_birthday = birthday.replace(year=current_date.year)
#             if next_birthday < current_date:
#                 next_birthday = next_birthday.replace(
#                     year=current_date.year + 1)
#             time_remaining = next_birthday - current_date
#             print(f"Час до наступного святкування вашого дня народження:"
#                   f" {time_remaining.days} днів,"
#                   f" {time_remaining.seconds // 3600} годин,"
#                   f" {(time_remaining.seconds // 60) % 60} хвилин,"
#                   f" {time_remaining.seconds % 60} секунд")
#
# except MemoryError as e:
#     print(f"{str(e)}, у вас недостатньо оперативної пам'яті щоб запустити цю "
#           "програму.")
# except FileNotFoundError as e:
#     print(f"{str(e)}, програма не може отримати доступ до файлу.")
# except OverflowError as e:
#     print(f"{str(e)}, межу допустимих значень було перевищено.")
# except PermissionError as e:
#     print(f"{str(e)},у вас немає необхідних прав доступу для виконання певної"
#           "операції")
# except TypeError as e:
#     print(f"{str(e)}, перевірте правильність типів даних.")
# except ValueError as e:
#     print(f"{str(e)}, перевірте правильність введених даних.")
# except Exception as e:
#     print(f"Виникла помилка: {str(e)}")


# def time(datestr1, datestr2):
#     dateformat = "%Y-%m-%d"
#     date1 = datetime.strptime(datestr1, dateformat)
#     date2 = datetime.strptime(datestr2, dateformat)
#     delta = date2 - date1
#     days = delta.days
#     hours, remainder = divmod(delta.seconds, 3600)
#     minutes, _ = divmod(remainder, 60)
#     return f"{days}, {hours}, {minutes}"
#
#
# date1 = "2020-01-01"
# date2 = "2020-02-01"
# print(time(date1, date2))


"""Написати функцію для перевірки чи є введена дата вихідним днем?
(Субота або Неділля)"""


# def time(date):
#     dateformat = "%Y-%m-%d"
#     date1 = datetime.strptime(date, dateformat)
#     return date1.weekday() in [5, 6]
#
#
# date1 = "2024-02-03"
# print(time(date1))


"""Написати функцію яка приймає дату народження і повертає кількість днів до 
наступного дня народження (Обов'язкова умова використовувати поточний день)"""


# def time(dobstr):
#     dateformat = "%Y-%m-%d"
#     today = datetime.now()
#     dob1 = datetime.strptime(dobstr, dateformat).replace(year=today.year)
#
#     if today > dob1:
#         dob1 = dob.replace(year=today.year + 1)
#
#     delta = dob1 - today
#     return delta.days
#
#
# dob = "2009-07-09"
# print(time(dob))


"""Перевірка на високосний вік"""


# def strange_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#
#
# year_now = 2024
# print(strange_year(year_now))
