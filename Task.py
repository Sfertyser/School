import random
import string
import datetime
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
