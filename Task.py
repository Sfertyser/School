# 1
# def numbers(a, b):
#     return a + b
#
#
# a, b = 2, 8
# sum = numbers(a, b)
# print(sum)

# 2
# def paired(number2):
#     if number2 % 2 == 0:
#         return "Число є парним"
#     else:
#         return "Число не є парним"
#
#
# number = 18
# pair = paired(number)
# print(pair)

# 3
# def function(a2, b2, c2):
#     return max(a2, b2, c2)
#
#
# a, b, c = 29, 8, 15
# max2 = function(a, b, c)
# print(max2)

# 4
# def function(number2):
#     if number2 == 0:
#         return 1
#     else:
#         return number2 * function(number2 - 1)
#
#
# number = 6
# factorial = function(number)
# print(f"Факторіал числа {number} = {factorial}")

# 5
# def function(text):
#     text2 = text.capitalize()
#     return text2


# def function(text):
#     return text.title()


# text = "hello world!"
# text_new = function(text)
# print(text_new)

# 6
# def function(text):
#     reversed_string = ""
#     for char in text:
#         reversed_string = char + reversed_string
#     return reversed_string

# def function(text):
#     reversed_string = text[::-1]
#     return reversed_string


# text = "hello world!"
# text3 = function(text)
# print(text3)

# 7
# def function():
#     if text == text[::-1]:
#         return "Так"
#     else:
#         return "Ні"
#
#
# text = "anna"
# polyndrom = function()
# print(polyndrom)

# 8
# def function():
#     letter_count = 0
#     for char in text:
#         if char == letter:
#             letter_count += 1
#     return letter_count
#
#
# text = "hello world!"
# letter = "o"
# letters = function()
# print(f"Літера {letter} зустрічається у тексті {text}, {letters} разів")

# 9
# def function(spisok):
#     spisok2 = []
#     for element in spisok:
#         if element not in spisok2:
#             spisok2.append(element)
#     return spisok2
#
#
# spisok = ["Картопля", "Томат", "Морква", "Морква"]
# final_list = function(spisok)
# print(final_list)

# 10
# def function(spisok):
#     spisok.sort()
#     return spisok
#
#
# spisok = [8, 4, 2, 6, 5, 9, 7, 1, 3]
# sorted_spisok = function(spisok)
# print(f"Відсортований список: {sorted_spisok}")

""" ~#> Функції зі змінним числом аргументів:
Написати функцію sum_all, що приймає довільне число аргументів і повертає їхню
суму.
Написати функцію print_all, що приймає довільне число аргументів і друкує їх на
екран (у консоль)
Написати функцію average, що приймає довільну кількість аргументів і повертає
їхнє середнє значення.
~#> Рекурсивні функції:
Написати рекурсивну функцію factorial, що приймає число і повертає його
факторіал.
Написати рекурсивну функцію fibonacci, що приймає число і повертає n-е число
Фібоначчі.
Написати рекурсивну функцію gcd, що приймає два числа і повертає їхній
найбільший спільний дільник. """
# 1
# def sum_all(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
#
# print(sum_all(4, 6, 7, 9, 3,5))

# 2


# def print_all(*args):
#     for arg in args:
#         if arg == None:
#             print(" ")
#         else:
#             print(arg)
#     return None
#
#
# print(print_all(2, 6, 5, 7, 3, 9))

# 3
# Написати функцію average, що приймає довільну кількість аргументів і повертає
# їхнє середнє значення.
# def average(*args):
#     if not args:
#         return None
#     sum = 0
#     for arg in args:
#         sum += arg
#     return sum / len(args)
#
#
# print(average(4, 7, 14, 67))

# 4
# Написати рекурсивну функцію factorial, що приймає число і повертає його
# факторіал.
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
#
#
# print(factorial(6))

# 5
# Написати рекурсивну функцію fibonacci, що приймає число і повертає n-е число
# Фібоначчі.
# def fibonacci(num):
#     num = num - 1
#     if num + 1 <= 1:
#         return num
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)
#
#
# print(fibonacci(7))

# 6
# Написати рекурсивну функцію gcd, що приймає два числа і повертає їхній
# найменшим спільний дільник. """
# def gcd(arg1, arg2):
#     if arg2 == 0:
#         return arg1
#     else:
#         return gcd(arg2, arg1 % arg2)
#
#
# print(gcd(3, 9))
