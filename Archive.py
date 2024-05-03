import random
# print(random.randint(1, 10))
""" Виводить рандомне число від 1 до 10 включно"""
# name = "Oleksandr"
# print("Hello " + name)
""" Потрібна для з'єднання текста зі змінною """
# print('#####', '#####' + '#####' + '#####', "#####", sep='\n')
""" sep='\n' потрібна щоб кожний раз виводило на нову строку.
Коми для нового рядку. Плюси для з'єднування текстів """
# print('#\n#####\n' * 5)
""" Можна так записати і помножити щоб повторювалося """
# text = 'asjkdausfioquwrioquwroiqwrtuioqwr  '
# print(len(text))
""" Показує кількість символів в тексті (Пробіли також рахуються) """
# reports = [1, 2, 3, 4, 5, 6]
# done_reports = [1, 2, 3]
# 01234567891011
""" Пов'язано з len """
# text = 'Hello world!'
# card = '1111 1111 1111 1234'
# print(len(text))
""" довжина текста """
# print(text[0])
""" Показує 1 символ """
# print(text[14])
""" Видасть помилку бо недостатньо символів в тексті """
# print(text[-2])
""" Числа з мінусами видають символи з кінця """
# print(text[len(text) - 4]
#        + text[len(text) - 3]
#        + text[len(text) - 2]
#        + text[len(text) - 1])
""" Видають разом текст з кінця """
# range(від, до, крок) # 0, 1, 2, 3 ,4 ,5, 6, 7, 8, 9
# print(text)
# print(text[0:len(text):2])
""" Виведе тільки символи які не діляться на два """
# print(text[len(text):0:-1])
""" Виведе текст навпаки без 1 символу """
# print(text[6:])
""" Виведе текст після 6 символу """
# print(text[:5])
""" Виведе текст до 5 символу """
# print(text[::-1])
""" Виведе текст навпаки """
# text = 'Hello world world'
# print( len(text) )  # Функція - що це?
"""  Показує кількість символів"""
# print(text.find('w', 7, 12))  # Метод - що це?
# print(text.rfind('w', 7, 12))  # Метод
""" Не до кінця зрозумів як працює але воно шукає символ в тексті """
# print(text[6])
""" виводить символ на 1 більший за вказаний """
# print(text.find('123'))
""" знаходить в тексті 123 """
# print(text.index('123'))
#
# url = 'https://google.com'
# find_is_valid_url = url.find('https') != -1 and url.find('.com') != -1
# is_valid_url = url.startswith('https') and url.endswith('.com')
""" Перевіряє щоб посилання починалося на https і закінчувалося .com """
# print(f'Find: {find_is_valid_url}')
# print(f'swith: {is_valid_url}')
""" Виводить чи є посиланя і чи працює посилання """
# string = '-12345'
# if string[0] == '-' and string[1:].isdigit():
#     number = int(string)
#     print(number)
# elif string.isdigit():
#     number = int(string)
#     print(number)
# else:
#     print('Error')
""" Якщо 1 символ - і 2 символ це число тоді 
Інакше якщо текст це числа 
Інакше виводить помилку """
# print('Hello world'.isalpha())
# print('h1'.islower())
# print('H1'.isupper())
""" Якщо всі символи це букви тоді True інакше False (Пробіли рахуються) 
Якщо весь текст з маленьких літер тоді True
Якщо весь текст з великих літер тоді True """
"""
replace
split
strip
join
count
"""
text = 'Hello world'
# print( text.replace('l', '1').replace('o', '0') )
""" Замінює значення тексту """
# for i in range(0, len(text)):
#     print(i,'-',text[i])
""" Виводить текст у стовбчик починаючи з 1 символу """
"""
1) Len - 10
2) Upper
3) Lower
4) Number
5) Spec symbols (+, -, =, ., _, ,)
"""
# password = '123456789011g''simplepassword'
# if len(password) < 11:
#     print('Error!')
#     exit()
""" Якщо довжина паролю меньше 11 вивести помилку """
# has_upper = False
# for char in password:  #
#     if char.isupper():
#         has_upper = True
""" Якщо в паролі є великі літери тоді True """
# if not has_upper:
#     print('Error.')
#     exit()
""" Якщо великих літер немає вивести помилку """
# print('Ok!')


# Це перший прямокутний трикутник.
# n = int(input("Введiть кiлькiсть зiрочок: "))
# m = 0
# while n > 0:
#     print(" " * m + "*" * n)
#     n -= 1
#     m += 1
#
# # Це другий прямокутний трикутник.
# n = int(input("Введiть кiлькiсть зiрочок: "))
# m = 1
# while n > 0:
#     print(" " * (n - 1) + "*" * m)
#     n -= 1
#     m += 1

""" 
*****
 ****
  ***
   **
    *

    *
   **
  ***
 ****
*****
"""


# print("Введіть число:")
# number = int(input())
# print("Введіть місяць:")
# month = (input())
# print("Введіть рік:")
# year = int(input())
# if 21 <= number <= 31 and month == 'березень' or 1 <= number <= 20 and month == 'квітень':
#     print("По гороскопу ви Овен.")
# elif 21 <= number <= 30 and month == 'квітень' or 1 <= number <= 20 and month == 'травень':
#     print("По гороскопу ви Телець.")
# elif 21 <= number <= 31 and month == 'травень' or 1 <= number <= 20 and month == 'червень':
#     print("По гороскопу ви Близнюки.")
# elif 22 <= number <= 30 and month == 'червень' or 1 <= number <= 22 and month == 'липень':
#     print("По гороскопу ви Рак.")
# elif 23 <= number <= 31 and month == 'липень' or 1 <= number <= 23 and month == 'серпень':
#     print("По гороскопу ви Лев.")
# elif 24 <= number <= 31 and month == 'серпень' or 1 <= number <= 23 and month == 'вересень':
#     print("По гороскопу ви Діви.")
# elif 24 <= number <= 30 and month == 'вересень' or 1 <= number <= 23 and month == 'жовтень':
#     print("По гороскопу ви Терези.")
# elif 24 <= number <= 31 and month == 'жовтень' or 1 <= number <= 22 and month == 'листопад':
#     print("По гороскопу ви Скорпіон.")
# elif 23 <= number <= 30 and month == 'листопад' or 1 <= number <= 21 and month == 'грудень':
#     print("По гороскопу ви Стрілець.")
# elif 22 <= number <= 31 and month == 'грудень' or 1 <= number <= 20 and month == 'січень':
#     print("По гороскопу ви Козеріг.")
# elif 21 <= number <= 31 and month == 'січень' or 1 <= number <= 18 and month == 'лютий':
#     print("По гороскопу ви Водолій.")
# elif 19 <= number <= 28 and month == 'лютий' or 1 <= number <= 20 and month == 'березень':
#     print("По гороскопу ви Риби.")


# print(random.randint(1, 10))
# name = "Oleksandr"
# print('Hello ' + name)
# print('#####', '#####' + '#####' + '#####', "#####", sep='\n')
# print('#\n#####\n' * 5)
# text = 'asjkdausfioquwrioquwroiqwrtuioqwr  '
# print(len(text))
# reports = [1, 2, 3, 4, 5, 6]
# done_reports = [1, 2, 3]
# 01234567891011
# text = 'Hello world!'
# card = '1111 1111 1111 1234'
# print(len(text))
# print(text[0])
# # print(text[14])
# print(text[-2])
# print(text[len(text) - 4]
#        + text[len(text) - 3]
#        + text[len(text) - 2]
#        + text[len(text) - 1])
# range(від, до, крок) # 0, 1, 2, 3 ,4 ,5, 6, 7, 8, 9
# print(text)
# print(text[0:len(text):2])
# print(text[len(text):0:-1])
# print(text[6:])
# print(text[:5])
# print(text[::-1])
# text = 'Hello world world'
# print( len(text) )  # Функція - що це?
# print( text.find('w', 7, 12) )  # Метод - що це?
# print( text.rfind('w', 7, 12) )  # Метод
# print( text[6] )
# print(text.find('123'))
# print(text.index('123'))
# url = 'https://google.com'
# find_is_valid_url = url.find('https') != -1 and url.find('.com') != -1
# is_valid_url = url.startswith('https') and url.endswith('.com')
# print(f'Find: {find_is_valid_url}')
# print(f'swith: {is_valid_url}')
# string = '-12345'
# if string[0] == '-' and string[1:].isdigit():
#     number = int(string)
#     print(number)
# elif string.isdigit():
#     number = int(string)
#     print(number)
# else:
#     print('Error')
# print('Hello world'.isalpha())
# print('h1'.islower())
# print('H1'.isupper())
"""
replace
split
strip
join
count
"""
# text = 'Hello world'
# # print( text.replace('l', '1').replace('o', '0') )
#
# # for i in range(0, len(text)):
# #     print(i,'-',text[i])
# """
# 1) Len - 10
# 2) Upper
# 3) Lower
# 4) Number
# 5) Spec symbols (+, -, =, ., _, ,)
# """
# password = '123456789011G'  # 'simplepassword'
# if len(password) < 11:
#     print('Error!')
#     exit()
# has_upper = False
# for char in password:  #
#     if char.isupper():
#         has_upper = True
# if not has_upper:
#     print('Error.')
#     exit()
# print('Ok!')

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

# name = "Oleksandr"
# number = 13
# if False:
#     print(name)
# else:
#     print(number)

# word = input("Введіть слово: ")
# if word == word[::-1]:
#     print("+")
# else:
#     print("-")

# text = input("Введіть текст: ")
# word = input("Введіть слово: ")
# if text.count(word) >= 1:
#     print("YES")
# else:
#     print("NO")

# text = input("Введіть рядок: ")
# if text.startswith("abc"):
#     print(text.replace("abc", "www"))
# else:
#     print(text + "qqq")


# Task 1
# text = input("Введіть текст: ")
# text2 = ""
# for char in text:
#     if not char.isdigit():
#         text2 += char
# print(text2)
#
# # Task 2
# email = input("Введіть електронну пошту: ")
# if "@" in email and "." in email:
#     print("YES")
# else:
#     print("NO")
#
# # Task 2 optimized
# email = input("Введіть електронну пошту: ")
# print("YES") if "@" in email and "." in email else print("NO")
#
#
# password = input('Введіть ваш пароль: ')
# (t, y, u, i, o, p) = (0, 0, 0, 0, 0, 0)
# s = "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"
# for char in password:
#     if len(password) >= 8:
#         t = 1
#     if char.isdigit:
#         y = 1
#     if char.isupper:
#         u = 1
#     if char.islower:
#         i = 1
#     if any(char in s for char in password):
#         o = 1
# p = t + y + u + i + o
# print(f"Ваша кількість балів: {p}")
# if t == 0:
#     print("""Ваш пароль складається з менше 8 символів."
#     Краще використовувати довші паролі для більшого захисту.""")
# if y == 0:
#     print("""У Вашому паролі немає чисел.
#     Використання чисел в паролі значно підвищує його складність.""")
# if u == 0:
#     print("""У Вашому паролі немає великих літер.
#     Використання великих літер в паролі значно підвищує його складність.""")
# if i == 0:
#     print("""У Вашому паролі немає маленьких літер.
#     Використання маленьких літер в паролі значно підвищує його складність.""")
# if o == 0:
#     print("""У Вашому паролі немає ніяких знаків.
#     Використання знаків в паролі значно підвищує його складність.""")
# if p == 5:
#     print("Ваш пароль пройшов всі перевірки, ви молодець.")


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
# print(f"Усі символи у зворотному порядку, починаючи з останнього: {text[-1::-1]}") # Незнаю як зробити.
#
# # У дев'ятому рядку виведіть довжину цього рядка.
# print(f"Довжина рядка: {len(text)}")

# Task 5 New
# print("Закічнувати речення потрібно з крапкою та пробілом після крапки.")
# text = input("Введіть речення: ")
# if text[0].isalpha():
#     text = text[0].upper() + text[1:]
# for a in range(1, len(text)):
#     if text[a - 2] == '.' and text[a].isalpha():
#         text = text[:a] + text[a].upper() + text[a + 1:]
# count = 0
# symbols = "~!@#$%^&*()_-+={[}]|\:;\"'<,>.?/ "
# symbols2 = 0
# mark = 0
# for char in text:
#     if char.isdigit():
#         count += 1
#     if char in symbols:
#         symbols2 += 1
#     if char == '!':
#         mark += 1
# print(f"Перероблений текст:{text}")
# print(f"Цифри зустрічаються {count} разів в {text}.")
# print(f"Розділові знаки зустрічаються: {symbols2} разів в {text}.")
# print(f"Знаки оклику зустрічаються {mark} разів в {text}.")

# Task 1
# try:
#     # Блок для створення списку.
#     random_number = random.randint(1, 1000)  # Створює рандомне число для random.seed
#     random.seed(random_number)  # Генерує список заповненим випадковими числами.
#     n = 10  # Кількість чисел у списку.
#     numbers = [random.randint(-1000, 1000) for _ in range(n)]  # Вибирає рандомне число для всіх елементів.
#     print(f"Список чисел: {numbers}")  # Виводить створенні числа.
#
#     # Блок для обчислення суми негативних чисел.
#     negative_sum = 0  # Створюємо змінну для суми негативних чисел.
#     for x in numbers:  # Звертається до кожного елементу в листі.
#         if x < 0:  # Якщо елемент списку менший за нуль.
#             negative_sum += x  # Добавляє число до змінної.
#     print(f"Сума негативних чисел: {negative_sum}")  # Виводимо суму негативних чисел.
#
#     # Блок для обчислення суми парних та непарних чисел.
#     even_sum = 0  # Створюємо змінну для суми парних чисел.
#     odd_sum = 0  # Створюємо змінну для суми непарних чисел.
#     for x in numbers:  # Звертається до кожного елементу в листі.
#         if x % 2 == 0:  # Якщо число зі списку ділиться на 2 без залишку.
#             even_sum += x  # Добавляємо число до суми парних чисел.
#         else:  # Інакше
#             odd_sum += x  # Добавляємо число до суми непарних чисел.
#     print(f"Сума парних чисел: {even_sum}")  # Виводимо суму парних чисел.
#     print(f"Сума непарних чисел: {odd_sum}")  # Виводимо суму непарних чисел.
#
#     # Блок для обчислення добутка елементів з кратними індексами 3.
#     index3_number = 1  # Змінна для добутка елементів з кратними індексами 3.
#     for i in range(2, len(numbers), 3):  # Вибирає елементи зі списку індекс який кратний 3.
#         index3_number *= numbers[i]  # Перемножує число зі змінною.
#     print(f"Добуток елементів з кратними індексами 3: {index3_number}")  # Виводить добуток елементів.
#
#     # Блок для обчислення добутка елементів між мінімальним та максимальним елементом.
#     min_num = min(numbers)  # Вибирає мінимальне число зі списку.
#     max_num = max(numbers)  # Вибирає максимальне число зі списку.
#     min_max_number = 1  # Змінна для добутка елементів.
#     for x in numbers[numbers.index(min_num) + 1: numbers.index(max_num)]:  # Шукає чи є елементи між ними.
#         min_max_number *= x  # Якщо є то перемножує зі змінною.
#     if min_max_number == 1:  # Якщо між елементами немає інших елементів.
#         print(f"Між мінімальним та максимальним елементом немає інших елементів.")  # Виводить це.
#     else:  # Інакше
#         print(f"Добуток елементів між мінімальним та максимальним елементом:: {min_max_number}")  # Виводить це.
#
#     # Блок для обчислення суми елементів між першим та останнім позитивними елементами
#     first_positive_number = 0  # Змінна для першого позитивного числа.
#     last_positive_number = 0  # Змінна для останнього позитивного числа.
#     sum_between_numbers = 0  # Змінна для суми елементів.
#     for i, x in enumerate(numbers):  # Звертаємося до елементів зі списку.
#         if x > 0:  # Якщо число більше за нуль.
#             first_positive_number = i  # Заноситься до змінної.
#             break  # Виходимо з циклу.
#     for i in range(len(numbers) - 1, -1, -1):  # Шукаємо елементи, починаючи з останнього.
#         if numbers[i] > 0:  # Якщо число більше за нуль.
#             last_positive_number = i  # Заноситься до змінної.
#             break  # Виходимо з циклу.
#     if first_positive_number == 0 or last_positive_number == 0:  # Якщо змінні дорівнюють нулю.
#         print(f"В Списку недостатньо позитивних елементів.")  # Виводимо помилку.
#     else:
#         for x in numbers[first_positive_number + 1: last_positive_number]:  # Шукаємо числа між ними.
#             sum_between_numbers += x  # Додаємо їх до змінної.
#         print(f"Сума елементів між першим та останнім позитивними елементами: {sum_between_numbers}")  # Виводить суму
#
# except Exception as error:  # Якщо з'являється якась помилка.
#     print("Помилка! зв'яжіться з розробником програми.")  # Виводимо користувачу про помилку.


# Task 2
# try:
#     # Блок для створення списку.
#     random_number = random.randint(1, 1000)  # Створює рандомне число для random.seed
#     random.seed(random_number)  # Генерує список заповненим випадковими числами.
#     n = 10  # Кількість чисел у списку.
#     numbers = [random.randint(-1000, 1000) for _ in range(n)]  # Вибирає рандомне число для всіх елементів.
#     print(f"Список чисел: {numbers}")  # Виводить створенні числа
#
#     # Блок для створення нового списка з цілими парними числами.
#     even_numbers = [x for x in numbers if x % 2 == 0]  # Звертаємося до кожного числа з першого списку.
#     print(f"Список парних чисел: {even_numbers}")  # Виводимо новий список.
#
#     # Блок для створення нового списка з цілими непарними числами.
#     odd_numbers = [x for x in numbers if x % 2 != 0]  # Звертаємося до кожного числа з першого списку.
#     print(f"Список непарних чисел: {odd_numbers}")  # Виводимо новий список.
#
#     # Блок для створення нового списка з цілими негативними числами.
#     negative_numbers = [x for x in numbers if x < 0]  # Звертаємося до кожного числа з першого списку.
#     print(f"Список негативних чисел: {negative_numbers}")  # Виводимо новий список.
#
#     # Блок для створення нового списка з цілими позитивними числами.
#     positive_numbers = [x for x in numbers if x > 0]  # Звертаємося до кожного числа з першого списку.
#     print(f"Список позитивних чисел: {positive_numbers}")  # Виводимо новий список.
#
# except Exception as error:  # Якщо з'являється якась помилка.
#     print("Помилка! зв'яжіться з розробником програми.")  # Виводимо користувачу про помилку.


# # Task Matrix
# try:
#     # Блок для створення матриці 10x10 та заповнення рандомними числами.
#     matrix = [[random.randint(10, 99) for _ in range(10)] for _ in range(10)]  # Створює матрицю.
#     print("Матриця:")  # Виводимо матрицю
#     for row in matrix:  # Звертаємося до кожного рядка в матриці.
#         print(row)  # Виводимо на екран матрицю.
#
#     # Блок для виведення суми чисел головної діагоналі.
#     main_diagonal_sum = sum(matrix[i][i] for i in range(10))  # Цей рядок проходить по всім індексам i від 0 до 9.
#     print(f"Сума чисел головної діагоналі: {main_diagonal_sum}")  # Виводимо суму головної діагоналі.
#
#     # Знаходимо та виводимо мінімальне та максимальне значення побічної діагоналі
#     secondary_diagonal_numbers = [matrix[i][9 - i] for i in range(10)]  # Проходить по побічній діагоналі матриці.
#     min_secondary = min(secondary_diagonal_numbers)  # Вибирає мінімальне значення з матриці.
#     max_secondary = max(secondary_diagonal_numbers)  # Вибирає максимальне значення з матриці.
#     print("Мінімальне значення побічної діагоналі:", min_secondary)  # Виводить мінімальне значення.
#     print("Максимальне значення побічної діагоналі:", max_secondary)  # Виводить максимальне значення.
#
#     # Ввід номера стовпця та вивід цифр з цього стовпця.
#     column_number = int(input("Введіть номер стовпця (0-9): "))  # Просить ввести в користувача номер стовпця.
#     column_values = [matrix[i][column_number] for i in range(10)]  # Вибирає стовбець з матриці.
#     print(f"Значення зі стовпця {column_number}: {column_values}")  # Виводить цифру користувача і стовпець.
#
#     # Ввід номера рядка та вивід цифр з цього рядка.
#     row_number = int(input("Введіть номер рядка (0-9): "))  # Просить ввести в користувача номер рядка.
#     row_values = matrix[row_number]  # Вибирає рядок з матриці.
#     print(f"Значення з рядка {row_number}: {row_values}")  # Виводить цифру користувача і рядок.
#
#     # Ввід номера двох стовпців та обмін їх місцями.
#     swap_column1 = int(input("Введіть номер стовпця який ви хочете замінити (0-9): "))
#     swap_column2 = int(input("Введіть номер стовпця яким ви заміните його (0-9): "))
#     if swap_column1 == swap_column2 or swap_column2 == swap_column1:
#         print("Помилка, ви ввели однакові стовпці")
#     else:
#         if 0 <= swap_column1 < 10 and 0 <= swap_column2 < 10:
#             for i in range(10):
#                 matrix[i][swap_column1], matrix[i][swap_column2] = matrix[i][swap_column2], matrix[i][swap_column1]
#             print("Матриця після обміну стовпців:")  # Виводимо змінену матрицю.
#             for row in matrix:
#                 print(row)
#         else:
#             print("Помилка, ви ввели число не в діапазоні матриці.")
#
#     # Ввід номера двох рядків та обмін їх місцями.
#     swap_row1 = int(input("Введіть номер рядка який ви хочете замінити (0-9): "))
#     swap_row2 = int(input("Введіть номер рядка яким ви заміните його (0-9): "))
#     if swap_row1 == swap_row2:
#         print("Помилка, ви ввели однакові рядки")
#     else:
#         if 0 <= swap_column1 < 10 and 0 <= swap_column2 < 10:
#             for i in range(10):
#                 matrix[i][swap_column1], matrix[i][swap_column2] = matrix[i][swap_column2], matrix[i][swap_column1]
#             print("Матриця після обміну рядків:")  # Виводимо змінену матрицю.
#             for row in matrix:
#                 print(row)
#         else:
#             print("Помилка, ви ввели число не в діапазоні матриці.")
#
# except ValueError as error:  # Якщо з'являється якась помилка.
#     print("Помилка, ви ввели текст або символи.")  # Виводимо користувачу про помилку.
# except Exception as Error:  # Якщо з'являється якась помилка.
#     print(f"Помилка! зв'яжіться з розробником програми.")  # Виводимо користувачу про помилку.

# task
# n = 10
# ist = [random.randint(1, 100) for _ in range(n)]
# print(f"Лист: {ist}")
# min_number = min(ist)
# max_number = max(ist)
# min_value_index = ist.index(min_number)
# max_value_index = ist.index(max_number)
# ist[min_value_index] = max_number
# ist[max_value_index] = min_number
# print(f"Лист: {ist}")

# task other solution
# ist[ist.index(min(ist))], ist[ist.index(max(ist))] = max(ist), min(ist)
# print(f"Лист: {ist}")

# task 2
# n = 10
# numbers = [random.randint(1, 100) for _ in range(n)]
# print(numbers)
# # for x in numbers:
# #     if x % 2 == 0:
# #         print(x)
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)


# task 3
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# lenth = (len(numbers)) // 2
# numbers_1 = numbers[:lenth]
# numbers_2 = numbers[lenth:]
# print(numbers_1, numbers_2)
# sorted_numbers = sorted(numbers, reverse=True)
# second_numbers = sorted_numbers[1]
# print(second_numbers)

# try:
#     Task = int(input("Введіть номер завдання(1-6): "))
#     if 0 < Task < 7:
#         match Task:
#             case 1:  # Порахувати кiлькiсть чисел зI знаком "-"
#                 List = [random.randint(-100, 100) for _ in range(10)]
#                 print(f"Згенерований лист: {List}")
#                 negative_count = sum(1 for num in List if num < 0)
#                 if negative_count == 0:
#                     print("Негативних чисел немає.")
#                 else:
#                     print(f"Кількість негативних чисел: {negative_count}")
#             case 2:  # Видалити всi елементи списку, що дiляться на 3 без залишку
#                 List = [random.randint(-100, 100) for _ in range(10)]
#                 print(f"Згенерований лист: {List}")
#                 final_list = [num for num in List if num % 3 != 0]
#                 if final_list == 0:
#                     print("В листі немає елементів які дiляться на 3 без залишку.")
#                 else:
#                     print(f"Лист без елементів які дiляться на 3 без залишку: {final_list}")
#             case 3:  # Зробити сортування списку без метода sort
#                 List = [random.randint(-100, 100) for _ in range(10)]
#                 print(f"Згенерований лист: {List}")
#                 e = len(List)  # Змінна для довжини списка.
#                 for i in range(e):  # Потрібно для створення циклу.
#                     for j in range(0, e - i - 1):  # (0, n - i - 1) Робить щоб через кожний цикл він переходив на 2 ел
#                         if List[j] > List[j + 1]:  # Якщо минулий елемент більший за наступний.
#                             List[j], List[j + 1] = List[j + 1], List[j]  # Змінює їх місцями.
#                 print(f"Посортований список: {List}")
#             case 4:  # Написати список задом наперед
#                 List = [random.randint(-100, 100) for _ in range(10)]
#                 print(f"Згенерований лист: {List}")
#                 reversed_list = List[::-1]
#                 print(f"Список задом наперед: {reversed_list}")
#             case 5:  # Створити новий список, у якому кожен елемент - конкатенація рядка
#                 words = ["apple", "banana", "cherry"]
#                 print(f"Данні слова: {words}")
#                 suffix = " pie"
#                 print(f"Суфікс: {suffix}")
#                 new_list = [word + suffix for word in words]
#                 print(f"Новий список: {new_list}")
#             case 6:  # Знайти спільні елементи у двох списках.
#                 List1 = [random.randint(-30, 30) for _ in range(10)]
#                 List2 = [random.randint(-30, 30) for _ in range(10)]
#                 print(f"Перший згенерований лист: {List1}")
#                 print(f"Другий згенерований лист: {List2}")
#                 same_elements = []
#                 for e in List1:
#                     if e in List2:
#                         same_elements.append(e)
#                 if not same_elements:
#                     print(f"Спільних елементів немає.")
#                 else:
#                     print(f"Спільні елементи: {same_elements}")
#     else:
#         print("Помилка, ви ввели число не в діапазоні завдань.")
# except ValueError as Error:
#     print("Помилка, ви ввели текст або символи.")
# except Exception as Error:
#     print("Помилка, зв'яжіться з розробником програми.")

# try:
#     Task = int(input("Введіть номер завдання(1-9): "))
#     if 0 < Task < 10:
#         match Task:
#             case 1:
#                 words = ["apple", "banana", "grape", "pear", "kiwi", "orange"]
#                 grouped_by_length = {}
#                 for word in words:
#                     lenth = len(word)
#                     if lenth in grouped_by_length:
#                         grouped_by_length[lenth].append(word)
#                     else:
#                         grouped_by_length[lenth] = [word]
#                 print(grouped_by_length)
#             case 2:
#                 text_numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
#                 text = "three"
#                 number = text_numbers.get(text, "unknown")
#                 print(number)
#             case 3:
#                 elements = [1, 2, 3, 2, 1, 3, 1, 2, 4, 5, 1]
#                 count_dict = {}
#                 for el in elements:
#                     if el in count_dict:
#                         count_dict[el] += 1
#                     else:
#                         count_dict[el] = 1
#                 print(count_dict)
#             case 4:
#                 synonyms = {
#                     "happy": ["joyful", "content", "pleased"],
#                     "sad": ["unhappy", "miserable", "gloomy"],
#                     "angry": ["irate", "furious", "enraged"]
#                 }
#                 word = "happy"
#                 end = synonyms.get(word, [])
#                 print(end)
#             case 5:
#                 text = "hello world"
#                 char_count = {}
#                 for t in text:
#                     if t in char_count:
#                         char_count[t] += 1
#                     else:
#                         char_count[t] = 1
#                 print(char_count)
#             case 6:
#                 # 1 варіант
#                 student_info = {
#                     "Аліса": {"age": 20, "grades": [85, 90, 78]},
#                     "Боб": {"age": 22, "grades": [92, 88, 95]}
#                 }
#                 print("Варіанти: Аліса, Боб")
#                 student_name = str(input("Введіть ім'я студента: "))
#                 correct_name = student_name.capitalize()
#                 if correct_name in student_info:
#                     student = student_info[correct_name]
#                     age = student["age"]
#                     grades = student["grades"]
#                     average_grade = sum(grades) / len(grades)
#                     print(f"Ім'я: {correct_name}")
#                     print(f"Вік: {age}")
#                     print(f"Оцінки: {grades}")
#                 else:
#                     print(f"Студента з ім'ям {student_name} не знайдено.")
#                 # 2 варіант
#                 student_info = {
#                     "Аліса": {"age": 20, "grades": [85, 90, 78]},
#                     "Боб": {"age": 22, "grades": [92, 88, 95]}
#                 }
#                 student_info_alice = {
#                     "Аліса": student_info["Аліса"]
#                 }
#                 student_info_bob = {
#                     "Боб": student_info["Боб"]
#                 }
#                 print()
#                 print(student_info_alice)
#                 print(student_info_bob)
#             case 7:
#                 grades = {"math": 90, "history": 85, "biology": 78}
#                 total = sum(grades.values())
#                 average = int(total / len(grades))
#                 print(f"Оцінки: {grades}")
#                 print(f"Сума: {total}")
#                 print(f"Середнє значення: {average}")
#             case 8:
#                 menu = {
#                     "burger": 8.99,
#                     "pizza": 12.99,
#                     "salad": 6.49,
#                     "pasta": 10.49
#                 }
#                 order = ["pizza", "salad"]
#                 total_price = 0
#                 for item in order:
#                     if item in menu:
#                         total_price += menu[item]
#                 print(f"Меню: {menu}")
#                 print(f"Ваш заказ: {order}")
#                 print(f"Сума заказу: {total_price}")
#             case 9:
#                 translations = {
#                     "hello": "привіт",
#                     "world": "світ",
#                     "python": "пітон"
#                 }
#                 print("Варіанти: hello, world, python")
#                 word = input("Введіть слово яке потрібно перекласти: ")
#                 correct_word = word.lower()
#                 if correct_word in translations:
#                     translation = translations[correct_word]
#                     print(f"Переклад слова {correct_word} - {translation}")
#                 else:
#                     print(f"Слово {correct_word} не знайдено у словнику перекладів.")
#     else:
#         print("Помилка, ви ввели число не в діапазоні завдань.")
# except ValueError as Error:
#     print("Помилка, ви ввели текст або символи.")
# except Exception as Error:
#     print("Помилка, зв'яжіться з розробником програми.")

# import string
# import random
# try:
#     Task = int(input("Введіть номер завдання(1-5): "))
#     if 0 < Task < 6:
#         match Task:
#             case 1:  # 1. Функція для перевірки, чи є рядок паліндромом
#                 def palindrome(a):
#                     a = a.replace(" ", "").lower()  # Прибирає всі пробіли та робить текст маленьким.
#                     return a == a[::-1]  # Перевіряє чи текст буде таким самим з його оберненою версією.
#
#                 input_string = input("Введіть слово яке ви хочете перевірити: ")
#                 if input_string.strip() == "" or "  " in input_string:
#                     print("Ви ввели нічого, або ввели більше ніж 1 пробіл.")
#                 else:
#                     if palindrome(input_string):
#                         print(f"{input_string} є паліндромом.")
#                     else:
#                         print(f"{input_string} не є паліндромом.")
#             case 2:  # 2. Функція для перевірки наявності елемента у списку
#                 def check_element(element, user_list):
#                     return element in user_list
#
#                 user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#                 print(f"Лист: {user_list}")
#                 user_element = int(input("Введіть елемент який ви хочете найти: "))
#                 if check_element(user_element, user_list):
#                     print(f"{user_element} знаходиться у списку.")
#                 else:
#                     print(f"{user_element} не знаходиться у списку.")
#             case 3:  # 3. Функція для перевірки входження підрядка в рядок
#                 def check_substring(substring, my_string):
#                     return substring.lower() in my_string.lower()
#
#                 my_string = input("Введіть рядок: ")
#                 substring = input("Введіть підрядок: ")
#                 if check_substring(substring, my_string):
#                     print(f"Підрядок {substring} знайдено у рядку {my_string}")
#                 else:
#                     print(f"Підрядок {substring} не знайдено у рядку {my_string}")
#             case 4:  # 4. Функція для створення випадкового пароля (import string)
#                 def generate_random_password(length=16):
#                     characters = string.ascii_letters + string.digits  # Добавляє всі літери (Великі та малі) та числа.
#                     password = "".join(random.choice(characters) for _ in range(length))  # Вибирає числа зі змінної
#                     return password
#
#                 random_password = generate_random_password()
#                 print(f"Ваш випадковий пароль: {random_password}")
#             case 5:  # 5. Функція для сортування списку слів за довжиною
#                 def sort_words(word_list):
#                     return sorted(word_list, key=len)  # key=len означає сортування за довжиною кожного слова.
#                 words = ["Blueberry", "Banana", "Orange", "Watermelon", "Strawberry", "Apple", "Grape", "Pineapple"]
#                 print(f"Список до сортування: {words}")
#                 sorted_words = sort_words(words)
#                 print(f"Список після сортування: {sorted_words}")
#     else:
#         print("Помилка, ви ввели число не в діапазоні завдань.")
# except ValueError as Error:
#     print("Помилка, ви ввели текст або символи.")
# except Exception as Error:
#     print("Помилка, зв'яжіться з розробником програми.")

# Task 1
# dictionary = {
#     "dict1": {'a': 1, 'b': 2},
#     "dict2": {'x': 10, 'y': 20}
# }
# value = dictionary["dict2"]["y"]
# print(value)

# Task 2
# def find_common_elements(dict1, dict2):
#     common_elements = {}
#     for key in dict1.keys():
#         if key in dict2:
#             common_elements[key] = dict1[key]
#     return common_elements
#
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 2, 'c': 4, 'd': 5}
# result = find_common_elements(dict1, dict2)
# print(result)

# Task 3
# Створіть словник, де ключами є кортежі, і напишіть функцію для доступу до значень з використанням кортежів як ключі.
# tuple_dict = {
#     ('a', 'b'): 1,
#     ('x', 'y'): 2
# }
# key1, key2 = ('a', 'b'), ('x', 'y')
# value1, value2 = tuple_dict.get(key1), tuple_dict.get(key2)
# print(f"Значення для ключа {key1}: {value1}")
# print(f"Значення для ключа {key2}: {value2}")

# def final_words(first_words):
#     dictionary_words = {}
#     for word in first_words:
#         sorted_letters = "".join(sorted(word))
#         if sorted_letters in dictionary_words:
#             dictionary_words[sorted_letters].append(word)
#         else:
#             dictionary_words[sorted_letters] = [word]
#     return dictionary_words
#
#
# first_words = ["риба", "школа", "дім", "магазин", "хімія", "біологія", "літак", "зошит", "офіс", "фабрика", "бар", "раб"]
# anagrams = final_words(first_words)
#
# for key, value in anagrams.items():
#     print(f"Анаграмна група {key}: {value}")

# from collections import defaultdict
# def final_words(first_words):
#     anagram_groups = defaultdict(list)
#     for word in first_words:
#         sorted_letters = "".join(sorted(word))
#         anagram_groups[sorted_letters].append(word)
#     return dict(anagram_groups)
#
#
# first_words = ["риба", "школа", "дім", "магазин", "хімія", "біологія", "літак", "зошит", "офіс", "фабрика", "бар", "раб"]
# anagrams = final_words(first_words)
#
# for key, value in anagrams.items():
#     print(f"Анаграмна група {key}: {value}")
# task 1 version 1
# def final_words(first_words):
#     dictionary_words = {}
#     for word in first_words:
#         sorted_letters = "".join(sorted(word))
#         if sorted_letters in dictionary_words:
#             dictionary_words[sorted_letters].append(word)
#         else:
#             dictionary_words[sorted_letters] = [word]
#     return dictionary_words
#
#
# first_words = ["риба", "школа", "магазин", "хімія", "біологія", "літак", "зошит", "офіс", "фабрика", "бар", "раб"]
# anagrams = final_words(first_words)
#
# for key, value in anagrams.items():
#     print(f"Анаграмна група {key}: {value}")

# task 1 version 2
# from collections import default-dict
# def final_words(first_words):
#     anagram_groups = default-dict(list)
#     for word in first_words:
#         sorted_letters = "".join(sorted(word))
#         anagram_groups[sorted_letters].append(word)
#     return dict(anagram_groups)
#
#
# first_words = ["риба", "школа", "магазин", "хімія", "біологія", "літак", "зошит", "офіс", "фабрика", "бар", "раб"]
# anagrams = final_words(first_words)
#
# for key, value in anagrams.items():
#     print(f"Анаграмна група {key}: {value}")

# task 2
# Напишіть функцію, яка приймає математичний вираз у вигляді рядка (наприклад, "2 + 3 * 4") і обчислює його результат.
# def math(examples):
#     stack = []
#     operators = set(["+", "-", "*", "/"])
#     for char in examples:
#         if char.isdigit():
#             stack.append(int(char))
#         elif char in operators:
#             operand2 = stack.pop()
#             operand1 = stack.pop()
#             if char == "+":
#                 results = operand1 + operand2
#             elif char == "-":
#                 results = operand1 - operand2
#             elif char == "*":
#                 results = operand1 * operand2
#             elif char == "/":
#                 results = operand1 / operand2
#             stack.append(results)
#     return stack[0]
#
#
# examples = "2 + 3 * 4"
# result = math(examples)
#
# print(result)

# Wrong program
# def calculate_expression(expression):
#     stack = []
#     operators = {"+", "-", "*", "/"}
#     current_number = ""
#
#     def perform_operation(operator, operand1, operand2):
#         if operator == "+":
#             return operand1 + operand2
#         elif operator == "-":
#             return operand1 - operand2
#         elif operator == "*":
#             return operand1 * operand2
#         elif operator == "/":
#             if operand2 == 0:
#                 raise ValueError("Дiлення на 0!")
#             return operand1 / operand2
#
#     for char in expression:
#         if char.isdigit() or char == "-":
#             current_number += char
#         elif char in operators or char.isspace():
#             if current_number:
#                 stack.append(int(current_number))
#                 current_number = ""
#             if char in operators:
#                 stack.append(char)
#
#     if current_number:
#         stack.append(int(current_number))
#
#     while len(stack) > 1:
#         operand2 = stack.pop()
#         operator = stack.pop()
#         operand1 = stack.pop()
#         result = perform_operation(operand1, operator, operand2)
#         stack.append(result)
#
#     return stack[0] if stack else "Некорректний вираз!"
#
#
# # Приклади використання функції
# expression1 = "3 + 5 * 2"
# result1 = calculate_expression(expression1)
# print("Result 1:", result1)
#
# expression2 = "8 / 0"
# result2 = calculate_expression(expression2)
# print("Result 2:", result2)


# Right program
# def calculate_expression(expression):
#     stack = []
#     operators = {"+", "-", "*", "/"}
#     current_number = ""
#
#     def perform_operation(operator, operand1, operand2):
#         if operator == "+":
#             return operand1 + operand2
#         elif operator == "-":
#             return operand1 - operand2
#         elif operator == "*":
#             return operand1 * operand2
#         elif operator == "/":
#             if operand2 == 0:
#                 print("Дiлення на 0!")  # Проблема була в raise ZeroDivision
#                 exit()
#             return operand1 / operand2
#
#     def precedence(operator):
#         if operator in ("+", "-"):
#             return 1
#         elif operator in ("*", "/"):
#             return 2
#         return 0
#
#     for char in expression:
#         if (char.isdigit() or char == "." or
#         (char == "-" and (not current_number or (stack and stack[-1] in operators)))):
#             current_number += char
#         elif char in operators or char.isspace():
#             if current_number:
#                 stack.append(int(current_number))
#                 current_number = ""
#             if char in operators:
#                 while (stack and stack[-1] in operators and
#                        precedence(stack[-1]) >= precedence(char)):
#                     operand2 = stack.pop()
#                     operator = stack.pop()
#                     operand1 = stack.pop()
#                     result = perform_operation(operator, operand1, operand2)
#                     stack.append(result)
#                 stack.append(char)
#
#     if current_number:
#         stack.append(int(current_number))
#
#     while len(stack) > 1:
#         operand2 = stack.pop()
#         operator = stack.pop()
#         operand1 = stack.pop()
#         result = perform_operation(operator, operand1, operand2)
#         stack.append(result)
#
#     return stack[0] if stack else "Некорректний вираз!"
#
#
# expression1 = "3 + 5 * 2"
# result1 = calculate_expression(expression1)
# print(f"{expression1} буде: {result1}")
#
# expression2 = "8 / 0"
# result2 = calculate_expression(expression2)
# print(f"{expression2} буде: {result2}")

# Задача 1
# text = input("Введіть рядок з 15 символами: ")
# if not text:
#     print("Помилка! рядок порожній.")
# else:
#     if len(text) < 15:
#         text *= (15//len(text))+1
# text_list = list(text)
# print(text_list)
# print(text_list[-5:])
# print(text_list[::-1])
# print(text_list[::2])
# print(text_list[:5]+text_list[-5:])

# Задача 2
# user_input = input("Введiть строку з 15 символiв: ")
# if not user_input:
#     print("Строка порожня!")
# else:
#     user_input = user_input.just(15, user_input * 15)[:15]
# user_list = list(user_input)
# print(user_list)

# Задача 2 перероблена
# user_input = input("Введiть строку з 15 символiв: ")
# if not user_input:
#     print("Строка порожня!")
# else:
#     user_input = user_input.ljust(15)[:15]
# user_list = list(user_input)
# print(user_list)

# Задача 3

# Вам дано 2 кортежі, (створіть за бажанням будьякі кортежі)
# A) потрібно створити з них список , елементами якого будуть числа
# обєкти кортежу першого та другого - результат виести на екран
# first = (1, 2, 3)
# second = (3, 4, 5)
# result = [1, 2, 3, 4, 5, 6]
# print(result)
# B) створити кортеж - який містить в собі 1 список створений раніше і 2 кортежі - кожен кортеж
# представленний у зрекальній послідовності - результат вивести на єкран
# t_result = ([1, 2, 3, 4, 5, 6], (3, 2, 1), (5, 4, 3))

# ex1
# first = (1, 2, 3)
# second = (3, 4, 5)

# result = list(first) + list(second)
# result = list(first + second)
# print(result)

# ex2

# t_result = (result, first[::-1], second[::-1])
# t_result = (result, first[::-1], second[::-1])
# print(t_result)

# ex3
# також надрукувати 3 значення з кортежу що стоврено кроком вище,

# print()

"""Програма повинна прочитати з консолi масив з n цiлих чисел та вивести
елементи масиву в одному рядку через промiжок, змiнивши початковий рядок на
протилежний."""
# n = input("Введіть масив: ")
# text = []
#
# for i in n.split():
#     text.append(int(i))
#
# text = text[::-1]
# str_text = ""
# for i in text:
#     str_text += str(i) + " "
# print(str_text)

"""Задано масив з n цiлих чисел. Вивести тiльки додатнi його елементи,
не змiнюючи їх початковий порядок або повiдомлення NО, якщо їх немає."""
# text = input("Введіть масив: ")
# text_2 = []
# text_complete = []
# str_text = ""
# for i in text.split():
#     text_2.append(int(i))
# for y in text_2:
#     if y > 0:
#         text_complete.append(y)
# if not text_complete:
#     print("NO")
# else:
#     for i in text_complete:
#         str_text += str(i) + " "
# print(str_text)

"""Задано n цiлих чисел. Вивести рiзницю мiж найбiЛьшим i найменшим числом.
Масив заповнити 20 випадковими числами вiд -10 до 10."""
# Оригінальна версія
# text = []
# for i in range(20):
#     text.append(random.randint(-10, 10))
# print(text)
# print(max(text) - min(text))

# Дуже спрощена версія
# numbers = [random.randint(-10, 10) for _ in range(20)]
# print(f"Масив випадкових чисел: {numbers}")
# print(f"Різниця між найбільшим і найменшим числом: {max(numbers) - min(numbers)}")

# Версія з розширеним функціоналом
"""Задано n цiлих чисел. Вивести рiзницю мiж найбiльшим i найменшим числом.
Масив заповнити 20 випадковими числами вiд -10 до 10."""
# try:
#     actions = ["+", "-", "*", "/", "quit"]
#     number_of_numbers = int(input("Введіть кількість чисел в масиві: "))
#     while number_of_numbers < 2:
#         number_of_numbers = int(input("Помилка! Кількість чисел в масиві повинна бути не менше 2: "))
#     min_randint = int(input("Введіть мінімальне значення цілого випадкового числа: "))
#     max_randint = int(input("Введіть максимальне значення цілого випадкового числа: "))
#     while min_randint > max_randint:
#         max_randint = int(input("Помилка! Ваше максимальне значення менше за мінімальне. Введіть нове значення: "))
#     numbers = [random.randint(min_randint, max_randint) for _ in range(number_of_numbers)]
#     print(f"Згенерований масив: {numbers}")
#     while True:
#         print("")
#         print("Варіанти: + - * / Або 'quit' щоб вийти з програми.")
#         choice = input("Введіть команду для найменшого та найбільшого числа в масиві: ")
#         if choice in actions:
#             match choice:
#                 case "+":
#                     print(f"{min(numbers)} + {max(numbers)} =", min(numbers) + max(numbers))
#                 case "-":
#                     print(f"{min(numbers)} - {max(numbers)} =", min(numbers) - max(numbers))
#                 case "*":
#                     print(f"{min(numbers)} * {max(numbers)} =", min(numbers) * max(numbers))
#                 case "/":
#                         division_value = float(min(numbers)) / float(max(numbers))
#                         rounded_division_value = round(division_value, 2)
#                         print(f"{min(numbers)} / {max(numbers)} = {rounded_division_value}")
#                 case "quit":
#                     print("Програму завершено.")
#                     break
#         else:
#             print("Помилка! Ви ввели неправильну команду.")
# except ValueError:
#     print("Помилка! Ви ввели некоректний тип даних.")
# except ZeroDivisionError:
#     print("Помилка! Ділити на нуль не можна.")
# except Exception:
#     print("Помилка! Зв'яжіться з розробником програми.")

#  Класи

# class Cat:
#     def init(self, name, breed):
#         self.name = name
#         self.breed = breed
#
# my_cat = Cat("Павло", "Дворянин")
# print(my_cat.name)

# Наслiдування

# class Animal:
#     def init(self, species):
#         self.species = species
#
# class Cat(Animal):
#     def init(self, name, breed):
#         super().init("Cat")
#         self.name = name
#         self.breed = breed
#
# my_cat = Cat("Павло", "Дворянин")
# print(my_cat.species)

# class Animal:
#     def speak(self):
#         print("Тварина звучить")
#
# class Cat(Animal):
#     def speak(self):
#         super().speak()
#         print("Павло мурчить")
#
# my_cat = Cat()
# my_cat.speak()

# Iнкапсуляцiя

# class BankAccount:
#     def init(self, balance):
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#
# my_account = BankAccount(1000)
# my_account.withdraw(100)
# print(my_account.get_balance())

#  Полiморфiзм

# class Cat:
#     def sound(self):
#         print("Мяу")
#
# class Dog:
#     def sound(self):
#         print("Гав")
#
# def make_sound(animal):
#     print(animal.sound())
#
# my_cat = Cat()
# my_dog = Dog()
#
# make_sound(my_cat)
# make_sound(my_dog)

# task 1
# class Student:
#     def __init__(self, name, age, grade):
#         self.__name = name
#         self.__age = age
#         self.__grade = grade
#
#     def name1(self):
#         return self.__name
#
#     def age1(self):
#         return self.__age
#
#     def grade1(self):
#         return self.__grade
#
#     def set_grade(self, grade):
#         if 0 <= grade <= 100:
#             self.__grade = grade
#         else:
#             print("Некоректнно заданна оцінка.")
#
#
# student1 = Student("Олександр", 25, 50)
# print(student1.name1())
# print(student1.age1())
# print(student1.grade1())
#
# student1.set_grade(100)
# print(student1.grade1())

# Task 2
# class Book:
#     def __init__(self, name, creator):
#         self.__name = name
#         self.__creator = creator
#
#     def get_name(self):
#         return self.__name
#
#     def get_creator(self):
#         return self.__creator
#
#
# book1 = Book("Пригоди", "Іван Франко")
# print(book1.get_name())
# print(book1.get_creator())

# Task 3
# class Car:
#     def __init__(self, mark, model):
#         self.__mark = mark
#         self.__model = model
#         self.__speed = 0
#
#     def get_mark(self):
#         return self.__mark
#
#     def get_model(self):
#         return self.__model
#
#     def get_speed(self):
#         return self.__speed
#
#     def accelerate(self, amount):
#         if amount > 0:
#             self.__speed += amount
#
#     def brake(self, amount):
#         if amount > 0:
#             self.__speed -= amount
#             if self.__speed < 0:
#                 self.__speed = 0
#
#
# new_car = Car("Ford", "Transit")
# print(new_car.get_mark())
# print(new_car.get_model())
# print(new_car.get_speed())
# new_car.accelerate(60)
# print(new_car.get_speed())
# new_car.brake(20)
# print(new_car.get_speed())

# try:
#     tasks = ["1", "2", "3"]
#     choice_library = ["+", "-", "=", "/"]
#     user_choice = input("Введіть номер завдання (1-3): ")
#     while user_choice not in tasks:
#         user_choice = input("Помилка! введіть номер завдання (1-3): ")
#     match user_choice:
#         case "1":
#             """Завдання 1: Створення класу для представлення бібліотеки з інкапсуляції.
#             Створіть клас Library, який представляє бібліотеку з каталогом книг
#             та методами для додавання та видалення книг.
#             Приховати каталог книг із використанням інкапсуляції."""
#
#
#             class Library:
#                 def __init__(self):
#                     self.__catalog = set()
#
#                 def add_book(self, book):
#                     book_lower = book.lower()
#                     if book_lower in self.__catalog:
#                         print(f"Книга '{book}' вже є в каталозі.")
#                     else:
#                         self.__catalog.add(book_lower)
#                         print(f"Додано книгу '{book}' до каталогу.")
#
#                 def remove_book(self, book):
#                     book_lower = book.lower()
#                     if book_lower in self.__catalog:
#                         self.__catalog.remove(book_lower)
#                         print(f"Книга '{book}' видалена з каталогу.")
#                     else:
#                         print(f"Книга '{book}' не знайдена в каталозі.")
#
#                 def get_catalog(self):
#                     if not self.__catalog:
#                         return []
#                     return list(self.__catalog)
#
#
#             my_library = Library()
#             print("Пояснення:\n"
#                   "'+' - Добавити книгу в каталог.\n"
#                   "'-' - Видалити книгу з каталогу.\n"
#                   "'=' - Вивести список книг в каталозі.\n"
#                   "'/' - Завершити роботу програми.")
#             while True:
#                 library_choice = input("Введіть одну із дій ('+' '-' '=' '/'): ")
#                 while library_choice not in choice_library:
#                     library_choice = input("Помилка! введіть одну із дій ('+' '-' '=' '/'): ")
#                 match library_choice:
#                     case "+":
#                         my_library.add_book(input("Введіть назву книги яку ви хочете добавити в каталог: "))
#                         print("")
#                     case "-":
#                         my_library.remove_book(input("Введіть назву книги яку ви хочете видалити з каталога: "))
#                         print("")
#                     case "=":
#                         print("Каталог книг в бібліотеці:")
#                         print(my_library.get_catalog())
#                         print("")
#                     case "/":
#                         print("Програму завершено.")
#                         break
#
#         case "2":
#             """Завдання 2: Створення класу подання співробітника з допомогою інкапсуляції.
#             Створіть клас Employee, який представляє співробітника з ім'ям, посадою та зарплатою.
#             Приховати дані про зарплату за допомогою інкапсуляції."""
#
#
#             class Employee:
#                 def __init__(self, name, position, salary):
#                     self.name = name
#                     self.position = position
#                     self.__salary = salary
#
#                 def get_salary(self):
#                     return self.__salary
#
#                 def set_salary(self, new_salary):
#                     if new_salary >= 0:
#                         self.__salary = new_salary
#                         print(f"Зарплата співробітника {self.name} оновлена: {new_salary}")
#                     else:
#                         print("Зарплата не може бути від'ємною.")
#
#
#             employee1 = Employee("Іван", "Менеджер", 50000)
#             choice_employee = ("info", "salary")
#             print("Варіанти:\n"
#                   "'info' - Інформація про робітника.\n"
#                   "'salary' - Змінити зарплату.\n"
#                   "'quit' - Вийти з програми.")
#
#             while True:
#                 employee_choice = input("Введіть одну із дій ('info' 'salary' 'quit'): ")
#                 while employee_choice not in choice_employee:
#                     employee_choice = input("Помилка! введіть одну із дій ('info' 'salary' 'quit'): ")
#                 match employee_choice:
#                     case "info":
#                         print(f"Ім'я: {employee1.name}")
#                         print(f"Посада: {employee1.position}")
#                         print(f"Зарплата: {employee1.get_salary()}")
#                         print("")
#                     case "salary":
#                         employee1.set_salary(int(input("Введіть нову зарплату: ")))
#                         print("")
#                     case "quit":
#                         print("Програму завершено.")
#                         break
#         case "3":
#             """Завдання 3: Створення класу представлення магазину з допомогою інкапсуляції.
#             Створіть клас Store, який представляє магазин з асортиментом товарів
#             та методами для додавання та видалення товарів.
#             Приховати асортименти товарів з використанням інкапсуляції."""
#
#
#             class Store:
#                 def __init__(self):
#                     self.__inventory = {}
#
#                 def add_item(self, item, quantity):
#                     item_lower = item.lower()
#                     if item_lower in self.__inventory:
#                         self.__inventory[item_lower] += quantity
#                         print(f"Додано {quantity} одиниць товару '{item}' до асортименту.")
#                     else:
#                         self.__inventory[item_lower] = quantity
#                         print(f"Додано {quantity} одиниць товару '{item}' до асортименту.")
#
#                 def remove_item(self, item, quantity):
#                     item_lower = item.lower()
#                     if item_lower in self.__inventory:
#                         if self.__inventory[item_lower] >= quantity:
#                             self.__inventory[item_lower] -= quantity
#                             print(f"Видалено {quantity} одиниць товару '{item}' з асортименту.")
#                             if self.__inventory[item_lower] == 0:
#                                 del self.__inventory[item_lower]
#                         else:
#                             print(f"У вас немає достатньої кількості товару '{item}' в асортименті.")
#                     else:
#                         print(f"Товар '{item}' не знайдений в асортименті.")
#
#                 def get_inventory(self):
#                     return self.__inventory
#
#
#             my_store = Store()
#             choice_Store = ["+", "-", "=", "/"]
#             while True:
#                 store_choice = input("Введіть одну із дій ('+' '-' '=' '/'): ")
#                 while store_choice not in choice_Store:
#                     store_choice = input("Помилка! введіть одну із дій ('+' '-' '=' '/'): ")
#                 match store_choice:
#                     case "+":
#                         item = input("Введіть назву товару: ")
#                         quantity = int(input("Введіть кількість товару: "))
#                         my_store.add_item(item, quantity)
#
#                     case "=":
#                         inventory = my_store.get_inventory()
#                         print("Асортимент товарів в магазині:")
#                         for item, quantity in inventory.items():
#                             print(f"{item}: {quantity} одиниць")
#
#                     case "-":
#                         item_to_remove = input("Введіть назву товару для видалення: ")
#                         remove_quantity = int(input("Введіть кількість товару для видалення: "))
#                         my_store.remove_item(item_to_remove, remove_quantity)
#
#                     case "/":
#                         print("Програму завершено.")
#                         break
# except Exception:
#     print("Помилка! зв'яжіться з розробником програми.")

# Поліморфізм
# class Animal:
#     def speak(self):
#         return ""
#
#
# class Cat(Animal):
#     def speak(self):
#         return "Мяу"
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Гав"
#
#
# cat = Cat()
# dog = Dog()
#
# print(cat.speak())
# print(dog.speak())


# def animal_sound(animal):
#     return animal.speak()


# cat = Cat()
# dog = Dog()
# print(animal_sound(cat))
# print(animal_sound(dog))


# class My_number:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         if isinstance(other, My_number):
#             return My_number(self.value + other.value)
#         else:
#             return My_number(self.value + other)
#
#     def __str__(self):
#         return str(self.value)
#
#
# num1 = My_number(25)
# num2 = My_number(35)
# result = num1 + num2
# print(result)

"""Створіть функцію get_area, яка приймає об'єкт фігури (як екземпляр класу Shape)
та повертає площу цієї фігури, використовуючи поліморфізм."""


# class Shape:
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         import math
#         return math.pi * self.radius ** 2
#
#
# def get_area(Shape):
#     return Shape.area()
#
#
# rectangle = Rectangle(10, 8)
# circle = Circle(30)
# print(get_area(rectangle))
# print(get_area(circle))


# shapes = [Rectangle(4, 5), Circle(30)]
# for shape in shapes:
#     print(shape.area())

"""1. Наведено список чисел. Визначте, скільки у ньому зустрічається різних чисел.
приклад: якщо в списку число 8 зустрічається 3 рази то це означає що в списку зустрічається 8мка."""

# import random
#
# numbers = [random.randint(0, 20) for _ in range(10)]
# different_numbers = set(numbers)
# similar_numbers = len(different_numbers)
# print(similar_numbers)

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3, 4, 10, 11, 12, 13, 14, 15}
# # Додавання елементу
# set1.add(6)
# print(set1)
# # Видалення елементу
# set1.remove(3)
# print(set1)
# set1.remove(6)
# print(set1)
# # Об'єднання множин
# union_set = set1.union(set2)
# print(union_set)
# # Перевірка елемента у множині
# member = 4 in set1
# print(member)
# # Перетин множин
# intersection_set = set1.intersection(set2)
# print(intersection_set)
# # Різниця множин
# difference_set = set1.difference(set2)
# print(difference_set)

"""2. Дано два списки чисел. Порахуйте, скільки різних чисел міститься як у першому списку, і у другому оночасно.
-PS: Різних чисел - мається на увазі що усі однакові елементи повинні бути представленні в одному екземплярі
(приклад: 3 однаковиі числа мають бути пораховані як 1 елемент)"""
# text1 = [1, 2, 3, 4, 5, 6, 7, 8]
# text2 = [5, 6, 7, 8, 9, 10, 11, 12]
# different_num1 = set(text1)
# different_num2 = set(text2)
# difference_set = different_num1.intersection(different_num2)
# difference = len(difference_set)
# print(difference)

""" 3. Є список(створити тестовий список для перевірки) із довільними даними (можуть бути словніки і списки).
Поставлено завдання перетворити його на множину. Якщо якісь елементи не можна хешувати, пропускаємо їх."""
# text1 = ["abc", 5, 89, {"author": "book"}]
# text2 = set()
# for i in text1:
#     if isinstance(i, (str, int)):
#         text2.add(i)
# print(text2)

# try:
#     choice = int(input("Введіть номер завдання(1-5): "))
#     if 0 < choice < 6:
#         match choice:
#             case 1:  # Операції над множинами:
#                 set1 = {1, 2, 3, 4, 5}
#                 set2 = {4, 5, 6, 7, 8}
#                 print("Об'єднання множин:", set1.union(set2))
#                 print("Перетин чисел у множинах:", set1.intersection(set2))
#                 print("Різниця чисел у першій множині від другої:", set1.difference(set2))
#                 print("Різниця чисел у другої множини від першої:", set2.difference(set1))
#             case 2:  # Перевірка включеності:
#                 set3 = {1, 2, 3, 4}
#                 set4 = {1, 2, 3, 4, 5, 6, 7, 8}
#                 if set3.issubset(set4):
#                     print("Так, одна множина є підмножиною іншої.")
#                 else:
#                     print("Ні, одна множина не є підмножиною іншої.")
#             case 3:  # Видалення дублікатів:
#                 list_wd = [1, 1, 2, 3, 4, 4, 5, 5]
#                 print(f"Список з дублікатами: {list_wd}")
#                 print("Множина:", set(list_wd))
#             case 4:  # Математичні операції:
#                 math_students = {"Abby", "Bob", "Max", "Michael"}
#                 physics_students = {"Bob", "James", "Michael", "Grace"}
#                 print("Студенти, які вивчають лише математику:", math_students.difference(physics_students))
#                 print("Студенти, які вивчають лише фізику:", physics_students.difference(math_students))
#                 print("Студенти, які вивчають обидва предмети:", math_students.intersection(physics_students))
#             case 5:  # Конвертація типів:
#                 mixed_set = {1, 4, 7, "hello"}
#                 print("Множина: ", mixed_set)
#                 converted_list = list(mixed_set)
#                 print("Конвертована множина у список:", converted_list)
#     else:
#         print("Помилка, ви ввели число не в діапазоні завдань.")
# except MemoryError as Error:
#     print("Помилка, у вас нехватає пам'яті для запуску програми.")
# except Exception as Error:
#     print("Помилка, зв'яжіться з розробником програми.")

"""
Написати функцію яка приймає на вхід параметри: список  чисел будь-якої довжини та число.
Функція повинна перевірити чи є у списку/послідовності 2 числа сума яких
еквівалентна числу переданому 2-гим параметром. Функція має повернути
булеве значення як результат пошуку фукції.
Для перевірки викликати двічі функцію з різними тестовими прикладами"""


# def user_input():
#     user_list = list(input("Введіть список чисел: "))
#     user_input = int(input("Введіть число: "))
#     for i in user_list:
#         if i


# def perevirka_sumy(nums, ts_ch):  # ts_ch - цiльове число
#     potentsiina_suma = set()
#
#     for num in nums:
#         riznytsya = ts_ch - num
#         if riznytsya in potentsiina_suma:
#             return True
#         potentsiina_suma.add(num)
#
#     return False
#
#
# dovguna_spysku1 = random.randint(5, 10)
# spysok1 = random.sample(range(5, 15), dovguna_spysku1)
# zadane_chyslo1 = random.randint(5, 15)
# print(f"Згенерований випадковий список: {spysok1} має випадкову суму"
#       f" {zadane_chyslo1}. Булевий результат: "
#       f"{perevirka_sumy(spysok1, zadane_chyslo1)}.")
#
# dovguna_spysku2 = random.randint(3, 10)
# spysok2 = random.sample(range(5, 15), dovguna_spysku2)
# zadane_chyslo2 = random.randint(10, 20)
# print(f"Згенерований випадковий список: {spysok2} має випадкову суму"
#       f" {zadane_chyslo2}. Булевий результат: "
#       f"{perevirka_sumy(spysok2, zadane_chyslo2)}.")

"""
Реалізувати 2 функціЇ
Перша функція приймає 2 параметри і генерує 2 вимірний список.
Заповнений випадковими цілими значенням в диапазлні 0 - 200 .
Параметри повинні задати кількість списків у основному списку а також довжину елементів списку.
Усі елементи головного списку є списками і мають однакову довжину.
Тако ж функція може бути запущена без параметрів з одним параметром та 2ма параметрами.
Функція повинна повернути згенерований 2 мірний список.
2 га функція очікує один обовязковий парметр і це має бути 2 вимірний список симетричний.
Вона отримує спискок і друкує симетричну табличку (у якої колонки не роз'їжаються)
значень з отриманого формального парметра. 
За дпомогою 1 та 2 функції вивести 3 таблички :
коли перша функція не отримує параметри 
коли перша фнкція отримує 1 парметр
коли перша функція отримує 2 параметри
"""


# def list2d(row=None, column=None):
#     if row is None and column is None:
#         row = int(input("Введіть довжину строки: "))
#         column = int(input("Введіть висоту строки: "))
#     elif column is None:
#         column = int(input("Введіть висоту строки: "))
#     matrix = [[random.randint(0, 200) for _ in range(column)] for _ in range(row)]
#     return matrix
#
#
# def symetrical_table():
#     max_len = max(len(str(element)) for st in list2d for element in st)
#     for st in list2d:
#         row_str = " ".join(str(element).rjust(max_len) for element in st)
#         print(row_str)
#
#
# print("Таблиця без параметрів")
# symetrical_table(list2d())
# print()

"""Оптимізація словника для зберігання даних:
Розглянемо ситуацію, коли у вас є словник з великим обсягом даних, які надають інформацію про студентів в університеті.
Кожен студент має унікальний ідентифікатор,
а атрибути включають оцінки різних предметів, дату народження, список курсів і т.д.
Зіткніться із завданням оптимізації цього словника, щоб забезпечити ефективний доступ та модифікацію даних."""

# from collections import namedtuple, default-dict
# Student = namedtuple("Student", ["Name", "DOB", "Grades"])
# grades = defaultsect(int)
# grades["Math"] = 0
# grades["Ecology"] = 0
# student_data = {
#     "ID1": Student("Петро", "01-01-2000", {"Language": 75, "Chemistry": 86, "Math": 72}),
#     "ID2": Student("Оксана", "25-08-2003", {"Biology": 93, "Ecology": 82, "History": 79}),
#     "ID3": Student("Дмитро", "12-11-1998", {"Information Technology": 96, "Physics": 88, "Geography": 91})
# }
# for studentID, student_info in student_data.items():
#     print(f"studentID: {studentID}")
#     print(f"Name:{student_info.Name}")
#     print(f"DOB:{student_info.DOB}")
#     print("Grades:")
#     for subject, grade in student_info.Grades.items():
#         print(f"    {subject}: {grade}")
#
# student_test = Student("Оксана", "25-08-2003", {"Biology": 93, "Ecology": 82, "History": 79})
# print(student_test[0])
# print(student_test.Name)
# print(grades["Law"])

"""Спростіть представлення точок у двовимірному просторі та обчисліть відстань між двома точками."""
# from collections import namedtuple
# import math
#
# Point = namedtuple("Point", ["x", "y"])
# point1 = Point(3, 4)
# point2 = Point(-3, 4)
#
#
# def calculate(p1, p2):
#     return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
#
#
# distance = calculate(point1, point2)
# print(distance)

"""Оптимізація словника для зберігання даних:
Розглянемо ситуацію, коли у вас є словник з великим обсягом даних, які надають інформацію про студентів в університеті.
Кожен студент має унікальний ідентифікатор,
а атрибути включають оцінки різних предметів, дату народження, список курсів і т.д.
Зіткніться із завданням оптимізації цього словника, щоб забезпечити ефективний доступ та модифікацію даних."""

# from collections import namedtuple, default-dict
# Student = namedtuple("Student", ["Name", "DOB", "Grades"])
# grades = defaultsect(int)
# grades["Math"] = 0
# grades["Ecology"] = 0
# student_data = {
#     "ID1": Student("Петро", "01-01-2000", {"Language": 75, "Chemistry": 86, "Math": 72}),
#     "ID2": Student("Оксана", "25-08-2003", {"Biology": 93, "Ecology": 82, "History": 79}),
#     "ID3": Student("Дмитро", "12-11-1998", {"Information Technology": 96, "Physics": 88, "Geography": 91})
# }
# for studentID, student_info in student_data.items():
#     print(f"studentID: {studentID}")
#     print(f"Name:{student_info.Name}")
#     print(f"DOB:{student_info.DOB}")
#     print("Grades:")
#     for subject, grade in student_info.Grades.items():
#         print(f"    {subject}: {grade}")
#
# student_test = Student("Оксана", "25-08-2003", {"Biology": 93, "Ecology": 82, "History": 79})
# print(student_test[0])
# print(student_test.Name)
# print(grades["Law"])

"""Спростіть представлення точок у двовимірному просторі та обчисліть відстань між двома точками."""
# from collections import namedtuple
# import math
#
# Point = namedtuple("Point", ["x", "y"])
# point1 = Point(3, 4)
# point2 = Point(-3, 4)
#
#
# def calculate(p1, p2):
#     return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
#
#
# distance = calculate(point1, point2)
# print(distance)

from collections import defaultdict
import random
import math
# Дано звіт продаж за тиждень працівників компанії у такому форматі
# Може бути таке що якись працівник робив декілька продаж на тиждень як на приклад "Alisa"
# Задача:
# створити множину робітників що зазначено у звіті продаж - вивести на єкран створити словник ключем якого буде ім'я
# працівника, а значенням сума виторгу ним за тиждень що зазначена  ключем "price" у звіті. Словник  надрукувати.
# data = [
#  {"name": "Alisa", "country": "UA", "item": "socks", "price": 15},
#  {"name": "Alisa", "country": "UA", "item": "socks", "price": 25},
#  {"name": "Ben", "country": "US", "item": "pencil", "price": 95},
#  {"name": "Alisa", "country": "UA", "item": "pencil", "price": 45},
#  {"name": "Oleg", "country": "GB", "item": "socks", "price": 100},
#  {"name": "Ben", "country": "US", "item": "pencil", "price": 10}
# ]
# workers = set(entry["name"] for entry in data)
# sales_sum = {}
# for entry in data:
#  name = entry["name"]
#  price = entry["price"]
#  if name in sales_sum:
#   sales_sum[name] += price
#  else:
#   sales_sum[name] = price
#
# print(f"Множина робітників: {workers}")
# print("Сума виторгу за тиждень за кожного працівника: ")
# for worker, sales in sales_sum.items():
#  print(f"{worker}: {sales}")

# v2
# data = [
#  {"name": "Alisa", "country": "UA", "item": "socks", "price": 15},
#  {"name": "Alisa", "country": "UA", "item": "socks", "price": 25},
#  {"name": "Ben", "country": "US", "item": "pencil", "price": 95},
#  {"name": "Alisa", "country": "UA", "item": "pencil", "price": 45},
#  {"name": "Oleg", "country": "GB", "item": "socks", "price": 100},
#  {"name": "Ben", "country": "US", "item": "pencil", "price": 10}
# ]
# workers = set(entry["name"] for entry in data)
# sales_sum = default dict(int)
# for entry in data:
#  sales_sum[entry["name"]] += entry["price"]
# print(f"Множина робітників: {workers}")
# print("Сума виторгу за тиждень за кожного працівника: ")
# for worker, sales in sales_sum.items():
#  print(f"{worker}: {sales}")

# Задача: Розподіл точок на площині
# Створіть програму, яка генерує список точок на площині. Кожна точка представлена словником з ключами "x" та "y",
# що вказують координати точки. Кількість точок та їхні координати визначаються випадковим чином.
# Виведіть:
# 1. Кількість унікальних значень x та y у згенерованому списку точок.
# 2. Всі точки, які знаходяться в першій чверті (x та y обидва додатні).
# 3. Відстань між першою та останньою точкою у списку.
# Приклад виводу:
# Кількість унікальних значень x: 8
# Кількість унікальних значень y: 7
# Точки в першій чверті:
# {"x": 3, "y": 5}
# {"x": 2, "y": 4}
# {"x": 4, "y": 3}
# Відстань між першою та останньою точкою: 5.0
# У цій задачі вам слід розглянути генерацію списку точок та виконання різних операцій над ним.
# dots = [{"x": random.randint(-10, 10), "y": random.randint(-10, 10)} for _ in range(10)]
# unique_x_value = len(set(dot["x"] for dot in dots))
# unique_y_value = len(set(dot["y"] for dot in dots))
# points_in_first_quadrant = [dot for dot in dots if dot["x"] > 0 and dot["y"] > 0]
# print("Точки в першій чверті: ")
# for dot in points_in_first_quadrant:
#     print(dot)
# distance = math.sqrt((dots[0]["x"] - dots[-1]["x"])**2 + (dots[0]["y"] - dots[-1]["y"])**2)
# print(f"\n Відстань між першою та останію точкою: {distance:.4f}")

# import random
# """Задача: Магазин книг з інформацією про покупців
# Створіть програму для інтернет-магазину книг, яка генерує список покупців.
# Кожен покупець представлений словником з ключами
# "ім'я", "прізвище", "адреса" та "кількість придбаних книг".
# Кількість покупців та їхні дані визначаються випадковим чином."""
# # "adress": f"{random.randint(1, 100)} вул. {random.choice(["Спортивна",
# # "Миру", "Героїв танкістів", "Тараса Шевченка", "Гоголя"])}"
#
#
# def gen_customers(num_customers):
#     name_list = ["Олександр", "Оксана", "Дмитро", "Максим", "Ірина", "Софія"]
#     surname_list = ["Агаштон", "Радченко", "Клименко", "Савчук", "Науменко",
#                     "Єрмоленко"]
#
#     customers = [
#         {
#             "name": random.choice(name_list),
#             "surname": random.choice(surname_list),
#             "adress": str(random.randint(1, 100)) + " вул. "
#                       + random.choice(["Спортивна", "Миру", "Героїв танкістів",
#                                        "Тараса Шевченка", "Гоголя"]),
#             "count_of_books": random.randint(1, 20)
#         }
#         for _ in range(num_customers)
#     ]
#     return customers
#
#
# def num_of_books(customers):
#     return sum(customer["count_of_books"] for customer in customers)
#
#
# def max_books(customers, n):
#     return [customer for customer in customers if customer["count_of_books"]
#             > n]
#
#
# num_customers = 10
# customers_list = gen_customers(num_customers)
# print("Інформація про покупців: ")
# for customer in customers_list:
#     print(customer)
#
# sum_of_books = num_of_books(customers_list)
# print(f"\nЗагальна кількість придбаних книг: ")
#
# n_books = 3
# selected_customers = max_books(customers_list, n_books)
# print(f"\nПокупці які придбали більше ніж {n_books} книги:")
# for customer in selected_customers:
#     print(customer)
# """Генерує список покупців з випадковими даними."""
# """Знаходить загальну кількість придбаних книг усіма покупцями."""
# """Знаходить покупців, які придбали більше ніж n книг."""
# Генеруємо список покупців
# Виводимо дані про покупців
# Знаходимо та виводимо загальну кількість придбаних книг
# Знаходимо та виводимо покупців, які придбали більше ніж 3 книги

# import random
# """Задача: Спортивний турнір
# Напишіть програму для генерації розкладу спортивного турніру.
# Кількість команд та результати матчів визначаються випадковим чином.
# Кожен матч представлений словником з ключами:
# "команда1", "команда2" та "результат".
# Результат може бути виграшем однієї з команд або нічиєю."""
# try:
#     def generate_tournament_schedule(num_teams):
#         teams = [f"Команда {i}" for i in range(1, num_teams + 1)]
#         random.shuffle(teams)
#         schedule = []  # Потрібний для зберігання розкладу матчів.
#         while len(teams) > 1:
#             matches = []
#             for i in range(0, len(teams), 2):  # Формує пари команд для матчів.
#                 match = {
#                     "команда1": teams[i],
#                     "команда2": teams[i + 1],
#                     "результат": None
#                 }
#                 while (match["результат"] is None  # Для переграння після нічиї.
#                        or match["результат"] == "Нічия"):
#                     match["результат"] = random.choice([teams[i], teams[i + 1],
#                                                         "Нічия"])
#                     if match["результат"] == "Нічия":
#                         print(f"Нічия між {match["команда1"]}"
#                               f" та {match["команда2"]} у Етапі "
#                               f"{round_num}")  # Не працює
#                         match["результат"] = random.choice([teams[i],
#                                                             teams[i + 1]])
#                 matches.append(match)  # Додає для зміни щоб вивести можна було.
#             schedule.append(matches)  # Додає список matches до schedule.
#             winners = [match["результат"] for match in matches
#                        if match["результат"]
#                        != "Нічия"]  # Зберігає переможців у зміну.
#             teams = winners
#         return schedule
#
#
#     round_num = 1
#     num_teams = random.choice([4, 8, 16])
#     print(f"Розклад спортивного турніру з {num_teams} команд:\n")
#     tournament_schedule = generate_tournament_schedule(num_teams)
#     for matches in tournament_schedule:
#         print(f"\nЕтап {round_num}:")
#         for match in matches:
#             if match["результат"] == "Нічия":
#                 print(f"Нічия між {match["команда1"]} та {match["команда2"]}"
#                       f". Матч було переграно.")
#             print(f"{match["команда1"]} проти {match["команда2"]}:"
#                   f" Переможець - {match["результат"]}")
#             winner_team = match["результат"]
#         round_num += 1
#     print(f"\nВ цьому спортивному турнірі перемогла: {winner_team}")
# except MemoryError as Error:
#     print("Помилка, у вас нехватає пам'яті для запуску програми.")
# except Exception as Error:
#     print("Помилка, зв'яжіться з розробником програми.")

# import random
# """Задача: Комерційна нерухомість
# Напишіть програму для генерації списку комерційних приміщень
# на земельній ділянці. Кожне приміщення представлено словником з ключами:
# "площа", "тип" та "ціна". Тип приміщення може бути, наприклад: "офіс",
# "магазин", "ресторан". Площа та ціна генеруються випадковим чином.
# Кількість приміщень, їхні характеристики також визначаються випадковим чином."""
#
#
# def buildings_function(num_properties):
#     property_types = ["офіс", "магазин", "ресторан"]
#     buildings = [
#         {
#             "площа": random.randint(100, 1000),
#             "тип": random.choice(property_types),
#             "ціна": random.randint(1000, 99999)
#         }
#         for _ in range(num_properties)
#     ]
#     return buildings
#
#
# def buildings_info(properties):
#     for i, prop in enumerate(properties, 1):
#         print(f"{i}. Інформація про комерційні приміщеня: Тип - "
#               f"{prop["тип"]}, Площа - {prop["площа"]}, Ціна - ${prop["ціна"]}")
#
#
# def square(properties):
#     return sum(prop["площа"] for prop in properties)
#
#
# def value(properties):
#     return sum(prop["ціна"] for prop in properties)
#
#
# # Генеруємо список комерційних приміщень
# # Виводимо інформацію про приміщення
# # Обчислюємо та виводимо загальну площу та вартість
# num_properties = 5
# comercial_buildings = buildings_function(num_properties)
# buildings_info(comercial_buildings)
# square_all = square(comercial_buildings)
# value_all = value(comercial_buildings)
# print(f"Загальна площа: {square_all}, загальна ціна: {value_all}")

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

"""
Задача 1: Робота з часовими діапазонами

Створіть програму, яка приймає введення користувача у вигляді
дати та часу в форматі "YYYY-MM-DD HH:MM:SS". Перевірте, чи введені дані
знаходяться в діапазоні від сьогоднішньої дати і часу до дати та часу
через 7 днів включно. Виведіть повідомлення, чи введені дані відповідають
цьому діапазону.

Вимоги до програми:

1. Використайте бібліотеку datetime для роботи з часовими даними.
2. Запитуйте користувача про введення дати та часу.
3. Перевірте, чи введені дані входять в діапазон від сьогоднішньої дати і часу
до дати та часу через 7 днів.
4. Виведіть повідомлення про відповідність чи невідповідність введених даних
діапазону.
"""


# def verification(input_date_str):
#     try:
#         user_date = (datetime.strptime
#                      (input_date_str, "%Y-%m-%d %H:%M:%S"))
#         current_date = datetime.now()
#         next_date = current_date + timedelta(days=7)
#         if current_date <= user_date <= next_date:
#             print(f"Ваша дата та час: {user_date}, відповідають діапазону.")
#         else:
#             print(f"Ваша дата та час: {user_date}, не відповідають діапазону.")
#     except Exception as e:
#         print(f"Помилка!, {str(e)}")
#
#
# user_date_time = input("Введіть вашу дату у форматі (YYYY-MM-DD "
#                        "HH:MM:SS): ")
# result = verification(user_date_time)
# print(result)

"""
Розрахунок різниці між датами

Напишіть програму, яка приймає введення користувача у вигляді двох дат в форматі
"YYYY-MM-DD". Розрахуйте та виведіть на екран різницю в днях між цими датами.

Вимоги до програми:

1. Використайте бібліотеку datetime для роботи з датами.
2. Запитуйте користувача про введення двох дат.
3. Розрахуйте різницю між цими датами.
4. Виведіть на екран кількість днів, яка розділяє ці дві дати.

Обидві ці задачі дозволять вам використовувати бібліотеку datetime
для роботи з часовими та датовими даними в Python.
"""


# def difference(input_date_str1, input_date_str2):
#     user_date1 = (datetime.strptime(input_date_str1, "%Y-%m-%d"))
#     user_date2 = (datetime.strptime(input_date_str2, "%Y-%m-%d"))
#     days_left = abs((user_date2 - user_date1).days)
#     print(f"Різниця між днями складає {days_left} днів.")
#
#
# user_date1 = input("Введіть першу дату у форматі (YYYY-MM-DD): ")
# user_date2 = input("Введіть другу дату у форматі (YYYY-MM-DD): ")
# difference(user_date1, user_date2)

"""
1. Задача про коло:
Обчисліть площу кола з радіусом 8.
2. Задача про трикутник:
Знайдіть гіпотенузу прямокутного трикутника зі сторонами 3 та 4.
3. Задача з округленням вгору:
Округліть число 12.46 вгору до найближчого цілого.
4. Задача з округленням вниз:
Округліть число 2.47 вниз до найближчого цілого.
5. Задача з факторіалом:
Знайдіть факторіал числа 17.
6. Задача про ступінь:
Піднесіть число 2 до 16-ї ступеня (2-ма способами).
7. Задача про пошук максимуму:
Знайдіть максимальне число зі списку: [15, 8, 12, 20, 5].
"""

# Task 1
# rad = 8
# P = math.pi * math.pow(8, 2)
# print(f"Площа кола: {P}")
#
# # Task 2
# katet1 = 3
# katet2 = 4
# gipotenusa = math.sqrt(math.pow(katet1, 2) + math.pow(katet2, 2))
# print(f"гіпотенуза прямокутного трикутника: {gipotenusa}")
#
# # Task 3
# number1 = 12.46
# new_number1 = math.ceil(number1)
# print(f"Число округлене вгору до найближчого цілого: {new_number1}")
#
# # Task 4
# number2 = 2.47
# new_number2 = math.floor(number2)
# print(f"Число округлене вниз до найближчого цілого: {new_number2}")
#
# # Task 5
# number3 = 17
# num_factorial = math.factorial(number3)
# print(f"Факторіал числа {number3} = {num_factorial}")
#
# # Task 6
# stupin_1 = math.pow(2, 16)
# stupin_2 = 2 ** 16
# print(f"Піднесення числа 2 до 16 ступеня (1 спосіб): {stupin_1}")
# print(f"Піднесення числа 2 до 16 ступеня (2 спосіб): {stupin_2}")
#
# # Task 7
# num_list = [15, 8, 12, 20, 5]
# max_num = max(num_list)
# print(f"Максимальне число зі списку: {max_num}")

# import math
# try:
#     choice = int(input("Введіть номер завдання(1-5): "))
#     while choice <= 0 or choice >= 6:
#         choice = int(input("Помилка, введіть номер завдання(1-5): "))
#     match choice:
#
#         case 1:  # Задача про об'єм кулі.
#             """ Обчисліть об'єм кулі з радіусом 34. """
#             radius = 34
#             volume = (4 * math.pi * radius ** 3) / 3
#             print(f"Об'єм кулі з радіусом {radius} дорівнює: {volume}")
#
#         case 2:  # Задача з геометричною прогресією.
#             """ Знайдіть суму перших 5 членів геометричної прогресії
#              з першим членом 3 і знаменником 2. """
#             first_term = 3
#             common_ratio = 2
#             num_terms = 5
#             sum_gp = (first_term * (1 - common_ratio ** num_terms)
#                       / (1 - common_ratio))
#             print(f"Сума перших {num_terms}"
#                   f" членів геометричної прогресії: {int(sum_gp)}")
#
#         case 3:  # Задача про об'єм циліндра.
#             """ Обчисліть об'єм циліндра з радіусом основи 5 і висотою 15. """
#             radius = 5
#             height = 15
#             base_area = math.pi * radius ** 2
#             volume = base_area * height
#             print(f"Об'єм циліндра з радіусом основи: {radius}, і висотою: "
#                   f"{height}, дорівнює: {volume}")
#
#         case 4:  # Задача про використання константи π.
#             """ Знайдіть довжину кола, якщо радіус дорівнює 7. """
#             radius = 7
#             circumference = 2 * math.pi * radius
#             print(f"Довжина кола з радіусом: {radius},"
#                   f" дорівнює: {circumference}")
#
#         case 5:  # Задача з трикутником і сінусом.
#             """ Знайдіть довжину сторони прямокутного трикутника,
#              якщо вам відомі кут 30 градусів і гіпотенуза рівна 5. """
#             angle = 30
#             hypotenuse = 5
#             angle_rad = math.radians(angle)
#             side = hypotenuse * math.sin(angle_rad)
#             print(f"Довжина сторони прямокутного трикутника"
#                   f" при куті {angle} градусів та гіпотенузі {hypotenuse} "
#                   f"градусів, дорівнює {round(side, 1)}")
#
# except MemoryError as e:
#     print(f"{str(e)}, у вас недостатньо оперативної пам'яті щоб запустити цю "
#           "програму.")
# except FileNotFoundError as e:
#     print(f"{str(e)}, програма не може отримати доступ до файлу.")
# except OverflowError as e:
#     print(f"{str(e)}, межу допустимих значень було перевищено.")
# except PermissionError as e:
#     print(f"{str(e)}, у вас немає необхідних прав доступу для виконання "
#           f"певної операції")
# except TypeError as e:
#     print(f"{str(e)}, перевірте правильність типів даних.")
# except ValueError as e:
#     print(f"{str(e)}, перевірте правильність введених даних.")
# except Exception as e:
#     print(f"Виникла помилка: {str(e)}")

import requests
""" Відправте GET-запит до веб-сайту
 та виведіть статус відповіді (код статусу) """
# url = "https://www.example.com"
# response = requests.get(url)
# print(response)

""" Відправте POST-запит до веб-сервера
 з певними даними та виведіть вміст відповіді. """
# url = "https://www.example.com"
# data = {'key': 'value'}
# response = requests.post(url, data=data)
# print(response.text)

""" Запитайте користувача про URL-адресу,
 а потім відправте GET-запит за введеним URL. """
# url = input("Введіть URL-адресу: ")
# response = requests.get(url)
# print(response)

"""Сума елементiв матрицi (построково)"""

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for row in matrix:
#     row_sum = sum(row)
#     print(f"Сума елементiв строки {row}: {row_sum}")

"""Множення на число"""
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# factor = 2
#
# result_matrix = [[element * factor for element in row] for row in matrix]
#
# print("Помножена матриця:", result_matrix)

"""Пошук min елементу у кожному стовбцi"""

# matrix = [
#     [11, -2, 34],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for j in range(len(matrix[0])):
#     column = [matrix[i][j] for i in range(len(matrix))]
#     min_element = min(column)
#     print(f"Мiнiмальний елемент у стовпцi {j + 1}: {min_element}")

"""Пошук середнього значення ел-тiв у матрицi"""

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# flat_row = [element for row in matrix for element in row]
# average = sum(flat_row) / len(flat_row)
#
# print(average)

"""Пошук додатнiх елементiв у матрицi"""

# matrix = [
#     [-1, 2, 3],
#     [4, -5, 6],
#     [-7, -8, 9]
# ]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j] > 0:
#             print(f"Додатнiй елемент {matrix[i][j]}, позицiя ({i + 1}, "
#                   f"{j + 1})")

"""Транспонування матриці"""
"""Створіть матрицю та транспонуйте її, помінявши місцями рядки і стовпці,
 створюючи нову матрицю."""

# V1
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix2 = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]
# for i in range(3):
#     for j in range(3):
#         matrix2[i][j] = matrix1[j][i]
#
# for row in matrix2:
#     print(row)

# V2
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix2 = [[matrix1[j][i] for j in range(len(matrix1))]
#            for i in range(len(matrix1[0]))]
#
# for row in matrix2:
#     print(row)

# import random
# try:
#     choice = int(input("Введіть номер завдання(1-4): "))
#     while choice <= 0 or choice >= 5:
#         choice = int(input("Помилка, введіть номер завдання(1-4): "))
#     match choice:
#         case 1:
#             """Створіть матрицю чисел. Знайдіть максимальний елемент
#             в кожному рядку та виведіть результат."""
#             rows = int(input("Введіть кількість рядків: "))
#             cols = int(input("Введіть кількість стовпців: "))
#             min_value = int(input("Введіть мінімальне значення: "))
#             max_value = int(input("Введіть максимальне значення: "))
#             matrix = []
#             while min_value == max_value:
#                 max_value = int(input("Помилка, мінімальне число дорівнювало "
#                                       "максимальному. Введіть максимальне "
#                                       "значення: "))
#
#             for _ in range(rows):
#                 row = [random.randint(min_value, max_value)
#                        for _ in range(cols)]
#                 matrix.append(row)
#             print("Згенерована матриця:")
#
#             for row in matrix:
#                 print(row)
#             print("\nМаксимальні елементи в кожному рядку:")
#
#             for i, row in enumerate(matrix, 1):
#                 max_in_row = max(row)
#                 print(f"Рядок {i}: {max_in_row}")
#
#         case 2:
#             """Створіть дві матриці однакового розміру та додайте їх,
#             створюючи нову матрицю із результатом."""
#             rows = int(input("Введіть кількість рядків: "))
#             cols = int(input("Введіть кількість стовпців: "))
#             min_value = int(input("Введіть мінімальне значення: "))
#             max_value = int(input("Введіть максимальне значення: "))
#             matrix1 = []
#             matrix2 = []
#             result_matrix = []
#
#             for _ in range(rows):
#                 row = [random.randint(min_value, max_value)
#                        for _ in range(cols)]
#                 matrix1.append(row)
#             print("Перша матриця:")
#
#             for row in matrix1:
#                 print(row)
#
#             for _ in range(rows):
#                 row = [random.randint(min_value, max_value)
#                        for _ in range(cols)]
#                 matrix2.append(row)
#             print("\nДруга матриця:")
#             for row in matrix2:
#                 print(row)
#
#             for i in range(rows):
#                 result_row = [matrix1[i][j] + matrix2[i][j]
#                               for j in range(cols)]
#                 result_matrix.append(result_row)
#             print("\nРезультат додавання матриць:")
#             for row in result_matrix:
#                 print(row)
#
#         case 3:
#             """Створіть дві матриці із відповідними розмірами та перемножте їх,
#             створюючи нову матрицю із результатом"""
#             matrix1 = [
#                 [1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]
#             ]
#             print(f"Перша матриця:")
#             for row in matrix1:
#                 print(row)
#             matrix2 = [
#                 [9, 8, 7],
#                 [6, 5, 4],
#                 [3, 2, 1]
#             ]
#             print(f"Друга матриця:")
#             for row in matrix2:
#                 print(row)
#             result_matrix = [
#                 [0, 0, 0],
#                 [0, 0, 0],
#                 [0, 0, 0]
#             ]
#
#             for i in range(len(matrix1)):
#                 for j in range(len(matrix2[0])):
#                     for k in range(len(matrix2)):
#                         result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
#
#             print("Результуюча матриця:")
#             for row in result_matrix:
#                 print(row)
#
#         case 4:
#             """Створіть квадратну матрицю та визначте,
#             чи вона є симетричною(рівною своєму транспонованому варіанту)."""
#             n = int(input("Введіть розмір квадратної матриці: "))
#             matrix = [[random.randint(1, 10) for _ in range(n)]
#                       for _ in range(n)]
#             print("Квадратна матриця:")
#             for row in matrix:
#                 print(row)
#             transposed_matrix = [[matrix[j][i] for j in range(n)]
#                                  for i in range(n)]
#             is_symmetric = True
#             for i in range(n):
#                 for j in range(n):
#                     if matrix[i][j] != transposed_matrix[i][j]:
#                         is_symmetric = False
#                         break
#             if is_symmetric:
#                 print("\nМатриця є симетричною.")
#             else:
#                 print("\nМатриця не є симетричною.")
#
#
# except MemoryError as e:
#     print(f"{str(e)}, у вас недостатньо оперативної пам'яті щоб запустити цю "
#           "програму.")
# except FileNotFoundError as e:
#     print(f"{str(e)}, програма не може отримати доступ до файлу.")
# except OverflowError as e:
#     print(f"{str(e)}, межу допустимих значень було перевищено.")
# except PermissionError as e:
#     print(f"{str(e)}, у вас немає необхідних прав доступу для виконання "
#           f"певної операції")
# except TypeError as e:
#     print(f"{str(e)}, перевірте правильність типів даних.")
# except ValueError as e:
#     print(f"{str(e)}, перевірте правильність введених даних.")
# except Exception as e:
#     print(f"Виникла помилка: {str(e)}")

# Напишіть програму, яка приймає матрицю та номер рядка або стовпця і знаходить
# суму всіх елементів у цьому рядку або стовпці.
# matrix = [
#           [1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]
#          ]


# row_index = 1
# column_index = 2
# sum_of_row = sum(matrix[row_index])
# print(f"Сума елементів у рядку: {sum_of_row}")
# sum_of_column = sum(row[column_index] for row in matrix)
# print(f"Сума елементів у стовбці: {sum_of_column}")


# def sum_matrix(matrix, index, axis="row"):
#     if axis == "row":
#         return sum(matrix[row_index])
#     elif axis == "column":
#         return sum(row[column_index] for row in matrix)
#
#
# print(f"Сума елементів у рядку: {sum_matrix(matrix, row_index)}")
# print(f"Сума елементів у стовбці: "
#       f"{sum_matrix(matrix, column_index, axis="column")}")


"""Реалізуйте функцію, яка приймає матрицю і повертає її транспоновану версію,
тобто матрицю, в якій рядки стають стовпцями і навпаки."""


# def function():
#     return [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(
#         matrix1[0]))]
#
#
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transported_matrix = function()
# for row in transported_matrix:
#     print(row)

# Напишіть програму, яка приймає дві матриці і виконує їх множення за правилом
# матричного множення, якщо це можливо, або повертає помилку в іншому випадку.

"""Напишіть програму, яка приймає дві матриці і виконує їх множення за правилом
матричного множення, якщо це можливо, або повертає помилку в іншому випадку."""

# matrix1 = [
#           [1, 2, 3],
#           [4, 5, 6],
#           ]
# matrix2 = [
#           [7, 8],
#           [9, 10],
#           [11, 12]
#           ]
#
# rows1 = len(matrix1)
# cols1 = len(matrix1[0])
# rows2 = len(matrix2)
# cols2 = len(matrix2[0])
#
# print(f"Перша матриця: {matrix1}")
# print(f"Друга матриця: {matrix2}")
#
# if cols1 != rows2:
#     print("Помилка, неможливо виконати множення, розміри матриць не "
#           "відповідають умовам матричного множення")
# else:
#     result = [[0 for _ in range(cols2)] for _ in range(rows1)]  # Створює
#     # нову матрицю
#     for i in range(rows1):  # проходить по кожному рядку першої матриці
#         for j in range(cols2):  # проходить по кожному стовпцю другої матриці
#             for k in range(cols1):  # проходить по минулим
#                 result[i][j] += matrix1[i][k] * matrix2[k][j]
#
#     print("Результат множення матриць: ")
#     for row in result:
#         print(row)

"""
1 Згенерувати випадкове ціле число в діапазоні від 1 до 100.
2 Випадковим чином вибрати елемент зі списку.
3 Перемішати порядок елементів у списку.
4 Згенерувати випадкову послідовність букв заданої довжини.
5 Випадковим чином обрати пароль заданої довжини зі списку допустимих символів.
6 Розіграти лотерею, вибираючи випадковий набір чисел з певного діапазону.
7 Симулювати кидання грального кубика (генерувати випадкове число від 1 до 6).
8 Випадковим чином розподілити учасників на команди для змагань.
9 Згенерувати випадкову дату в певному діапазоні.
10 Випадковим чином змінювати порядок рядків у двовимірному списку (матриці).
"""
# 1
# random_num = random.randint(1, 100)
# print(random_num)
# # 2
# sp = [1, 2, 3, 4, 5]
# random_sp = random.choice(sp)
# print(random_sp)
# # 3
# sps = [1, 2, 3, 4, 5]
# random.shuffle(sps)
# # 4
# lenth = 10
# leters = "".join(random.choices(string.ascii_letters, k=lenth))
# print(leters)
# # 5
# lenth = 10
# variable = string.ascii_letters + string.digits
# password = "".join(random.choices(variable, k=lenth))
# 6
# lottery = 0
# lottery2 = ""
# while lottery <= 8:
#     ran_num = random.randint(1, 200)
#     lottery2 += str(ran_num) + " "
#     lottery += 1
#
# print(f"Результат лотереї: {lottery2}")

# start_range = 1
# end_range = 50
# num_choices = 6
# lottery_numbers = random.sample(range(start_range, end_range + 1), num_choices
# print(lottery_numbers)

# 7
"""Симулювати кидання гральногокубика(генерувати випадкове число від 1 до 6)."""
# dice = random.randint(1, 6)
# print(f"{dice}")

# 8
"""Випадковим чином розподілити учасників на команди для змагань."""
# V1
# players = ["Максим", "Денис", "Назар", "Дмитро"]
# num_teams = 2
# random.shuffle(players)
# teams = [players[i::num_teams] for i in range(num_teams)]
# print("Команди для змагань:")
# for i, team in enumerate(teams, start=1):
#     print(f"Команда {i}: {team}")

# V2
# players = ["Максим", "Денис", "Назар", "Дмитро"]
# num_teams = 2
# teams = [[] for _ in range(num_teams)]
# while players:
#     for i in range(num_teams):
#         if players:
#             random_index = random.randint(0, len(players) - 1)
#             teams[i].append(players.pop(random_index))
#
# print("Команди для змагань:")
# for i, team in enumerate(teams, 1):
#     print(f"Команда {i}: {', '.join(team)}")

# 9
"""Згенерувати випадкову дату в певному діапазоні."""
# start_date = datetime.date(2000, 1, 1)
# end_date = datetime.date(2024, 12, 31)
#
# random_days = (end_date - start_date).days
# random_day_offset = random.randint(0, random_days)
# random_date = start_date + datetime.timedelta(days=random_day_offset)
#
# print(f"Випадкова дата: {random_date}")

# 10
"""Випадковим чином змінювати порядок рядків у двовимірному списку (матриці)."""


# def shuffle_matrix(matrix):
#     random.shuffle(matrix)
#     return matrix
#
#
# matrix = [
#          [1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]
#          ]
#
# print("Початкова матриця:")
# for row in matrix:
#     print(row)
#
# shuffled_matrix = shuffle_matrix(matrix)
#
# print("\nМатриця після випадкового перетасування рядків:")
# for row in shuffled_matrix:
#     print(row)

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

# print("15. Створити список з 10 чисел,потім видалити всі парні числа з нього")
#
# numbers = [22, 34, 97, 89, 41, 56, 78, 91, 13, 65]
# print(f"Список до видалення парних чисел: {numbers}")
# numbers = [num for num in numbers if num % 2 != 0]
# print(f"Список після видалення парних чисел: {numbers}")

# 1
# dictionary = {
#     1: {"Ім`я": "Максим", "Прізвище": "Дарієнко", "Вік": "15"},
#     2: {"Ім`я": "Каріна", "Прізвище": "Хорошун", "Вік": "16"},
#     3: {"Ім`я": "Дмитро", "Прізвище": "Агоштон", "Вік": "15"},
#    4: 10, {"Ім`я": "Олександр", "Прізвище": "Мандзюк", "Вік": "14"},
# 5: {"Ім`я": "Назар", "Прізвище": "Калуга", "Вік": "14"}}

# 2
# name = "Дмитро"
# for person_ID, info in dictionary.items():
#     if info["Ім`я"] == name:
#         print("Вік людини:", info.get("Вік", "Вік не знайдено"))

# 3
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# dict3 = {**dict1, **dict2}
# dict3 = dict1.copy()
# for key, value in dict2.items():
#     dict3[key] = value
# print(dict3)

# 4
# for key, value in dictionary.items():
#     if value == 10:
#         print(key)

# 5
# unique_values = set()
# for value in dictionary.values():
#     unique_values.add(value)
# print(len(unique_values))

# 6
# longest_key = ""
# for key in dictionary.keys():
#     key = str(key)
#     if len(key) > len(longest_key):
#         longest_key = key
# print(longest_key)

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


# 3. Перетворіть рядок з датою ("2024-04-05") в об'єкт datetime.
# date_string = "2024-04-05"
# date_object = datetime.strptime(date_string, "%Y-%m-%d")
# print(f"Об'єкт datetime: {date_object}")

# 4. Виведіть список дат за заданий проміжок часу (наприклад, тиждень) з
# кроком в 1 день.
# start_date = datetime(2024, 4, 5)
# end_date = datetime(2024, 4, 11)
# current_date = start_date
# while current_date <= end_date:
#     print(current_date.strftime("%Y-%m-%d"))
#     current_date += timedelta(days=1)

# 5. Обчисліть, скільки годин, хвилин і секунд минуло з певного моменту часу.
# start_time = datetime(2024, 4, 8, 11, 22, 16)
# time_difference = datetime.now() - start_time
# hours, remainder = divmod(time_difference.seconds, 3600)
# minutes, seconds = divmod(remainder, 60)
# print(f"Пройшло часу: {time_difference.days * 24 + hours}"
#       f" годин, {minutes} хвилин, {seconds} секунд.")

# class Person:
#     def __init__(self, name, age, company):
#         self.name = name
#         self.age = age
#         self.company = company
#
#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Company: {self.company}")
#
#     def __del__(self):
#         print("Видалено людину з ім'ям:", self.name)
#
#
# artem = Person("Артем", 14, "Google")
# print(artem.name)
# print(artem.age)
# print(artem.company)
# artem.age = 15
# print(artem.age)
# artem.display_info()
# sergiy = Person("Сергій", 15, "Microsoft")
# print(sergiy.name)
# print(sergiy.age)
# sergiy.company = "Samsung"
# print(sergiy.company)
# sergiy.display_info()
# andriy = Person("Андрій", 16, "Amazon")
#
#
# class Hello:
#     def say_hello(self, message):
#         print(message)
#
#
# artem = Hello()
# artem.say_hello("hello")


"""
1. Створити клас для представлення точки в 2D просторі:
Клас повинен мати два атрибути: x та y, що відповідають координатам точки.
Додати методи для отримання та встановлення значень атрибутів,
а також для обчислення відстані до іншої точки.
"""


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_x(self):
#         return self.x
#
#     def set_x(self, new_x):
#         self.x = new_x
#
#     def get_y(self):
#         return self.y
#
#     def set_y(self, new_y):
#         self.y = new_y
#
#     def distance(self, other_point):
#         dx = self.x - other_point.x
#         dy = self.y - other_point.y
#         return (dx**2 + dy**2)**0.5
#
#
# point1 = Point(2, 3)
# print(point1.get_x(), point1.get_y())
# point2 = Point(5, 7)
# print(point2.get_x(), point2.get_y())
# distance = point1.distance(point2)
# print(distance)


"""
2. Створити клас для представлення прямокутника:
Клас повинен мати чотири атрибути: x, y, width та height,
що відповідають координатам лівого нижнього кута,
ширині та висоті прямокутника відповідно.
Додати методи для отримання та встановлення значень атрибутів,
а також для обчислення площі та периметра прямокутника.
"""


# class Pryamokutnik:
#     def __init__(self, x, y, width, lenth):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.lenth = lenth
#
#     def get_area(self):
#         return self.width * self.lenth
#
#     def ger_perimetr(self):
#         return (self.width + self.lenth) * 2
#
#     def get_x(self):
#         return self.x
#
#     def set_x(self, new_x):
#         self.x = new_x
#
#     def get_y(self):
#         return self.y
#
#     def set_y(self, new_y):
#         self.y = new_y
#
#     def get_lenth(self):
#         return self.lenth
#
#     def get_width(self):
#         return self.width
#
#
# pryamokutnik1 = Pryamokutnik(3, 4, 5, 2)
# print(pryamokutnik1.get_lenth(), pryamokutnik1.get_width())
# print(pryamokutnik1.get_area(), pryamokutnik1.ger_perimetr())

"""
3. Створити клас для представлення банківського рахунку:
Клас повинен мати два атрибути: balance та interest_rate,
що відповідають залишку на рахунку та процентній ставці відповідно.
Додати методи для отримання та встановлення значень атрибутів,
а також для внесення та зняття коштів, а також для нарахування відсотків.
"""


# class BankAccount:
#     def __init__(self, balance, interest_rate):
#         self.balance = balance
#         self.interest_rate = interest_rate
#
#     def get_balance(self):
#         return self.balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return True
#         else:
#             return False
#
#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate
#         self.balance += interest
#
#
# account = BankAccount(1000, 0.05)
# print(account.get_balance())
# account.deposit(700)
# account.withdraw(300)
# print(account.get_balance())
# account.calculate_interest()
# print(account.get_balance())

