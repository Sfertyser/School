# Тернарний оператор
# number = 10
# text = ""
# if number % 2 == 0:
#     text = "парним"
# else:
#     text = "не парним"
# text = "парним" if number % 2 == 0 else "не парним"
# print(f"{number} є {text}")

# Робота над помилками
# month = int(input("Введіть місяць: "))
#   Через while not
# while not 1 <= month <= 12:
#     print("не вірний місяць")
#     month = int(input("Введіть місяць: "))
# print("Все вірно")
# print(type(month))
#   Через range
# while month not in range(1, 13):
#     print("не вірний місяць")
#     month = int(input("Введіть місяць: "))
# print("Все вірно")

name = "Oleksandr"
number = 13
if number == 13:
    print(name)
else:
    print(number)
