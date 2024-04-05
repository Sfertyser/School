import datetime
from datetime import date

# 1
# current_date = datetime.date.today()
# birthday = datetime.date(2009, 7, 9)
# date = current_date - birthday
# date = date.days
# print(f"Різниця днів: {date}")

# 2
# a1 = datetime.date(2030, 11, 24)
# a2 = datetime.timedelta(days=100)
# a3 = a1 + a2
# print(f"{a3}")

# 3
# date1 = datetime.date(2024, 3, 7)
# is_leap = date1.is_leapyear()
# if date1.year % 4 == 0:
#     print("Цей рік є високосним")
# else:
#     print("Цей рік не є високосним")

# 4
# 1. Знайдіть дату, яка була 30 днів тому.
# current_date = datetime.date.today()
# other_date = datetime.timedelta(days=30)
# new_date = current_date - other_date
# print(current_date)
# print(new_date)

# 2Визначте чи є даний момент часу (час та дата) в межах заданого проміжку часу.
# start_date = datetime.datetime(2020, 9, 4, 12, 46)
# end_date = datetime.datetime(2024, 10, 17, 3, 8)
# current_date = datetime.datetime.now()
# time = current_date >= start_date and current_date <= end_date
# if time:
#     print("Так")
# else:
#     print("Ні")


# def is_leap_year(year):
#   try:
#     date(year, 2, 29)
#     return True
#   except ValueError:
#     return False
#
#
# year = 2024
#
# if is_leap_year(year):
#   print(f"Рік {year} - високосний.")
# else:
#   print(f"Рік {year} - не високосний.")
