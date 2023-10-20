import random
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
try:
    actions = ["+", "-", "*", "/", "quit"]
    number_of_numbers = int(input("Введіть кількість чисел в масиві: "))
    while number_of_numbers < 2:
        number_of_numbers = int(input("Помилка! Кількість чисел в масиві повинна бути не менше 2: "))
    min_randint = int(input("Введіть мінімальне значення цілого випадкового числа: "))
    max_randint = int(input("Введіть максимальне значення цілого випадкового числа: "))
    while min_randint > max_randint:
        max_randint = int(input("Помилка! Ваше максимальне значення менше за мінімальне. Введіть нове значення: "))
    numbers = [random.randint(min_randint, max_randint) for _ in range(number_of_numbers)]
    print(f"Згенерований масив: {numbers}")
    while True:
        print("")
        print("Варіанти: + - * / Або 'quit' щоб вийти з програми.")
        choice = input("Введіть команду для найменшого та найбільшого числа в масиві: ")
        if choice in actions:
            match choice:
                case "+":
                    print(f"{min(numbers)} + {max(numbers)} =", min(numbers) + max(numbers))
                case "-":
                    print(f"{min(numbers)} - {max(numbers)} =", min(numbers) - max(numbers))
                case "*":
                    print(f"{min(numbers)} * {max(numbers)} =", min(numbers) * max(numbers))
                case "/":
                        division_value = float(min(numbers)) / float(max(numbers))
                        rounded_division_value = round(division_value, 2)
                        print(f"{min(numbers)} / {max(numbers)} = {rounded_division_value}")
                case "quit":
                    print("Програму завершено.")
                    break
        else:
            print("Помилка! Ви ввели неправильну команду.")
except ValueError:
    print("Помилка! Ви ввели некоректний тип даних.")
except ZeroDivisionError:
    print("Помилка! Ділити на нуль не можна.")
except Exception:
    print("Помилка! Зв'яжіться з розробником програми.")
