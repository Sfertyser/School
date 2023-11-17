import random
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


def list2d(row=None, column=None):
    if row is None and column is None:
        row = int(input("Введіть довжину строки: "))
        column = int(input("Введіть висоту строки: "))
    elif column is None:
        column = int(input("Введіть висоту строки: "))
    matrix = [[random.randint(0, 200) for _ in range(column)] for _ in range(row)]
    return matrix


def symetrical_table():
    max_len = max(len(str(element)) for st in list2d for element in st)
    for st in list2d:
        row_str = " ".join(str(element).rjust(max_len) for element in st)
        print(row_str)


print("Таблиця без параметрів")
symetrical_table(list2d())
print()
