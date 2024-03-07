import random
import string
from datetime import datetime, timedelta
# 1. Вивести числа від 1 до 10
# 2. Вивести числа від 10 до 1 в зворотному порядку
# 3. Вивести всі парні числа від 1 до 20
# 4. Вивести суму чисел від 1 до 100
# 5. Вивести добуток чисел від 1 до 5
# 6. Знайти факторіал числа 5
# 7. Вивести всі числа Фібоначчі до 50
# 8. Вивести всі дільники числа 12
# 9. Перевірити, чи є число 17 простим
# 10. Знайти найменше спільне кратне чисел 12 і 18
# 11. Вивести таблицю множення для числа 7
# 12. Вивести шахівницю з символів 'X' і 'O'
# 13. Згенерувати 10 випадкових чисел від 1 до 100
# 14. Згенерувати 5 випадкових слів з 5 букв
# 15. Створити список з 10 чисел, потім видалити всі парні числа з нього

# print("1. Вивести числа від 1 до 10")
# for i in range(1, 11):
#     print(i, end=" ")
# print()

# print("2. Вивести числа від 10 до 1 в зворотному порядку")
# for i in range(10, 0, -1):
#     print(i, end=" ")
# print()

# print("3. Вивести всі парні числа від 1 до 20")
# for i in range(2, 22, 2):
#     print(i, end=" ")
# print()

# print("4. Вивести суму чисел від 1 до 100")
# num = 0
# for i in range(1, 101):
#     num += i
# print(num)

# print("5. Вивести добуток чисел від 1 до 5")
# num2 = 1
# for i in range(1, 6):
#     num2 *= i
# print(num2)

# print("6. Знайти факторіал числа 5")
# num3 = 1
# for i in range(1, 6):
#     num3 *= i
# print(num3)

# print("7. Вивести всі числа Фібоначчі до 50")
# a, b = 0, 1
# while b <= 50:
#     print(a, end=" ")
#     a, b = b, a+b
# print()

# print("8. Вивести всі дільники числа 12")
# for i in range(1, 13):
#     if 12 % i == 0:
#         print(i, end=" ")

# print("9. Перевірити, чи є число 17 простим")
# for i in range(2, 17):
#     if 17 % i == 0:
#         print("Ні, число 17 не є простим")
#     else:
#         print("Число 17 є простим")
#         break

# print("10. Знайти найменше спільне кратне чисел 12 і 18")
# for i in range(1, 13):
#     if 12 and 18 % i == 0:
#         print(f"Найменшим спільним кратним числа 12 і 18 є {i}")
#         break

# i = 1
# while i % 12 != 0 or i % 18 != 0:
#     i += 1
# print(i)

# print("11. Вивести таблицю множення для числа 7")

# for i in range(1, 11):
#     print(f"7 * {i} = {7 * i}")
# print("12. Вивести шахівницю з символів 'X' і 'O'")

# size = 6
# for i in range(size):
#     for j in range(size):
#         if (i + j) % 2 == 0:
#             print('X', end=' ')
#         else:
#             print('O', end=' ')
#     print()

# print("13. Згенерувати 10 випадкових чисел від 1 до 100")
#
# random_numbers = [random.randint(1, 100) for _ in range(10)]
# print(f"10 випадкових чисел від 1 до 100: {random_numbers}")

# print("14. Згенерувати 5 випадкових слів з 5 букв")
#
# random_words = [''.join(random.choices(string.ascii_lowercase, k=5))
#                 for _ in range(5)]
# print(f"5 випадкових слів з 5 букв: {random_words}")

print("15. Створити список з 10 чисел,потім видалити всі парні числа з нього")

numbers = [22, 34, 97, 89, 41, 56, 78, 91, 13, 65]
print(f"Список до видалення парних чисел: {numbers}")
numbers = [num for num in numbers if num % 2 != 0]
print(f"Список після видалення парних чисел: {numbers}")
