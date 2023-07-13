# Task 1
# text = input("Введіть текст: ")
# text2 = ""
# for char in text:
#     if not char.isdigit():
#         text2 += char
# print(text2)

# Task 2
# email = input("Введіть електронну пошту: ")
# if "@" in email and "." in email:
#     print("YES")
# else:
#     print("NO")

# Task 2 optimized
# email = input("Введіть електронну пошту: ")
# print("YES") if "@" in email and "." in email else print("NO")


# Task 3
# a = 1
# b = 2
# c = 3
# user_select = input()
# match user_select:
#     case "min":
#         print(min(a, b, c))
#     case "max":
#         print(min(a, b, c))
#     case "avg":
#         print(f"Середньоарифметичне трьох чисел - {( a + b + c) / 3}")


# Task 4
# Ця програма переводить метри в іншу одиницю довжини.
meters = input("Введіть кількість метрів: ")
symbols = 0
for char in meters:
    if not (char.isdigit() or char == '.'):    # Перевіряє чи є в змінній щось окрім чисел або крапки.
        print("Помилка, ви ввели щось окрім чисел або крапки.")
        exit()
    if char == ".":    # Перевіряє чи більше 1 крапки є в змінній.
        symbols += 1
        if symbols > 1:
            print("Помилка, ви ввели більше 1 крапки.")
            exit()
if symbols == 0:    # Переводить змінну в інший тип данних за кількістю крапок.
    meters = int(meters)
else:
    meters = float(meters)
print("Варіанти: милі дюйми ярди.")
user_select = input("В яку одиницю довжини перевести: ")
match user_select:
    case "милі":
        print(f"З {meters} метрів виходить {meters * 0.000621371} миль.")
    case "дюйми":
        print(f"З {meters} метрів виходить {meters * 39.37} дюймів.")
    case "ярди":
        print(f"З {meters} метрів виходить {meters * 1.09361} ярдів.")
    case _:
        print("Помилка, ви ввели щось не так.")
