import random
# print(random.randint(1, 10))
""" Виводить рандомне число від 1 до 10 включно"""
# name = "Oleksandr"
# print("Hello " + name)
""" Потрібна для з'єднання текста зі змінною """
# print('#####', '#####' + '#####' + '#####', "#####", sep='\n')
""" sep='\n' потрібна щоб кожний раз виводило на нову строку. Коми для нового рядку. Плюси для з'єднування текстів """
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


print(random.randint(1, 10))
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
