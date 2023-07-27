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
# symbol = 0
# for char in email:
#     if char == "@":    # Перевіряє чи більше 1 собаки є в змінній.
#         symbol += 1
#         if symbol > 1:
#             print("Помилка, ви ввели більше 1 собаки.")
#             exit()
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
# meters = input("Введіть кількість метрів: ")
# symbols = 0
# for char in meters:
#     if not (char.isdigit() or char == '.'):    # Перевіряє чи є в змінній щось окрім чисел або крапки.
#         print("Помилка, ви ввели щось окрім чисел або крапки.")
#         exit()
#     if char == ".":    # Перевіряє чи більше 1 крапки є в змінній.
#         symbols += 1
#         if symbols > 1:
#             print("Помилка, ви ввели більше 1 крапки.")
#             exit()
# if symbols == 0:    # Переводить змінну в інший тип данних за кількістю крапок.
#     meters = int(meters)
# else:
#     meters = float(meters)
# print("Варіанти: милі дюйми ярди.")
# user_select = input("В яку одиницю довжини перевести: ")
# match user_select:
#     case "милі":
#         print(f"З {meters} метрів виходить {meters * 0.000621371} миль.")
#     case "дюйми":
#         print(f"З {meters} метрів виходить {meters * 39.37} дюймів.")
#     case "ярди":
#         print(f"З {meters} метрів виходить {meters * 1.09361} ярдів.")
#     case _:
#         print("Помилка, ви ввели щось не так.")

# Task 5
# try:
#     day = int(input("Введіть день тижня: "))
#     match day:
#         case 1:
#             print("Понеділок")
#         case 2:
#             print("Вівторок")
#         case 3:
#             print("Середа")
#         case 4:
#             print("Четвер")
#         case 5:
#             print("П`ятниця")
#         case 6:
#             print("Субота")
#         case 7:
#             print("Неділя")
#         case _:
#             print("Помилка, ви ввели не те число.")
# except ValueError as error:
#     print("Помилка, ви ввели текст або символи.")
# except Exception as error:
#     print("Помилка!")

# Task 6
# try:
#     num1 = float(input("Введіть перше число: "))
#     num2 = float(input("Введіть друге число: "))
#     if num1 == num2:
#         print("Числа однакові.")
#     else:
#         min_num = min(num1, num2) # Шукає менше число
#         max_num = max(num1, num2) # Шукає більше число
#         print(f"Числа у порядку зростання:{min_num}, {max_num}")
# except ValueError as error:
#     print("Помилка, ви ввели щось окрім цілих або дробових чисел.")

# Task 7
# try:
#     num1 = float(input("Введіть перше число: "))
#     num2 = float(input("Введіть друге число: "))
#     operation = input("Введіть математичну дію (+, -, *, /): ")
#     match operation:
#         case '+':
#             result = num1 + num2
#         case '-':
#             result = num1 - num2
#         case '*':
#             result = num1 * num2
#         case '/':
#             if num1 == 0 or num2 == 0:
#                 print("Помилка, ділити на нуль не можна.")
#                 exit()
#             else:
#                 result = num1 / num2
#         case '_':
#             print("Помилка, ви ввели неправильну дію.")
#     print(f"Результат:{result}")
# except ValueError as error:
#     print("Помилка, введіть цілі або дробові числа.")

# Task 1 New
# text = input("Введіть рядок: ")
# symbols = "~!@#$%^&*()_-+={[}]|\:;\"'<,>.?/ "
# symbols2 = 0
# numbers = 0
# words = 0
# for char in text:
#     if char in symbols: # Перевіряє чи символ з'являється в змінній зі спец символами.
#         symbols2 += 1
#     if char.isdigit():
#         numbers += 1
#     else:
#         words += 1
# print(f"Кількість цифр:{numbers} Кількість літер:{words - symbols2}.")

# Task 2 New
# text = input("Введіть рядок: ")
# symbol = input("Введіть один символ для пошуку: ")
# while len(symbol) != 1:
#     symbol = input("Помилка, введіть один символ для пошуку: ")
# count = 0
# for char in text:
#     if char == symbol:
#         count += 1
# print(f"Символ {symbol} зустрічається {count} разів в {text}")

# Task 3 New
# text = input("Введіть рядок: ")
# while len(text) < 1:
#     text = input("Помилка, введіть рядок: ")
# search = input("Введіть слово для пошуку: ")
# replace = input("Введіть слово для заміни: ")
# result = text.replace(search, replace)
# print(f"Новий рядок: {result}")

# Task 4 New
# text = input("Введіть рядок: ")
#
# # Спершу виведіть третій символ цього рядка.
# print(f"Третій символ: {text[2]}")
#
# # У другому рядку виведіть передостанній символ цього рядка.
# print(f"Передостанній символ: {text[-2]}")
#
# # У третьому рядку виведіть перші п'ять символів цього рядка.
# print(f"Перші п'ять символів: {text[:5]}")
#
# # У четвертому рядку виведіть весь рядок, крім двох останніх символів.
# print(f"Весь рядок окрім останніх двох символів: {text[:-2]}")
#
# # У п'ятому рядку виведіть усі символи з парними індексами
# print(f"Усі символи з парними індексами: {text[::2]}")
#
# # У шостому рядку виведіть усі символи з непарними індексами
# print(f"Усі символи з непарними індексами: {text[1::2]}")
#
# # У сьомому рядку виведіть усі символи у зворотному порядку.
# print(f"Усі символи у зворотному порядку: {text[::-1]}")
#
# # У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
# print(f"Усі символи у зворотному порядку, починаючи з останнього: {text[-1::-1]}")
#
# # У дев'ятому рядку виведіть довжину цього рядка.
# print(f"Довжина рядка: {len(text)}")

# Task 5
print("Закічнувати речення потрібно з крапкою та пробілом після крапки.")
text = input("Введіть речення: ")
if text and text[0].isalpha():
    text = text[0].upper() + text[1:]
for i in range(1, len(text)):
    if text[i - 2] == '.' and text[i].isalpha():
        text = text[:i] + text[i].upper() + text[i + 1:]
print(text)
