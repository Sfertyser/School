import math
import random
import string

# 1
# Написати функцію fizzbuzz, яка приймає число n і друкує числа від 1 до n,
# замінюючи числа, кратні 3, на "Fizz", кратні 5 - на "Buzz",
# а кратні 3 і 5 - на "FizzBuzz".


# def fizzbuzz(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
#
#
# n = 15
# fizzbuzz(n)


# 2
# Написати функцію calculate_area, що приймає тип фігури (коло, квадрат,
# трикутник) і повертає їхню площу та периметр.
# def calculate_area(shape, *args):
#     if shape == "Коло":
#         radius = args[0]
#         area = math.pi * radius**2
#         perimeter = 2 * math.pi * radius
#         return area, perimeter
#     elif shape == "Квадрат":
#         side_length = args[0]
#         area = side_length ** 2
#         perimeter = 4 * side_length
#         return area, perimeter
#     elif shape == "Трикутник":
#         a, b, c = args
#         s = (a + b + c) / 2
#         area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#         perimeter = a + b + c
#         return area, perimeter
#
#
# circle_area, circle_perimeter = calculate_area("Коло", 3)
# print(f"Площа кола: {circle_area}")
# print(f"Периметр кола: {circle_perimeter}")
# print("")
#
# square_area, square_perimeter = calculate_area("Квадрат", 4)
# print(f"Площа квадрата: {square_area}")
# print(f"Периметр квадрата: {square_perimeter}")
# print("")
#
# triangle_area, triangle_perimeter = calculate_area("Трикутник", 3, 4, 5)
# print(f"Площа трикутника: {triangle_area}")
# print(f"Периметр трикутника: {triangle_perimeter}")

# 3
# Написати функцію convert_to_celsius або convert_to_fahrenheit, що здійснює
# конвертацію введеного числа градусів за шкалою Цельсія або Фаренгейта
# (наприклад, було в Цельсії, а у Фаренгейті - n градусів).
# def convert_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9 / 5) + 32
#     return fahrenheit
#
#
# celsius_input = float(input("Введіть температуру у градусах Цельсія: "))
# fahrenheit_output = convert_to_fahrenheit(celsius_input)
# print(f"Температура у Фаренгейтах: {fahrenheit_output}")

# 4
# Написати функцію validate_email, що приймає рядок і повертає True,
# якщо e-mail правильний (може існувати, не обов'язково існує),
# і False у протилежному випадку.
# def validate_email(email):
#     parts = email.split("@")
#     if len(parts) != 2:
#         return False
#     local_part, domain_part = parts
#     if not local_part or not domain_part:
#         return False
#     if "." not in domain_part:
#         return False
#     for part in domain_part.split("."):
#         if not part:
#             return False
#     return True
#
#
# print(validate_email("example@mail.com"))

# 5
# Написати функцію generate_password, що генерує випадковий пароль заданої
# довжини.


# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = "".join(random.choice(characters) for _ in range(length))
#     return password
#
#
# password_length = 12
# random_password = generate_password(password_length)
# print(f"Випадковий пароль: {random_password}")

# 6
# Написати функцію shuffle_list, що перемішує елементи списку.
# def shuffle_list(lst):
#     shuffled_lst = lst[:]
#     random.shuffle(shuffled_lst)
#     return shuffled_lst
#
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# shuffled = shuffle_list(my_list)
# print(f"Оригінальний список: {my_list}")
# print(f"Перемішаний список: {shuffled}")

# 7
# Написати функцію find_duplicates, яка знаходить елементи, що повторюються,
# у списку.


# def find_duplicates(lst):
#     seen = set()
#     duplicates = set()
#     for item in lst:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)
#     return list(duplicates)
#
#
# my_list = [4, 2, 1, 4, 1, 3, 5, 6]
# print(f"Список: {my_list}")
# print(f"Елементи що повторюються: {find_duplicates(my_list)}")

# 8
# Написати функцію most_frequent_word, яка знаходить слово, що найчастіше
# зустрічається в тексті.


# def most_frequent_word(text):
#     words = text.split()
#     word_count = {}
#     for word in words:
#         word = word.lower()
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     most_frequent = max(word_count, key=word_count.get)
#     return most_frequent
#
#
# text = "Цей текст має деякі слова. Деякі з них повторюються частіше ніж інші."
# print(f"Слово, що найчастіше зустрічається: {most_frequent_word(text)}")
