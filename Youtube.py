# string methods
# name = "oleksandr"
# print(len(name))
# print(name.find("k"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("e","a"))
# print(name*3)

# math functions
# import math
# pi = 3.14
# x = 1
# y = 2
# z = 3
# print(round(pi)) rounds number.
# print(math.ceil(pi)) rounds number up.
# print(math.floor(pi)) rounds number down.
# print(abs(pi)) turns negative number into positive.
# print(pow(pi,2)) multiples first number by itself set amount of times.
# print(math.sqrt(pi)) writes a square of number.
# print(max(x,y,z)) writes max value of numbers from targeted.
# print(min(x,y,z)) writes min value of numbers from targeted.

# string slicing
# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]
# name = "Klimenko Oleksandr"
# first_name = name[:8]
# last_name = name[9:18]
# funky_name = name[::2]
# reverse_name = name[::-1]

# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
# slice = slice(7, -4)
# print(website1[slice])
# print(website2[slice])
import random
# Блок для створення матриці 10x10 та заповнення рандомними числами.
matrix = [[random.randint(10, 99) for _ in range(10)] for _ in range(10)]  # Створює матрицю.
print("Матриця:")  # Виводимо матрицю
for row in matrix:  # Звертаємося до кожного рядка в матриці.
    print(row)  # Виводимо на екран матрицю.

swap_column1 = int(input("Введіть номер стовпця який ви хочете замінити (0-9): "))
swap_column2 = int(input("Введіть номер стовпця яким ви заміните його (0-9): "))
if swap_column1 == swap_column2 or swap_column2 == swap_column1:
    print("Помилка, ви ввели однакові рядки")
else:
    if 0 <= swap_column1 < 10 and 0 <= swap_column2 < 10:
        for i in range(10):
            matrix[i][swap_column1], matrix[i][swap_column2] = matrix[i][swap_column2], matrix[i][swap_column1]
        print("Матриця після обміну рядків:")  # Виводимо змінену матрицю.
        for row in matrix:
            print(row)
    else:
        print("Помилка, ви ввели число не в діапазоні матриці.")
