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
n = int(input("Введiть кiлькiсть зiрочок: "))
m = 0
while n > 0:
    print(" " * m + "*" * n)
    n -= 1
    m += 1

# Це другий прямокутний трикутник.
n = int(input("Введiть кiлькiсть зiрочок: "))
m = 1
while n > 0:
    print(" " * (n - 1) + "*" * m)
    n -= 1
    m += 1

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


print("Введіть число:")
number = int(input())
print("Введіть місяць:")
month = (input())
print("Введіть рік:")
year = int(input())
if 21 <= number <= 31 and month == 'березень' or 1 <= number <= 20 and month == 'квітень':
    print("По гороскопу ви Овен.")
elif 21 <= number <= 30 and month == 'квітень' or 1 <= number <= 20 and month == 'травень':
    print("По гороскопу ви Телець.")
elif 21 <= number <= 31 and month == 'травень' or 1 <= number <= 20 and month == 'червень':
    print("По гороскопу ви Близнюки.")
elif 22 <= number <= 30 and month == 'червень' or 1 <= number <= 22 and month == 'липень':
    print("По гороскопу ви Рак.")
elif 23 <= number <= 31 and month == 'липень' or 1 <= number <= 23 and month == 'серпень':
    print("По гороскопу ви Лев.")
elif 24 <= number <= 31 and month == 'серпень' or 1 <= number <= 23 and month == 'вересень':
    print("По гороскопу ви Діви.")
elif 24 <= number <= 30 and month == 'вересень' or 1 <= number <= 23 and month == 'жовтень':
    print("По гороскопу ви Терези.")
elif 24 <= number <= 31 and month == 'жовтень' or 1 <= number <= 22 and month == 'листопад':
    print("По гороскопу ви Скорпіон.")
elif 23 <= number <= 30 and month == 'листопад' or 1 <= number <= 21 and month == 'грудень':
    print("По гороскопу ви Стрілець.")
elif 22 <= number <= 31 and month == 'грудень' or 1 <= number <= 20 and month == 'січень':
    print("По гороскопу ви Козеріг.")
elif 21 <= number <= 31 and month == 'січень' or 1 <= number <= 18 and month == 'лютий':
    print("По гороскопу ви Водолій.")
elif 19 <= number <= 28 and month == 'лютий' or 1 <= number <= 20 and month == 'березень':
    print("По гороскопу ви Риби.")


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
text = input("Введіть текст: ")
text2 = ""
for char in text:
    if not char.isdigit():
        text2 += char
print(text2)

# Task 2
email = input("Введіть електронну пошту: ")
if "@" in email and "." in email:
    print("YES")
else:
    print("NO")

# Task 2 optimized
email = input("Введіть електронну пошту: ")
print("YES") if "@" in email and "." in email else print("NO")


password = input('Введіть ваш пароль: ')
(t, y, u, i, o, p) = (0, 0, 0, 0, 0, 0)
s = "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"
for char in password:
    if len(password) >= 8:
        t = 1
    if char.isdigit:
        y = 1
    if char.isupper:
        u = 1
    if char.islower:
        i = 1
    if any(char in s for char in password):
        o = 1
p = t + y + u + i + o
print(f"Ваша кількість балів: {p}")
if t == 0:
    print("""Ваш пароль складається з менше 8 символів."
    Краще використовувати довші паролі для більшого захисту.""")
if y == 0:
    print("""У Вашому паролі немає чисел.
    Використання чисел в паролі значно підвищує його складність.""")
if u == 0:
    print("""У Вашому паролі немає великих літер.
    Використання великих літер в паролі значно підвищує його складність.""")
if i == 0:
    print("""У Вашому паролі немає маленьких літер.
    Використання маленьких літер в паролі значно підвищує його складність.""")
if o == 0:
    print("""У Вашому паролі немає ніяких знаків.
    Використання знаків в паролі значно підвищує його складність.""")
if p == 5:
    print("Ваш пароль пройшов всі перевірки, ви молодець.")


